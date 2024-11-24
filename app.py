from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Templates as Strings
base_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Takshashala</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: white;
            padding: 1em 0;
            text-align: center;
        }
        header nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
        }
        header nav a:hover {
            text-decoration: underline;
        }
        main {
            padding: 20px;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2024 Takshashala</p>
    </footer>
</body>
</html>
"""

home_template = """
{% extends "base_template" %}
{% block content %}
<h1>Welcome to Takshashala</h1>
<p>Your one-stop solution for everything.</p>
{% endblock %}
"""

about_template = """
{% extends "base_template" %}
{% block content %}
<h1>About Takshashala</h1>
<p>Takshashala is dedicated to providing solutions to all your needs.</p>
{% endblock %}
"""

# Routes
@app.route("/")
def home():
    return render_template_string(home_template, base_template=base_template)

@app.route("/about")
def about():
    return render_template_string(about_template, base_template=base_template)

if __name__ == "__main__":
    app.run(debug=True)
