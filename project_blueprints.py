from flask import Flask
from MMS_Service.server import sms
from vmess_server.server import v2ray

all_blueprints = list()

all_blueprints.append(v2ray)
all_blueprints.append(sms)


def bind_blueprints(flask_app):
    assert isinstance(flask_app, Flask)

    for blueprint in all_blueprints:
        flask_app.register_blueprint(blueprint)

    return flask_app
