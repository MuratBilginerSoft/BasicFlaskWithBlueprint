from flask import Flask,Blueprint,render_template

loginBp =  Blueprint("login", __name__, template_folder="templates")

@loginBp.route("/login")
def login():

    return render_template("login.html")