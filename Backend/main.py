from flask import Flask, render_template, request

app = Flask(__name__)


squared_values = []


@app.route("/")
def home():
	return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    selected_option = request.form.get('option')
    selected_option = int(selected_option)
    
    squared_value = selected_option** 2
    
    squared_values.append(squared_value)
    
    return f'The square of {selected_option} is {squared_value}. Updated list of squares: {squared_values}'



if __name__ == "__main__":
	app.run(debug=True)
