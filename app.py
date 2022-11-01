import os

from flask import Flask, redirect, render_template, request, url_for
from pyflowchart import Flowchart

app = Flask(__name__)

@app.route("/")
def index():
    return f"""<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]>      <html class="no-js"> <!--<![endif]-->
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Flowchart Generator</title>
        <meta name="description" content="A small project which turns python code in flowchart using pyflowchart.">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
        <h1>Flowchart Generator</h1>
        <form action="{url_for('submit')}" method="post">
            <textarea name="code"></textarea>
            <input type="submit">
        </form>
    </body>
</html>"""

@app.route("/submit", methods=["POST"])
def submit():
    codei = request.form.get("code")
    fc = Flowchart.from_code(codei)
    code = fc.flowchart()
    print(code)
    return f"""<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]>      <html class="no-js"> <!--<![endif]-->
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Flowchart Generator</title>
        <meta name="description" content="A small project which turns python code in flowchart using pyflowchart.">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
        <div id="diagram"></div>
            <script src="http://cdnjs.cloudflare.com/ajax/libs/raphael/2.3.0/raphael.min.js"></script>
            <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
            <script src="http://flowchart.js.org/flowchart-latest.js"></script>
            <script>
                let co = `{code}`
                var diagram = flowchart.parse(co);
                diagram.drawSVG('diagram');
            </script>
    </body>
</html>"""

if __name__ == '__main__':
    app.run()
