import json
from flask import Blueprint

v2ray = Blueprint('v2ray', __name__, subdomain='v2ray')


@v2ray.route('/biforstv/<cfg_name>')
def bfv(cfg_name):
    try:
        with open("vmess_server/config.json", 'r') as load_f:
            load_dict = json.load(load_f)
            return load_dict["bfv"][cfg_name]
    except:
        return "No This Config!"


@v2ray.route('/v2rayn/<cfg_name>')
def v2r(cfg_name):
    try:
        with open("vmess_server/config.json", 'r') as load_f:
            load_dict = json.load(load_f)
            return load_dict["v2rayn"][cfg_name]
    except:
        return "No This Config!"
