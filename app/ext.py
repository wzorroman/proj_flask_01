from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


# Flask Marshmallow: Es una extensión que facilita la serialización
# de los modelos de la base de datos a JSON y viceversa. 
# Está basada en Marshmallow.
ma = Marshmallow()
migrate = Migrate()
