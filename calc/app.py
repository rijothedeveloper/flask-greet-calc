# Put your app in here.
from operations import *

@app.route('add')
def add_route():
    return add(request.args["a"], request.args["b"])

@app.route('sub')
def sub_route():
    return sub(request.args["a"], request.args["b"])

@app.route('mult')
def mult_route():
    return mult(request.args["a"], request.args["b"])

@app.route('div')
def div_route():
    return div(request.args["a"], request.args["b"])

