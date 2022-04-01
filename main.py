import schedule
from threading import Thread
from time import sleep
from cours import Cours
import requests
import datetime


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def telegram_bot_sendtext(bot_message):

    bot_token = '5290661767:AAEUSQuSgTDGMU8BNhLiRLyfl_ablX0-sFY'
    bot_chatID = '2108448564'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)


def journee(msg):
    now = datetime.datetime.today()
    d = now.strftime("%H%M")
    for i in range(len(msg)):
        print(msg[i][0], d, msg[i][0] == d)
        if msg[i][0] == d:
            telegram_bot_sendtext(msg[i][1])


if __name__ == "__main__":
    jour = Cours.coursdujour()
    msg = Cours.format(jour)
    schedule.every().minute.do(lambda: journee(msg))
    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start()
    # And then of course, start your server.
    # print(schedule.get_jobs())
    #uvicorn.run("example:app",host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
