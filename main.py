import telegram_send
import schedule
from threading import Thread
from time import sleep
from cours import Cours


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(300)


def function_to_run(heure, msge):
    telegram_send.send(messages=[msge])
    schedule.clear(heure)


def journee():
    jour = Cours.coursdujour()
    msg = Cours.format(jour)
    for i in range(len(msg)):
        heure = msg[i][0]
        msge = msg[i][1]
        schedule.every().day.at(heure).do(lambda: function_to_run(heure, msge)).tag(heure)


if __name__ == "__main__":
    schedule.every().day.at('00:20').do(lambda: journee())
    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start()
    # And then of course, start your server.
    #uvicorn.run("example:app",host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
