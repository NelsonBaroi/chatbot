from flask import Flask, request, jsonify, render_template
from g4f.client import Client

# Initialize Flask app
app = Flask(__name__)

# Initialize the gpt4free client
client = Client()

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to handle chatbot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    # Get the user's message from the request
    user_message = request.form['user_message']

    # Generate a response using gpt4free
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}],
        web_search=False
    )
    bot_response = response.choices[0].message.content

    # Return the response as JSON
    return jsonify({'response': bot_response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)