import os
import json
import random
from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

# Load quiz data.
# For a more robust solution, you could have a JSON file per class.
# For this example, we'll use a single file with a nested structure.
try:
    with open('questions.json', 'r') as f:
        quiz_data = json.load(f)
except FileNotFoundError:
    quiz_data = {}

# Replace with your actual key
API_KEY = "YOUR_SUPER_SECRET_KEY"

@app.route("/")
def home():
    """
    Handles the root path, displaying usage information and redirecting to the author's Telegram.
    """
    usage_info = {
        "message": "Welcome to the Random Quiz Generator API!",
        "usage": "Access the API by using the /api endpoint with a valid API key.",
        "example": "/api?class=10&XYZ=" + API_KEY,
        "author": "LORD_SIDDHARTH",
        "author_telegram": "https://t.me/LORD_SIDDHARTH"
    }
    return jsonify(usage_info)

@app.route("/api")
def api():
    """
    API endpoint for generating quizzes.
    Requires an API key (XYZ) and a class number.
    """
    api_key = request.args.get('XYZ')
    
    if api_key != API_KEY:
        return jsonify({"error": "Invalid API key"}), 401
    
    class_num = request.args.get('class')
    
    if not class_num:
        return jsonify({"error": "Missing 'class' parameter"}), 400
    
    try:
        class_num = str(int(class_num))
    except ValueError:
        return jsonify({"error": "Invalid 'class' parameter. Must be a number."}), 400
    
    if class_num not in quiz_data:
        return jsonify({"error": f"No quiz data found for class {class_num}"}), 404
    
    questions = quiz_data[class_num]
    if not questions:
        return jsonify({"error": f"No questions available for class {class_num}"}), 404

    random_quiz_question = random.choice(questions)
    
    return jsonify(random_quiz_question)

if __name__ == "__main__":
    # This is for local development only.
    # Vercel handles the production server.
    app.run(debug=True)
        <a href="#">Forgot password?</a>
      </div>
    </div>

    <div class="input_box">
      <input type="submit" class="input-submit" value="Login">
    </div>

    <div class="register">
      <span>Don't have an account? <a href="#">Register</a></span>
    </div>
  </div>
</div>
<!-- partial -->
  
</body>
</html>
