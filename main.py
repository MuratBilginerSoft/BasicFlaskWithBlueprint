from flask import Flask,Blueprint,render_template
from view.index import *
from view.login import *


app = Flask(__name__)

app.register_blueprint(indexBp)
app.register_blueprint(loginBp)

if __name__ == "__main__":
    app.run(debug=True)