from flask import render_template

from application import app
from application.nocache import nocache

from application.controllers import *

@app.route("/index")
@app.route("/")
def index_route():
	return index.__return__()

'''
# BOARD MODULE
#
@app.route('/board')
# @nocache
def board_route():
    return board.__return__()

@app.route("/lecturer_modal/<id>")
def lecturer_modal(id):
    return board.__return_modal__(id)

# TEST MODULE
#
@app.route('/test', methods=['POST'])
def test_route():
    return test.__return__()
'''    