from flask import Flask
from app.configs import Config  # Configs for app

app = Flask(__name__)
app.config.from_object(Config)  # Link configs for app (.env)


from app.routes.general import home
