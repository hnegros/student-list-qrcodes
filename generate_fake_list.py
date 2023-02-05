import csv

from faker import Faker


fake = Faker(locale="fr-FR")
l = [["Prénom","Nom","Classe"]]

for _ in range(20):
    e=[]
    e.append(fake.first_name())
    e.append(fake.last_name())
    e.append(f'{fake.random_element(["1ere","2nde","Term"])}{fake.random_int(min=1,max=4)}')
    l.append(e)

with open("fake_student_list.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(l)
