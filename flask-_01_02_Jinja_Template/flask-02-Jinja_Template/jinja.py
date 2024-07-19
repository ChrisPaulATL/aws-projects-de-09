from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def head():
     return 'Hello world Oktay'
@app.route('/secondpage')
def head():
     return 'This is second page'
@app.route('/third')
def head():
     return 'This is third page'
@app.route('/fourth/<string:id>')
def head():
     return f'Id of this page is {id}'

if __name__== "__main__":
     # app.run(debug=True, port=30000)
     app.run(host= '0.0.0.0', port=80)