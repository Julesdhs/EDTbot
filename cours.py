from datetime import date


class Cours():

    @staticmethod
    # méthode qui retourne l'heure donnée moins 10 minutes dans le format particulier
    def heuremoins10(heure):
        min = int(heure[2:4])
        if min >= 10:
            min2 = min-10
            return(str.format("{}:{}", heure[0:2], min2))
        h2 = int(heure[0:2])-1
        min2 = '50'
        return(str.format("{}:{}", h2, min2))

    @staticmethod
    def coursdujour():  # méthode qui retourne les cours du jour
        today = date.today()

        d = today.strftime("%Y%m%d")

        with open('C:/Users/jules/Desktop/TXT/output.txt', 'r', encoding="utf8") as f:
            find = str.format("DTSTART:{}", d)
            data = f.readlines()
            k = 0
            day = []
            for i in range(data.__len__()):
                if data[i][0:16] == find:
                    k += 1
                    day.append([data[i], data[i+2], data[i+3]])

        return day

    def format(day):  # formate chaque cours du jour en couple (heure de rappel, contenu du message à envoyer)
        msg = []
        for cours in day:
            heure = cours[0][17:21]
            matiere = cours[1][8:-1]
            salle = cours[2][9:-1]
            msg.append([Cours.heuremoins10(heure), str.format(
                "Tu as {} en {} à {}", matiere, salle, heure)])

        return(msg)
