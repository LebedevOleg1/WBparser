import telebot
from parsing import get_position

bot = telebot.TeleBot("7389037311:AAHuxOzNCL0VbabduuCfOC1hPhxcwvE3yFw")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,
    f"Привет, {message.from_user.first_name}!\nВведите ссылку на товар с Wb.\n"
    f"На следующей строке можете указать количество страниц (от 1 до 10), на которых будет "
    f"производиться поиск. "
    f"Если не укажете, то по умолчанию поиск будет по первым пяти страницам.")


@bot.message_handler()
def main(message):
    try:
        bot.send_message(message.chat.id, "Идёт поиск, пожалуйста, подождите...")
        input_list = message.text.lower().split('\n')
        if len(input_list) == 1:
            pages = 5
            link = input_list[0]
        elif len(input_list) == 2:
            link, pages = input_list
            if int(pages) > 10:
                raise ValueError
        res = get_position(link, int(pages))
        s = '\n\n'.join([': '.join(list(tup)) for tup in res.items()])
        bot.send_message(message.chat.id, s)
    except:
        bot.send_message(message.chat.id, "Некорректный ввод данных.")



bot.polling(none_stop=True)