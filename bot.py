import random
import telebot
from local_setting import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "этф игра 'камень ножницы бумага'!"
				 "выберете камень (к), ножницы (н), бумагу (б)")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	user = message.text
	user = user.lower()
	if user not in ["к", "н", "б"]:
		bot.reply_to(message, "выберете между к, н, б")
	else:
		comuter = random.choice(["к", "н", "б"])
		if user == "к" and comuter == "н":
			bot.reply_to(message, "выйграл")
		elif user == "н" and comuter == "б":
			bot.reply_to(message, "выйграл")
		elif user == "б" and comuter == "к":
			bot.reply_to(message, "выйграл")
		elif user == comuter:
			bot.reply_to(message, "ничья")
		else:
			bot.reply_to(message, "ты проиграл  боту ")



bot.infinity_polling()