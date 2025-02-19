from flask import Flask, render_template, request  # Import necessary modules

app = Flask(__name__)  # Create a Flask app instance

@app.route("/")  # Define a route for the root URL ("/")
def index():
    return render_template("index.html")  # Render the index.html template

@app.route("/about")  # Define a route for the "/about" URL
def about():
    return render_template("about.html")  # Render the about.html template

# Add more routes as needed

# Example of handling a form submission
@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")  # Get data from the form
        return f"Hello, {name}!"  # Process the data and return a response
    return "Invalid request"

# Remove this for Render deployment!
# if __name__ == "__main__":
#     app.run(debug=True)  # Run the app in debug mode (only for local development)
