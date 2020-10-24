from flask import Flask, render_template, session

app = Flask(__name__)

#app.secret_key = 'personal secret'
#app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")

def home():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

if __name__ == "__main__":
  app.run(debug=True)