from flask import Flask, Blueprint, render_template

indexBp = Blueprint("index",__name__,template_folder="templates")

@indexBp.route("/")
def index():

    return render_template('index.html')