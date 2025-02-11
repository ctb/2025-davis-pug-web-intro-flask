# 

## Quickstart: install & run

### Clone repo

First, get this repo:
```
git clone https://github.com/ctb/2025-davis-pug-web-intro-flask

cd ./2025-davis-pug-web-intro-flask
```

### Install necessary software

Next, create a new Python virtual environment, e.g.
```
conda create -n 2025-flask -y python=3.12
conda activate 2025-flask
```
and then do:
```
pip install -r requirements.txt
```

### Run the Web app

Assuming everything goes well above, this:
```
python main.py
```
will run the Web app locally, at
[http://localhost:5001/](http://localhost:5001/).

(You'll need to run it on your local laptop for this to connect.)

## A guided tour

See
["Server side Web programming"](https://hackmd.io/kLOnYY8vRtiSptcUU2zonQ?view).

## References and packages used

The underlying Python framework used here is
[Flask](https://flask.palletsprojects.com/en/stable/).

Flask uses [jinja2](https://jinja.palletsprojects.com/en/stable/) for
templating.

We use [the pico CSS framework](https://picocss.com/docs) for the CSS.

Tests are done using [pytest](https://docs.pytest.org/en/stable/index.html) and [the requests library](https://docs.python-requests.org/en/latest/api/).
