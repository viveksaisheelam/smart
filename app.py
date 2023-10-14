# importing Flask and other modules
from flask import Flask, request, render_template,redirect,url_for
import pickle
# from sklearn import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features=20000, ngram_range=(1,3),analyzer='char')
# Flask constructor
app = Flask(__name__) 

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =['GET', 'POST'])
def gfg():
    #  if(request.method == "POST"):
    #      first_name = request.form.get("fname")
    #     # getting input with name = lname in HTML form 
    #      last_name = request.form.get("lname") 
    #      return "Your name is "+first_name + last_name
    return render_template("home.html")
@app.route('/success/<int:score>',methods=["GET","POST"])
def success(score):
    return "The person has passed and marks is:"+str(score)
@app.route('/analysis',methods=["GET","POST"])
def analysis():
    if request.method =="POST":
        review=request.form['rev']
        # mod=pickle.load(open("model.pkl","rb"))
        mod=pickle.load(open("model.pkl","rb"))
        trans=tfidf.transform(review)
        mod.predict(trans)
        return "your review is :::"+mod
@app.route("/validate_user",methods=["POST","GET"])
def validate_user():
    if request.method =='POST':
        usrnm=request.form['name']
        pass1=request.form['pas']
        k="success"
        return "success"
@app.route('/index',methods=["GET",'POST'])
def index():
    return render_template("index.html")
if __name__=='__main__': 
    app.run(debug=True,port=8000)
