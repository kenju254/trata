from flask import Flask

#instance of the class Flask being initiated.
app = Flask(__name__)

#route decorate to define Flask URLs and methods defines the 
#the HTTP methods allowed.
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)