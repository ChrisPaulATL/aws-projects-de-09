from flask import Flask 
app = Flask(__name__)

@app.route('/')
def head():
      return 'hello world Chris'


@app.route('/secondpage')
def second():
      return 'this is second page'

@app.route('/thirdpage')
def third():
      return 'this is third page'

@app.route('/fourthpage/<string:id>')
def fourth(id):
      return f'Id of this page is {id}'

if __name__ == '__main__':

    app.run(debug=True)
    app.run(host= '0.0.0.0', port=3000)
















if __name__ == '__main__':

     app.run(debug=True)
     app.run(host= '0.0.0.0', port=80)