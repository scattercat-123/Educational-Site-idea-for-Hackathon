from flask import *
from flask_cors import CORS
import openai
openai.api_key = "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"

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()

    # Access individual values
    grade = data.get('grade')
    subject = data.get('subject')
    topic = data.get('topic')

    # Now you can use these values as needed
    print(f"Received data - Grade: {grade}, Subject: {subject}, Topic: {topic}")
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"I am in grade {grade} and i want 10 questions on {subject} about the topic {topic}"}])
    print(completion.choices[0].message.content)
    



if __name__ == '__main__':
    app.run(debug=True)
