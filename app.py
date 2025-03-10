from flask import render_template,request,Flask
import os
import requests
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipe.html")
@app.route('/analyse')
def analyse():
    return render_template("analyse.html")
@app.route('/get_one')
def get():
    return render_template("cat.html")
@app.route('/analyse_recipes',methods=["GET","POST"])
def analyse_recipes():
    if request.method=="POST":
        recipe=request.form["recipe"]
        ur="https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata"
        re=requests.get(ur)
        if re.status_code==200:
            result=re.json()
            print(result)
            return render_template("analyse.html",res=result["meals"][0]["strInstructions"])
        else:
            return render_template("analyse.html",error="Invalid Recipe Name")
    return render_template("index.html")

@app.route('/find_recipes',methods=["GET","POST"])
def find_recipes():
    if request.method=="POST":
        ingredients=request.form["ingredient"]
        url=f"https://www.themealdb.com/api/json/v1/1/search.php?s={ingredients}"
        res=requests.get(url)
        if res.status_code==200:
            result=res.json()
            return render_template("recipe.html",recipe=result["meals"][0]["strMeal"])
        else:
            return render_template("recipe.html",error="Invalid Ingredients")
    return render("index.html")
@app.route('/cat_recipes',methods=["GET","POST"])
def cat_recipes():
    if request.method=="POST":
        fil=request.form["fil"]
        u="https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood"
        res=requests.get(u)
        if res.status_code==200:
            result=res.json()
            return render_template("cat.html",recipe1=result["meals"][0]["strMeal"],recipe2=result["meals"][1]["strMeal"],recipe3=result["meals"][2]["strMeal"],recipe4=result["meals"][3]["strMeal"])
        else:
            return render_template("cat.html",error="Invalid Category")
    return render("index.html")
if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
