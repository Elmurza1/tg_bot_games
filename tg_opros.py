import telebot
from local_setting import API_TOKEN3

survey_bot = telebot.TeleBot(API_TOKEN3)

participant_responses = {}
participant_answers = {}

survey_questions = [
    "любимое время года?",
    "либмая игра?",
    "какую профессию ты выбрал?"
]


def send_survey_question(message):
    chat_id = message.chat.id
    current_survey = participant_responses.get(chat_id)
    current_answers = participant_answers.get(chat_id, [])
    question_number = len(current_answers)

    if question_number == len(survey_questions):
        survey_bot.send_message(chat_id, "ты пррошел опрос нифига себе достижения!")
        send_responses_to_organizer(chat_id)
        return

    survey_bot.send_message(chat_id, survey_questions[question_number])
    participant_responses[chat_id] = current_survey


def send_responses_to_organizer(participant_chat_id):
    answers = participant_answers.get(participant_chat_id)
    if answers:
        message_text = f" chat_id пользователя и ответы {participant_chat_id}: \n"
        for i, answer in enumerate(answers, start=1):
            message_text += f"вопрос {i}: {answer}\n"
        survey_bot.send_message(5889846876, message_text)


@survey_bot.message_handler(commands=['start'])
def initiate_survey(message):
    chat_id = message.chat.id

    participant_responses[chat_id] = True
    participant_answers[chat_id] = []
    send_survey_question(message)


@survey_bot.message_handler(func=lambda message: True)
def process_message(message):
    chat_id = message.chat.id
    current_survey = participant_responses.get(chat_id)

    if current_survey:
        participant_answers[chat_id].append(message.text)
        send_survey_question(message)

survey_bot.polling()