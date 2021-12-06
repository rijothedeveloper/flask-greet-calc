# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
    result = add(int(request.args.get("a")), int(request.args.get("b")))
    return str(result)

@app.route('/sub')
def sub_route():
    return str(sub(int(request.args.get("a")), int(request.args.get("b"))))

@app.route('/mult')
def mult_route():
    return str(mult(int(request.args.get("a")), int(request.args.get("b"))))

@app.route('/div')
def div_route():
    return str(div(int(request.args.get("a")), int(request.args.get("b"))))



# part 2

operations = {"add": add,
              "sub": sub,
              "mult": mult,
              "div": div }

@app.route("/math/<oper>")
def math_operation(oper):
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations[oper](a, b)
    return str(result)

 
