# sentiment-analyzer
A real-time sentiment analysis web app using a pretrained transformer model. By integrated it into a Flask backend and an interactive UI where users can input text and instantly get sentiment predictions with confidence scores
sentiment_analyser
A real-time sentiment analysis web app using a pretrained transformer model. I By integrating into a Flask backend and an interactive UI where users can input text and instantly get sentiment predictions with confidence scores This project demonstrates real-time AI integration using transformer-based NLP models in a production-like environment.

Project Overview

This project is a real-time Sentiment Analysis Web Application that classifies user input text into Positive, Negative, or Neutral sentiment along with a confidence score.

The application uses a pre-trained transformer model from Hugging Face, eliminating the need for manual training while still achieving high accuracy.

--Objectives

Build an interactive AI-powered web application
Perform real-time sentiment analysis on text data
Gain hands-on experience with NLP and transformer models
Deploy and demonstrate an end-to-end ML solution
Features

🔍 Real-time sentiment prediction
📊 Confidence score display
💻 Simple and user-friendly interface
⚡ Fast inference using pre-trained models
🌐 Web-based application using Flask
Tech Stack

Frontend: HTML, CSS
Backend: Flask (Python)
Machine Learning: Hugging Face Transformers
Libraries: torch, transformers
How It Works

User enters text into the input box

The text is sent to the Flask backend

A pre-trained NLP model processes the input

The model returns:

Sentiment (Positive / Negative / Neutral)
Confidence score
Results are displayed on the web interface

Project Structure

sentiment_analyzer/
│
├── main.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── utils/
    └── model.py
Installation & Setup

1.Clone the repository

git clone https://github.com/your-username/sentiment-analyzer.git
cd sentiment-analyzer
Create virtual environment
python -m venv venv
venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Run the application
python main.py
Open in browser
http://127.0.0.1:5000/
Example Outputs

Input Text	Sentiment	Confidence
"I love this product!"	Positive	98%
"This is terrible."	Negative	97%
"It's okay, not great."	Neutral	85%
Future Improvements

Add support for multilingual sentiment analysis
Deploy using cloud platforms (Render / AWS / Azure)
Improve UI with charts and visualizations
Add emotion detection (happy, angry, sad, etc.)
Learning Outcomes

Understanding of NLP and sentiment analysis
Experience with pre-trained transformer models
Building and deploying Flask web applications
End-to-end ML project development
Contribution

Feel free to fork this repository and contribute!

License

This project is open-source and available under the MIT License.

Author

Manvitha B.E. Computer Science and Business Systems