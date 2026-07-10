from flask import Flask,render_template,request
from scrapper import(search_incruit,search_saramin)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword=request.args.get("keyword")
    incruit_jobs = search_incruit(keyword)
    saramin_jobs = search_saramin(keyword)
    jobs=incruit_jobs + saramin_jobs
    return render_template("search.html",incruit_jobs=enumerate(incruit_jobs),saramin_jobs=enumerate(saramin_jobs),keyword=keyword,count=len(jobs))



if __name__ == '__main__':
    app.run(debug=True)

