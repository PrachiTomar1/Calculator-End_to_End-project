# calculator_api.py
from flask import Flask, jsonify
import calculator_backend

app = Flask(__name__)

# Route to handle calculation
@app.route('/calculate/<operation>/<float:num1>/<float:num2>', methods=['GET'])
def calculate(operation, num1, num2):
    if operation == 'add':
        result = calculator_backend.add(num1, num2)
    elif operation == 'subtract':
        result = calculator_backend.subtract(num1, num2)
    elif operation == 'multiply':
        result = calculator_backend.multiply(num1, num2)
    elif operation == 'divide':
        result = calculator_backend.divide(num1, num2)
    else:
        return jsonify({"error": "Invalid operation"}), 400
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)

