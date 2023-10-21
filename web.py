from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Python Developer',
    'location':'New York',
    'salary':50000
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Terre Haute',
    'salary':60000
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':80000
  }
  
]

@app.route("/")
def first_web():
    return render_template('home.html',jobs=JOBS)
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)