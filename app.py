from flask import Flask, render_template, request
from utils import create_page, search_page, get_page

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", page = create_page())

@app.route("/search", methods=['GET'])
def search():
    res = search_page(request.args.get("q"))
    return(render_template("results.html", results = res, q = request.args.get("q"), result_len = len(res)))

@app.route("/page/<int:page_id>")
def page(page_id):
    return render_template("page.html", info=get_page(page_id), id=page_id)