# Retrieving data using get
# In this step, let us use dummy data and return it as a json. To return it as json, will use json module and Response module.
from flask import Flask,  Response
import json

app = Flask(__name__)