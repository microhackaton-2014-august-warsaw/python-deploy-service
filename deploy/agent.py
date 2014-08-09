#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import call

from flask import Flask
app = Flask(__name__)

@app.route("/deploy/<service_name>")
def deploy(service_name):
    call(["ansible-playbook", "-i", "local.inv", "deploy.yml", "-s", "-e", "service_name=" + service_name])

    return service_name

if __name__ == "__main__":
    app.run(debug=True)
