import random
import telebot
from local_setting import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

user_core = {}
user_core[chat.id] = {"bot": 1, "user": 1}
user_core = {'bot': 0, 'user': 0}
print(user_core)
text = int(input('Введите значение:'))
if text == 2:
	print(user_core['bot': +2])

print(user_core)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id,  "этф игра 'камень ножницы бумага'!"
				 "выберете камень (к), ножницы (н), бумагу (б)")


#user_score = dict()
# {chat-id: {"user": 1, "bot": 2}}

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	user = message.text
	user = user.lower()
	if user not in ["к", "н", "б"]:
		bot.reply_to(message, "выберете между к, н, б")
	else:
		computer = random.choice(["к", "н", "б"])
		if user == "к" and computer == "н":

			bot.reply_to(message, "выйграл")
		elif user == "н" and computer == "б":
			bot.reply_to(message, "выйграл")
		elif user == "б" and computer == "к":
			bot.reply_to(message, "выйграл")
		elif user == computer:
			bot.reply_to(message, "ничья")
		else:
			bot.reply_to(message, "ты проиграл  боту ")



bot.infinity_polling()


# number = 10
# number += 1
# print(number)  # 11
# def do_something():
# 	chislo = 20
# 	print(chislo)
# 	number += 1  # глобальные переменные нельзя изменять в функциях
#
#
# print(number)
