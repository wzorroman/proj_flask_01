# proj_flask_01
    Demo with Endpoints - using Flask (framework)


    URL: https://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/

    crear las siguientes variables de entorno en el fichero ".env" activate del entorno virtual.

        export FLASK_APP="entrypoint:app"
        export FLASK_ENV="development"
        export APP_SETTINGS_MODULE="config.default"

# Install requirements    
  (venv)$ marshmallow-sqlalchemy==1.0.0

# Comandos principales de Flask-Migrate
    Los tres comandos principales de Flask-Migrate son:
    Cargar variables de entorno

    - *flask db init:* Crea una estructura de directorios y ficheros necesarios para la ejecución de esta extensión. Se ejecuta solo una vez, al principio.

    - *flask db migrate:* Navega entre los modelos en busca de actualizaciones y genera los ficheros de migración de base de datos con los cambios detectados.

    - *flask db upgrade:* Lleva a cabo la migración de la base de datos.

    ```
        (venv)$ source .env
        (venv)$> flask db init
        (venv)$> flask db migrate -m "Initial_db"
        (venv)$> flask db upgrade
    ```

# El API REST en Flask en funcionamiento
    Ahora sí que podemos poner en marcha la aplicación y probar nuestro API. Para arrancar la aplicación ejecuta el siguiente comando desde el terminal:

        (venv)$> flask run

# Collection
# =============
    ## Añadir una película a la colección
    Envía una petición POST a la URL http://localhost:5000/api/v1.0/films/ con el siguiente contenido:

        {
            "title": "Forrest Gump",
            "length": 8520,
            "year": 1994,
            "director": "Robert Zemeckis",
            "actors": [
                { "name": "Tom Hanks"},
                { "name": "Robin Wright"},
                { "name": "Gary Sinise"},
                { "name": "Mykelti Williamson"},
                { "name": "Sally Field"},
                { "name": "Michael Conner Humphreys"}
            ]
        }

    Obtener la colección de películas
    Realiza una petición GET a la URL http://localhost:5000/api/v1.0/films/. 
    La respuesta será similar a la siguiente:

        [{
            "year": 1994,
            "actors": [
                {
                    "name": "Gary Sinise",
                    "id": 3
                },
                {
                    "name": "Michael Conner Humphreys",
                    "id": 6
                },
                {
                    "name": "Mykelti Williamson",
                    "id": 4
                },
                {
                    "name": "Robin Wright",
                    "id": 2
                },
                {
                    "name": "Sally Field",
                    "id": 5
                },
                {
                    "name": "Tom Hanks",
                    "id": 1
                }
            ],
            "length": 8520,
            "id": 1,
            "director": "Robert Zemeckis",
            "title": "Forrest Gump"
            
        }]
    Obtener el recurso Película con id 1
    Realiza una petición GET a la URL http://localhost:5000/api/v1.0/films/1. 
    La respuesta será:

    {
        "year": 1994,
        "actors": [
            {
                "name": "Tom Hanks",
                "id": 1
            },
            {
                "name": "Robin Wright",
                "id": 2
            },
            {
                "name": "Gary Sinise",
                "id": 3
            },
            {
                "name": "Mykelti Williamson",
                "id": 4
            },
            {
                "name": "Sally Field",
                "id": 5
            },
            {
                "name": "Michael Conner Humphreys",
                "id": 6
            }
        ],
        "length": 8520,
        "id": 1,
        "director": "Robert Zemeckis",
        "title": "Forrest Gump"
    }

# First you should install binary:
  ## On Linux
    sudo apt-get update
    sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
  ## On Mac
    brew install tesseract
  ## On Windows
    download binary from https://github.com/UB-Mannheim/tesseract/wiki. then add pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' to your script.

  ## Then you should install python package using pip:
    pip install tesseract
    pip install tesseract-ocr
    references: https://pypi.org/project/pytesseract/ (INSTALLATION section) and https://tesseract-ocr.github.io/tessdoc/Installation.html

# ----
sudo apt-get install tesseract-ocr-eng 
sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn

pip install tesseract-ocr
sudo apt-get install tesseract-ocr-spa


$flask run --debug

http://127.0.0.1:5000/documentation/upload/