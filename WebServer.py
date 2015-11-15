'''
Created on Nov 11, 2015
Web Server using flask for Raspberry pi2
@author: Juan_Insuasti
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()