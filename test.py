from cours import Cours
import datetime
# print(Cours.heuremoins10('1830'))
# print(Cours.heuremoins10('0900'))
# print(Cours.heuremoins10('0945'))
#jour = Cours.coursdujour()
# print(jour)
# print(Cours.format(jour))

b = datetime.datetime.today()
print(b.minute)
# print(datem.hour)
d = b.strftime("%H%M")
print(d)
