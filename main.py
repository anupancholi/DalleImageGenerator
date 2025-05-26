from flask import Flask, jsonify, render_template
import os
import openai

openai.api_key = os.environ['OPENAI_KEY']

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generateimages/<prompt>')
def generate_images(prompt):
    print("prompt is:", prompt)
    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,  # DALL·E 3 allows only 1
            size="1024x1024")
        url = response.data[0].url
        return jsonify({'images': [url]})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
