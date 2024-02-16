import logging
import os
import io
import json

from flask import render_template, redirect, url_for, request, flash
from flask import jsonify, send_file, after_this_request
from werkzeug.utils import secure_filename

from app.auth.decorators import admin_required
from app.auth.models import User
from app.documentation.views.doc_reader import DocReader
from app.documentation.views.doc_report import build_report

from . import admin_docs


logger = logging.getLogger(__name__)


ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@admin_docs.route('/documentation/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if not file:
            flash('Not found file in request')
            return redirect(request.url)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        elif file and not allowed_file(file.filename):
            flash('Not file extensions allowed')
            return redirect(request.url)        
        
        file_name = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        # return redirect(url_for('download_file', name=file_name))
        dr = DocReader()
        has_error, str_doc = dr.read_file(file_name=file_name, current_file=file)
        
        return f'''
            <!doctype html>                
            <h1>Result</h1>
            <table border='1'>
                <tr><td>NAME: {file_name}</td></tr>
                <tr><td>{str_doc}</td></tr>
            </ul>
                
            '''
    # in method GET
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>        
        <form method=post enctype=multipart/form-data>
            <input type=file name=file>
            <input type=submit value=Upload>
        </form>
    '''


@admin_docs.route('/documentation/process/', methods=['POST'])
def process_file():
    dict_response = {"error": True, "message": "", "data": None, "status": 500}
    if 'file' not in request.files:
        dict_response["message"] = "No file part in the request"
        dict_response["status"] = 400
        resp = jsonify(dict_response)
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        dict_response["message"] = "No file selected for uploading"
        dict_response["status"] = 400
        resp = jsonify(dict_response)
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        dr = DocReader()
        has_error, str_doc = dr.read_file(file_name=filename, current_file=file)
        
        dict_response.update({
            "error": has_error,
            "message": str_doc if has_error else "ok",
            "data": "" if has_error else str_doc,
            "status": 200
        })
        resp = jsonify(dict_response)
        resp.status_code = 200
        return resp
    else:
        dict_response["message"] = 'Allowed file types are pdf, png, jpg, jpeg, gif'
        dict_response["status"] = 200
        resp = jsonify(dict_response)
        resp.status_code = 400
        return resp


@admin_docs.route('/documentation/generate-report/', methods=['POST'])
def generate_report():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        a = json.loads(request.data)  
        # correct type      
    else:
        a = "No es un tipo json"    
    
    request_data = request.get_json()    
    
    res = build_report(data=request_data)
    
    # current_working_directory = os.getcwd()
    # print(f"{current_working_directory=}") 
    # >> proj_flask_demo_1/proj_flask_01
    
    # remove previous files
    url_file_tmp = 'informe.docx'
    exist_file = os.path.isfile(url_file_tmp)
    if exist_file:
        os.remove(url_file_tmp)    

    # create file temporal 
    with open("informe.docx", "wb") as f:
        f.write(res.read())
    
    # preparate file for delete after response
    file_path = url_file_tmp
    file_handle = open(file_path, 'r')
        
    @after_this_request
    def remove_file(response):
        try:
            os.remove(file_path)
            file_handle.close()
        except Exception as error:
            admin_docs.logger.error("Error removing or closing downloaded file handle", error)
        return response
    
    # return file in response
    return send_file (
        "../informe.docx", 
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document", 
        download_name="informe.docx" 
    )
    