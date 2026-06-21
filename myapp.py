from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the main home page
@app.route("/")
def home():
    # Variables can be passed to render dynamic content
    return render_template("index.html", title="My Python Webpage")

# Run the local development server
if __name__ == "__main__":
    app.run(debug=True)
