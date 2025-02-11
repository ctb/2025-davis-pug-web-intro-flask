# classes & functions
from flask import Flask
from flask import app

# run this function once, to create the Flask applicaton.
def create_app():
    app = Flask(__name__)

    return app

# run create_app on import
app = create_app()

###
### define pages here
###

@app.route('/', methods=['GET'])
def index():
    return """hello, world!
    <p>
    <img src='/static/vase.jpg'/>
    <br>
    See: <a href='https://commons.wikimedia.org/wiki/File:33344-Mei%C3%9Fen-2008-Mei%C3%9Fner_Bleikristall_(Vase_und_Burg)-Br%C3%BCck_%26_Sohn_Kunstverlag.jpg'>source for vase image</a>
"""    
    
###
### run as app - 'python main.py'. Can also do 'flask --app main.py run'.
###

# not for production - run on localhost:5001
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
