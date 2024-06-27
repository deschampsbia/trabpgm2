from flask import Flask, render_template, request, redirect
from pony.orm import *

db = Database()
app = Flask(__name__)
