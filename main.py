# classes & functions
from flask import Flask, render_template, redirect, url_for
from flask import app, request  # these are frequently used objects.

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
    return """hello, world!<p>
links to try:
    <ul>
    <li> <a href='/user/user1'>User 1 link</a>
    <li> <a href='/example_form'>An example form (GET)</a>
    <li> <a href='/example_form2'>Another example form (POST)</a>
    </ul>
    <p>
    <img src='/static/vase.jpg'/>
    <br>
    See: <a href='https://commons.wikimedia.org/wiki/File:33344-Mei%C3%9Fen-2008-Mei%C3%9Fner_Bleikristall_(Vase_und_Burg)-Br%C3%BCck_%26_Sohn_Kunstverlag.jpg'>source for vase image</a>
"""    

@app.route('/user/<username>')
def user_fn(username):
    # here you would do some kind of validation for logins, etc.
    return f"this is the user page for user '{username}'"

@app.route('/example_form', methods=['GET'])
def example_form():
    return render_template('example_form.html')

@app.route('/example_form_process', methods=['GET'])
def example_form_process():
    value = request.args.get('the_number')
    if value is None:
        return redirect(url_for('example_form'))
    else:
        values=dict(the_number=value)
        return render_template('example_form_process.html',
                               **values)

@app.route('/example_form2', methods=['GET'])
def example_form2():
    return render_template('example_form2.html')

@app.route('/example_form_process2', methods=['POST'])
def example_form_process2():
    upper_limit = request.form.get('upper_limit')
    multiply_by = request.form.get('multiply_by')

    # error handling...
    try:
        upper_limit = int(upper_limit)
        multiply_by = int(upper_limit)
    except ValueError:
        upper_limit = None
        multiply_by = None

    if upper_limit is None or multiply_by is None:
        return redirect(url_for('example_form2'))
    else:
        values=dict(upper_limit=upper_limit,
                    multiply_by=multiply_by)
        return render_template('example_form_process2.html',
                               **values)

###
### run as app - 'python main.py'. Can also do 'flask --app main.py run'.
###

# not for production - run on localhost:5001
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
