from flask import Flask, render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


# Create a flask instance
app= Flask(__name__)
#Create a secret key but dont push it to git bcz when git is public. There is a problem. For now leave it blank .
app.config['SECRET_KEY'] = "NO SECRET KEY FOR NOW"

# Create a form class 
class namerForm(FlaskForm):
    name = StringField("What's your Name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

#Create a name page
@app.route('/name', methods =['GET','POST'])
def name():
    name = None
    form = namerForm()
    if form.validate_on_submit():
        name= form.name.data
        form.name.data = ''
        flash("Form submitted successfully !!! ")

    return render_template("name.html", name = name,form = form)
    


# Create a flask route(decorator)-creating URL
# ('/') this is the endpoint of the URL - This is homepage
# ('/about.html') or ('/about') is a route to about page
@app.route('/')
def home():
    return "<h1>Hello World !</h1>"   #Putting this is html tag in not mandatory

@app.route('/user/<name>')  #here name is a variable and you can change name on URL in browser
def user(name):
     return"<p>How are you {} </p>".format(name)
                                           


#CREATED A NEW TEMPLATE AND RENDERED IT
@app.route('/new/')
def new_page():
    skills_tolearn= ["Jinja2", "Databases","Python","Javascript","PowerBI", 41]
    return render_template("index.html",skills_tolearn=skills_tolearn)

@app.route('/temp/<name>')
def temp(name):
    return render_template("user.html",name=name)

@app.route('/subs/')
def subs():
    first_name = "Castro"
    stuff="Trying to use <strong>safe stuff</strong>"
    stuff1="Trying to use filters"
    flash("Welcome to our website !")
    trim = "Lets check    how                  trim    works"
    skills_tolearn= ["Jinja2", "Databases","Python","Javascript","PowerBI", 41]
    return render_template("index.html",first_name=first_name,  stuff=stuff, stuff1=stuff1,trim=trim,skills_tolearn=skills_tolearn)


# CREATE CUSTOM ERROR PAGES
# Invalid URL

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500



#TO ACTIVATE DEVELOPMENT MODE
if __name__ == '__main__':
     app.run(debug=True)
