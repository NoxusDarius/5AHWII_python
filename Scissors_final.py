import random
import os
import requests as requests
print("Scissor")
print("Rock")
print("Paper")
print("Lizard")
print("Spock")

result = os.path.abspath("Ergebnisse.txt")
print(result)
erg_file = result.replace("\\", "/")


print(erg_file)


def eingabe(values):
    while True:
        ein = input("Rock/Paper/Scissor/Lizard/Spock: ")
        if ein in values:
            return ein
        else:
            print("Falsche Eingabe")


def weiterspielen():
    while True:
        weiter = input("Möchten Sie gerne weiterspielen? [y/n]")
        if weiter == 'y':
            return True
        if weiter == 'n':
            print("Das Spiel wurde beendet")
            return False


def compare(player, computer, value, result):
    print("Spieler:" + player)
    print("Computer:" + computer)
    countuser[value[player]] = countuser[value[player]] + 1
    calc = value[player] - value[computer]
    return result[calc % 5]


def openfile():
    file = open(
        erg_file, 'r')
    d = {}
    for line in file:
        (key, val) = line.strip().split(',')
        d[key] = val
    file.close()
    return d


def writefile(dic_werte):
    file2 = open(erg_file, "w")
    for k, v in dic_werte.items():
        file2.writelines(k+","+str(v)+"\n")
    file2.close()


def dic_werte_andern(dic_werte):

    dic_werte["Draw"] = int(dic_werte["Draw"]) + countwerte[0]
    dic_werte["PlayerWon"] = int(dic_werte["PlayerWon"]) + countwerte[1]
    dic_werte["PlayerLost"] = int(dic_werte["PlayerLost"]) + countwerte[2]
    dic_werte["Paper"] = int(dic_werte["Paper"]) + countuser[2]
    dic_werte["Scissor"] = int(dic_werte["Scissor"]) + countuser[4]
    dic_werte["Rock"] = int(dic_werte["Rock"]) + countuser[0]
    dic_werte["Lizard"] = int(dic_werte["Lizard"]) + countuser[3]
    dic_werte["Spock"] = int(dic_werte["Spock"]) + countuser[1]

    return dic_werte


def count(ergebnis, result):
    if ergebnis is result[0]:
        countwerte[0] = countwerte[0] + 1
    elif ergebnis is result[1]:
        countwerte[1] = countwerte[1] + 1
    elif ergebnis is result[3]:
        countwerte[2] = countwerte[2] + 1
    else:
        print("Es wurde ein Falsches Ergebnis zurückgeliefert")


def countuser(user):
    pass


# erster Wert = Draw, zweiter Wert = Player, dritter Wert = Computer
countwerte = [0, 0, 0]
countuser = [0, 0, 0, 0, 0]  # erster Wert Rock, Spock, Paper, Lizard,Scissor
state = True
while state:
    if state == 1:

        values = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        comparevalues = {"Scissor": 4, "Rock": 0,
                         "Paper": 2, "Lizard": 3, "Spock": 1}
        result = ["Draw", "Player won", "Player won",
                  "Player lost", "Player lost"]
        user = eingabe(values)
        # countuser(user)
        comuter = random.choice(values)
        ergebnis = compare(user, comuter, comparevalues, result)
        print(ergebnis)
        count(ergebnis, result)
        dic_file_werte = openfile()
        final_write = dic_werte_andern(dic_file_werte)

        state = weiterspielen()


writefile(final_write)


def api_aufruf(username, anz_scheren, anz_stein, anz_papier, anz_lizard, anz_spock, apiIP="http://127.0.0.1:5000"):
    url = apiIP + "/v1/updateRecord"
    url += "?username=" + str(username) + "&voteScissors=" + str(anz_scheren) + "&voteRock=" + str(anz_stein) + "&votePaper=" +\
           str(anz_papier) + "&voteSpock=" + str(anz_spock) + \
        "&voteLizard=" + str(anz_lizard)
    responseCode = 0
    try:
        response = requests.post(url, None)
        responseCode = response.status_code
    except:
        return 0
    return responseCode


api_aufruf("RimmlSebastian", final_write["Scissor"], final_write["Rock"], final_write["Paper"], final_write["lizard"],
           final_write["spock"])

os.startfile("Ergebnisse.txt")


# es werd in der eltern klasse ein object erzeugt auf dieses referenziert super()
# Was ist static
# Wie wird es in python verwendet
# ohne self statische Methode
