from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    """Show the homepage"""

    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show form and ask for user's name"""

    return render_template('form.html')


@app.route('/save-name', methods=['POST'])
def save_session():
    """Save user input to session name"""

    name = request.form.get("name")
    session["name"] = name
    return render_template('homepage.html')


@app.route('/results')
def show_results():
    """Show results"""

    return render_template('results.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
