from flask import Flask, jsonify
import json

# Create Flask application
app = Flask(__name__)

# Define API route
@app.route('/api', methods=['GET'])
def get_data():

    # Read data from JSON file
    with open('data.json', 'r') as file:
        data = json.load(file)

    # Return data as JSON response
    return jsonify(data)


# Run Flask application
if __name__ == '__main__':
    app.run(debug=True)
