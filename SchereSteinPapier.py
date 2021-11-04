import random
print("-------------------")
print("Schere")
print("Stein")
print("Papier")
print("-------------------")


def eingabe(check):
    wahl = input("Rock,Paper,Scissor: ")
    if wahl in check:
        return wahl
    else:
        print("Please enter an correct value")


def compare(player, computer, value, result):
    print("Player answer:" + player)
    print("Computer answer:" + computer)
    calc = value[player] - value[computer]
    return result[calc % 3]


def stop():
    while True:
        playforward = input("Play again [y/n]: ")
        if playforward == "y":
            return True
        elif playforward == "n":
            return False


state = True
while state:
    listuser = ["Rock", "Paper", "Scissor"]
    listcomputer = ["Rock", "Paper", "Scissor"]
    listvalues = {"Rock": 0, "Paper": 1, "Scissor": 2}
    result = ["Draw", "Player won", "Player lost"]
    answerUser = eingabe(listuser)
    answerComputer = random.choice(listcomputer)
    print(compare(answerUser, answerComputer, listvalues, result))
    print(answerComputer, answerUser, listvalues.get(answerComputer,
          "Not defined"), listvalues.get(answerUser, "Not defined"))
    state = stop()
