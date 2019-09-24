from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Matt Mastin',
        'title': 'Blog Post 1',
        'content': 'Practicing Flask app stuff',
        'date_posted': 'September 24, 2019'
    },
    {
        'author': 'Mattie M',
        'title': 'Blog Post 2',
        'content': 'Sample content',
        'date_posted': 'September 25, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)