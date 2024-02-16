import io
import PyPDF2
import pytesseract
from PIL import Image

class DocReader:
    IMAGE_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]
    PDF_EXTENSIONS = ["pdf", ]
    ALLOWED_EXTENSIONS = []
    
    def __init__(self, allow_pdf: bool = True, allow_img: bool = True):
        if allow_pdf:
            self.ALLOWED_EXTENSIONS += self.PDF_EXTENSIONS
        if allow_img:
            self.ALLOWED_EXTENSIONS += self.IMAGE_EXTENSIONS 
        
    def file_extension(self, file_name: str) -> str:
        if not file_name:
            return None
        return file_name.rsplit('.', 1)[1].lower()
    
    def read_pdf(self, current_file) -> str:
        lector_pdf = PyPDF2.PdfReader(current_file)
        texto_total = ''
        for pagina in range(len(lector_pdf.pages)):
            pagina_obj = lector_pdf.pages[pagina]
            texto_total += pagina_obj.extract_text()
        return texto_total
    
    def read_image(self, current_file):
        current_image = Image.open(current_file)
        # Convierte la imagen a texto
        text = pytesseract.image_to_string(current_image, lang='spa')
    
        # Retorna el resultado
        return text

    def read_file(self, file_name, current_file) -> tuple:
        """
            file_name (str)
            current_file (io Bytes)

        Return (tuple):
            (bool) = Has error [True | False]
            (str) = Text content in File or detail error
        """
        current_ext = self.file_extension(file_name=file_name)
        if current_ext not in self.ALLOWED_EXTENSIONS:
            return True, "Tipo de archivo NO PERMITIDO"
        if current_ext in self.IMAGE_EXTENSIONS:
            return False, self.read_image(current_file=current_file)
        elif current_ext in self.PDF_EXTENSIONS:
            return False, self.read_pdf(current_file=current_file)
        else:
            return False, ""
