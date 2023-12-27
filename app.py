from flask import Flask , jsonify

#instance of the class Flask being initiated.
app = Flask(__name__)

#route decorate to define Flask URLs and methods defines the 
#the HTTP methods allowed.
@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))

@app.route('/person/')
def hello():
    return jsonify (
        {'name':'Kenneth',
         'address':'Nairobi'}
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)