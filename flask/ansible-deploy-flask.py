# Flask Site For ZandA Digital Ocean (DO_) Ansible playbooks.
# --- In line editing of YAMLs through web browser
# --- Browser Push Notifications (BPN) 
#	--- Alerts when DO_ playbook construction is happening
#	--- iTeam |Messaging 

# Libraries 
# GCM Push Messages
# --- Manifest & Service workers to subscribe
# --- Saving the UID's

from flask import Flask
from flask.ext.pymongo import PyMongo
from flask import render_template, send_from_directory, request, jsonify
import os
import random
import logging
import datetime 
import pymongo
from pymongo import MongoClient
import json

# 
#
#


client = MongoClient()
app = Flask(__name__, static_url_path='')
mongo = PyMongo(app)
app.debug = True

CURR_DIR = os.getcwd()
APP_NAME = "ansible.deploy.zinglax"
VENV_NAME = 'ansible'
STATIC_DIR = os.path.join(CURR_DIR, APP_NAME, "static")
GIT_DIR = os.path.join("/home", "dylan", "GITHUBS", APP_NAME)
db = client.ansible_do_site

# Passed in to all templates
script_args = {}

def create_user(name):

	# creating users
	users = db.users
	user = {"name":"djameszinglax"}
	return users.insert_one(user).inserted_id


@app.route('/', methods=['GET', 'POST'])
def home_page():

	if request.method == 'POST' :
		content = request.json
		print "POST content: " + str(content)

		if 'enable_subscription' in content:
			print 'POST TYPE: enable subscription'
		if 'disable_subscription' in content:
			print 'POST TYPE: disable subscription'
	if request.method == 'GET' :
		pass

	return render_template('./index.html', script_args=script_args)


if __name__ == '__main__':
    app.run(host='192.168.1.148')


'''
<script src="libs/CodeMirror/lib/codemirror.js"></script>
<link rel="stylesheet" href="libs/CodeMirror/lib/codemirror.css">
<script src="libs/CodeMirror/mode/javascript/javascript.js"></script>

<script>


var myCodeMirror = CodeMirror(document.body, {
  value: "function myScript(){return 100;}\n",
  mode:  "javascript"
});


</script>
'''