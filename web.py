from flask import Flask, render_template,jsonify,url_for

app = Flask(__name__)
# JOBS=[
#   {
#     'id':1,
#     'title':'Python Developer',
#     'location':'New York',
#     'salary':50000
#   },
#   {
#     'id':2,
#     'title':'Data Scientist',
#     'location':'Terre Haute',
#     'salary':60000
#   },
#   {
#     'id':3,
#     'title':'Frontend Engineer',
#     'location':'Remote',
#     'salary':80000
#   }
  
# ]

@app.route("/")
def first_web():
    return render_template('home.html')
  
# @app.route("/api/jobs")
# def list_jobs():
#   return jsonify(JOBS)
@app.route("/thank-you")
def thank_you():
    return render_template('thank-you.html')

@app.route('/word_count_result')
def word_count_result():
    word_count = request.args.get('count')
    return render_template('word_count_result.html', word_count=word_count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)