from flask import Flask
from flask import render_template 
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():   
    return render_template("index.html")

@app.route("/movie")
def movie():
    dataList = []
    conn = sqlite3.connect("movie250.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM movie250"
    data = cursor.execute(sql)
    for item in data:
        dataList.append(item)
    cursor.close()
    conn.close()
    
    return render_template("movie.html", movies = dataList)

@app.route("/score")
def score():   
    score = [] #评分
    num = [] #评分人数
    conn = sqlite3.connect("movie250.db")
    cur = conn.cursor()
    sql = "select score, count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        num.append(str(item[1]))

    cur.close()
    conn.close()
    
    return render_template("score.html", score = score, num = num)

@app.route("/word")
def word():   
    return render_template("word.html")

@app.route("/team")
def team():   
    return render_template("team.html")



if __name__ == "__main__":
    app.run()