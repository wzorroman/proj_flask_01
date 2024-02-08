# proj_flask_01
Demo with Endpoints - using Flask (framework)


URL: https://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/

crear las siguientes variables de entorno en el fichero activate del entorno virtual.

    export FLASK_APP="entrypoint:app"
    export FLASK_ENV="development"
    export APP_SETTINGS_MODULE="config.default"

# Crear la base de datos y las tablas
Para crear la base de datos y las tablas, vamos a hacer uso de la extensión Flask-Migrate. Ejecuta lo siguientes comandos en el terminal:
```
  $> flask db init
  $> flask db migrate -m "Initial_db"
  $> flask db upgrade
```

# El API REST en Flask en funcionamiento
Ahora sí que podemos poner en marcha la aplicación y probar nuestro API. Para arrancar la aplicación ejecuta el siguiente comando desde el terminal:

    $> flask run

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

    [
        {
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
        }
    ]
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
