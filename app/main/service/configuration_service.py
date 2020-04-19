import uuid
import datetime

from app.main import db
from app.main.model.user import User


def retrieve_config():
    config_object = {
        'Playlist': '0',
        'MessageOfTheDay': 'This is a promotional marketing message from the server',
    }
    return config_object, 200