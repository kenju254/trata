from flask import Flask

#instance of the class Flask being initiated.
app = Flask(__name__)

#route decorate to define Flask URLs and methods defines the 
#the HTTP methods allowed.
@app.route('/<int:number>/')
def inctementer(number):
    return "Incremented number is  " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello  " + name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)