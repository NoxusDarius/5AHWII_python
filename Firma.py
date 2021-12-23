
class Person:
    def __init__(self, firstname, lastname, age, isMale):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.isMale = isMale


class Mitarbeiter(Person):
    def __init__(self, firstname, lastname, age, gender, salary):
        super().__init__(firstname, lastname, age, gender)
        self.salray = salary


class Gruppenleiter(Person):
    def __init__(self, firstname, lastname, age, gender):
        super().__init__(firstname, lastname, age, gender)


class Abteilung:
    def __init__(self, name):
        self.name = name
    leiter = Gruppenleiter("", "", 0, True)
    arbeiter = []


class Company:
    abteilungen = []


m1 = Mitarbeiter("ALexander", "Bertoni", 18, True, 1800)
m2 = Mitarbeiter("Anna", "Tipotsch", 18, False, 2400)
g1 = Gruppenleiter("Noah", "Grobbel", 18, True)
a1 = Abteilung("Produktion")
a1.leiter = g1
a1.arbeiter.append([m1, m2])
c1 = Company()
c1.abteilungen.append([a1])


def count_mitarbeiter(com=Company()):
    count = 0
    for d in com.abteilungen:
        for e in d:
            for a in e.arbeiter:
                count += len(a)
    return count


def count_leiter(com=Company()):
    count = 0
    for d in com.abteilungen:
        for e in d:
            if e.leiter is not None:
                count += 1
    return count


def biggest_abteilung(com=Company()):
    count = 0
    bigCount = 0
    dep = None
    for d in com.abteilungen:
        for e in d:
            if e.leiter is not None:
                count += 1
            for a in e.arbeiter:
                count += len(a)
            if bigCount < count:
                bigCount = count
                dep = e
            count = 0
    return dep.name


def anteil_woman(com=Company()):
    ges = 0
    count = 0
    for d in com.abteilungen:
        for e in d:
            if e.leiter is not None:
                if e.leiter.isMale:
                    count += 1
                ges += 1
            for a in e.arbeiter:
                for b in a:
                    if not b.isMale:
                        count += 1
                    ges += 1
    return 100-(count / ges * 100)


print(count_mitarbeiter(c1))
print(count_leiter(c1))
print(biggest_abteilung(c1))
print(anteil_woman(c1), "%")
