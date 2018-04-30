from flask import Flask
import project_blueprints

app = project_blueprints.bind_blueprints(Flask(__name__))
app.config.update({
    'SERVER_NAME': 'artrix.tech'
})

app.run(host="45.76.102.168", port=80)
# app.run(host="127.0.0.1", port=80)
