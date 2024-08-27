from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Placeholder Python function
def example_function():
    return "This is a response from Python"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-python-function', methods=['GET'])
def run_python_function():
    result = example_function()
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
