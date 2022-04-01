import schedule
from threading import Thread
from time import sleep
from cours import Cours
import requests
import datetime
import dotenv
import os


def schedule_checker():
    while True:
        schedule.run_pending()
        # on vérifie si on est dans le créneau d'envoi toutes les 15 minutes (le créneau = 16 minutes ou moins avant le début)
        sleep(15*60)


def telegram_bot_sendtext(bot_message):
    dotenv.load_dotenv()
    bot_token = os.environ['KEY']
    bot_chatID = os.environ['NUMBER']
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)


def journee(msg):
    now = datetime.datetime.today()
    d = now.strftime("%H%M")
    for i in range(len(msg)):
        # on vérifie si on est dans le créneau d'envoi, à partir de 16 minutes avant le début du cours
        if (int(msg[i][0]) - int(d))**2 <= 16**2:
            telegram_bot_sendtext(msg[i][1])
            msg[i][0] = 99999


if __name__ == "__main__":
    jour = Cours.coursdujour()
    msg = Cours.format(jour)
    schedule.every().second.do(lambda: journee(msg))
    Thread(target=schedule_checker).start()  # Lance la boucle
