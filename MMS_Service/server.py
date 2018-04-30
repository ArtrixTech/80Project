import uuid
from MMS_Service.mns.demo_sms_send import send_sms
from flask import Blueprint
import urllib

sms = Blueprint('sms', __name__, subdomain='sms')


@sms.route('/send/<template>/<phone>/<content>')
def hello_world(template, phone, content):
    __business_id = uuid.uuid1()

    if not "SMS" in template:
        template = "SMS_133976627"

    try:
        url, content = content.split(",")
    except:
        return "Request Syntax ERROR"

    url = str(url).replace(".com", "-com").replace(".cn", "-cn")

    params = "{\"url_loc\":\"" + url + "\",\"content\":\"" + content + "\"}"
    res = send_sms(__business_id, phone, "Artrix雅智科技", template, params)

    print(res.decode())
    return res.decode()
