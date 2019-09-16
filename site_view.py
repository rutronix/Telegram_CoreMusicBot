import json

from flask import request, render_template

from app import server, db


@server.route('/api/<user>/api/', methods=['GET', 'POST'])
def api(user):
    return 'Hello API World!'