import telebot

BOT_TOKEN = "6003025515:AAGaHvoCG9hHpVHS2KvE0ivmdtAJEzI5h7k"
bot = telebot.TeleBot(BOT_TOKEN)

# ZPhisher ya ngrok ka demo phishing link
PHISHING_LINK = "https://your-ngrok-or-zphisher-link"

@bot.message_handler(commands=['start'])
def send_link(message):
    user_id = message.chat.id
    bot.send_message(user_id, f"🔗 This is your phishing awareness demo link:\n{PHISHING_LINK}\n\n⚠️ Do not misuse this. Educational only.")
    # Yahan aage victim data collect karne ka system add karenge

bot.polling()
