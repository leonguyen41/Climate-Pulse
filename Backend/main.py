from flask import Flask, render_template, request

app = Flask(__name__)

# This will store submitted data for demonstration purposes
submitted_data = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/submit', methods=['POST'])
def submit():
    # Get the location and selected variable from the form
    location = request.form.get('location')
    selected_variable = request.form.get('variable')

    # Dummy processing: Here you can add actual logic to handle the location and variable
    # For demonstration, just store the inputs
    data = {'location': location, 'variable': selected_variable}
    submitted_data.append(data)
    
    # Returning a response that displays the submitted information
    return f"Location: {location}, Selected Variable: {selected_variable}. Submitted Data: {submitted_data}"

if __name__ == "__main__":
    app.run(debug=True)
