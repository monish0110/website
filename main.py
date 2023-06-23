import flask
from flask import Flask, render_template
app = Flask(__name__)

friends = [
   {
      'name': 'Elon Musk',
      'age': '40',
      'Pro': 'prenuer'
   },
   {
      'name': 'Andrew Tate',
      'age': '37',
      'Pro': 'prenuer'
   },
   {
      'name': 'Tristan Tate',
      'age': '32',
      'Pro': 'prenuer'
   }
]

@app.route('/')
def homepage():
   return render_template('home.html',friends=friends)



if __name__ == '__main__':
   app.run(host='0.0.0.0', debug= True)



   #check
   #check

print("Hello World")   