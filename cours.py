import datetime


class Cours():

    @ staticmethod
    def coursdujour():  # méthode qui retourne les cours du jour à partir du fichier output.txt qui est obtenu par requete http non traitée ici
        today = datetime.datetime.today()

        d = today.strftime("%Y%m%d")

        with open('output.txt', 'r', encoding="utf8") as f:
            find = str.format("DTSTART:{}", d)
            data = f.readlines()
            k = 0
            day = []
            for i in range(data.__len__()):
                if data[i][0:16] == find:
                    k += 1
                    day.append([data[i], data[i+2], data[i+3]])

        return day

    def format(day):  # formate chaque cours du jour en couple (heure de début, contenu du message à envoyer)
        msg = []
        for cours in day:
            heure = cours[0][17:21]
            matiere = cours[1][8:-1]
            salle = cours[2][9:-1]
            msg.append([heure, str.format(
                "Tu as {} en {} à {}h{}", matiere, salle, heure[0:2], heure[2:4])])

        return(msg)
