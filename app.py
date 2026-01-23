from flask import Flask, render_template

app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'AI Engineer',
        'location': 'London',
        'salary': '$200,000'
    },
     {
        'id': 2,
        'title': 'GenAI Engineer',
        'location': 'Utah',
        #'salary': '$180,000'
    },
     
      {
        'id': 3,
        'title': 'ML Engineer',
        'location': 'Remote',
        'salary': '$150,000'
    },
      
    {
        'id': 4,
        'title': 'Data Engineer',
        'location': 'Denver',
        'salary': '$140,000'
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)


if __name__ == "__main__":
    app.run(debug=True)