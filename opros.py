import telebot
import random


bot = telebot.TeleBot("7113750736:AAFA-LJuXUH_Ri8gZ7j9R2ICk7k3dHsqg9w")
list_for_knb = ['к', 'н', 'б']
users_counter = 0
bots_counter = 0
users_count = 0

result_dict = {}  # chat.id: result-value
result_dict = {"bot": 1, "user": 1}
result_dict = {'bot': 0, 'user': 0}
print(result_dict)
text = int(input('Введите значение:'))
if text == 2:
    result_dict['bot': +2]
print(result_dict)


@bot.message_handler(commands=['start', 'help', 'game'])
def starting(message):
    bot.send_message(message.chat.id, 'Здраствуйте, давайте поиграем в камень ножницы бумага')
    result_dict[message.chat.id] = users_counter, bots_counter


@bot.message_handler(func=lambda message:True)
def knb(message):
    random_knb = random.choice(list_for_knb)
    user_knb = message.text.lower()
    if user_knb == random_knb:
        bot.send_message(message.chat.id, 'НИЧЬЯ')
    elif user_knb == 'к' and random_knb == 'н':
        bot.send_message(message.chat.id, 'Мой выбор ножницы и вы выиграли')
        result_dict[message.chat.id] = users_counter + 1, bots_counter
        bot.send_message(message.chat.id, result_dict[message.chat.id])
    elif user_knb == 'к' and random_knb == 'б':
        bot.send_message(message.chat.id, 'мой выбор бумага и я выиграл')
    elif user_knb == 'н' and random_knb == 'б':
        bot.send_message(message.chat.id, 'мой выбор бумага и вы выиграли')
    elif user_knb == 'н' and random_knb == 'к':
        bot.send_message(message.chat.id, 'мой выбор камень и вы выиграли')
    elif user_knb == 'б' and random_knb == 'к':
        bot.send_message(message.chat.id, 'мой выбор камень и вы выиграли')
    elif user_knb == 'б' and random_knb == 'н':
        bot.send_message(message.chat.id, 'мой выбор ножницы и я выиграл')
    else:
        bot.send_message(message.chat.id, 'Вы ввели не верное значение, введите к или н или б')


bot.infinity_polling()