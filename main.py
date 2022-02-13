#Blackjack
#Man bekommt am Anfang Karten und Der BOT auch
#Wenn man über 21 kommt ist vorbei 
#Man kann ziehen oder halten
from inspect import currentframe
import random
from os import system, name
import time
from tracemalloc import reset_peak

from Savefile import *
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')

def normalModus():
    global Guthaben
    clear()
    eigeneZahl = str(random.randint(1,6))
    gegnerZahl = str(random.randint(1,6))
    print("Hier, du hast noch " + str(Guthaben) + " Münzen zum spielen")
    print("Wie viel möchtest du Wetten?")
    wette = input("\n ")
    clear()
    if wette.isdigit():
        if int(wette) >= 0 and Guthaben >= int(wette):
            Guthaben = Guthaben-int(wette)
            print("Dein Guthaben: " + str(Guthaben))
            time.sleep(.5)
            print("\nDer Gegner würfelt eine " + gegnerZahl)
            time.sleep(.5)
            print("Du hast eine " + eigeneZahl + " gewürfelt\n")
            time.sleep(.5)
            if gegnerZahl > eigeneZahl:
                Guthaben = Guthaben
                print("Der Gegner hatte eine höhere Zahl und du hast dein Einsatz verloren.")
                print("\nDein neues Guthaben beträgt: " + str(Guthaben))
                save()
                time.sleep(1)
                menu()
            elif gegnerZahl==eigeneZahl:
                Guthaben = Guthaben+int(wette)
                print("Ihr habt die gleiche Zahl, du verlierst nichts.")
                print("\nDein neues Guthaben beträgt: " + str(Guthaben))
                save()
                goBack = input("\nPress Enter to get back to the Menu")
                menu()
            elif gegnerZahl < eigeneZahl:
                Guthaben = Guthaben+int(wette)*2
                print("Du hast die höhere Zahl und bekommst 2x dein Wetteinsatz.")
                print("\nDein neues Guthaben beträgt: " + str(Guthaben))
                save()
                goBack = input("\nPress Enter to get back to the Menu")
                menu()
        else:
            print("Bitte gib eine korrekte Zahl an! (ACHTE AUF DEIN GUTHABEN!)")

def riskyModus():
    global Guthaben
    clear()
    eigeneZahl = str(random.randint(1,6))
    gegnerZahl = str(random.randint(1,6))
    print("Hier, du hast noch " + str(Guthaben) + " Münzen zum spielen")
    print("Wie viel möchtest du Wetten?")
    wette = input("\n ")
    clear()
    if wette.isdigit():
        if int(wette) >= 0 and Guthaben >= int(wette):
            Guthaben = Guthaben-int(wette)
            print("Dein Guthaben: " + str(Guthaben))
            time.sleep(.5)
            print("\nDer Gegner würfelt eine " + gegnerZahl)
            time.sleep(.5)
            print("Du hast eine " + eigeneZahl + " gewürfelt\n")
            time.sleep(.5)
            if gegnerZahl > eigeneZahl:
                Guthaben = Guthaben-int(wette)*5
                print("Der Gegner hatte eine höhere Zahl und du hast dein Einsatz 5x verloren.")
                print("\nDein neues Guthaben beträgt: " + str(Guthaben))
                save()
                goBack = input("\nPress Enter to get back to the Menu")
                menu()
            elif gegnerZahl==eigeneZahl:
                Guthaben = Guthaben+int(wette)
                print("Ihr habt die gleiche Zahl, du verlierst nichts.")
                print("\nDein neues Guthaben beträgt: " + str(Guthaben))
                save()
                goBack = input("\nPress Enter to get back to the Menu")
                menu()
            elif gegnerZahl < eigeneZahl:
                Guthaben = Guthaben+int(wette)*5
                print("Du hast die höhere Zahl und bekommst 5x dein Wetteinsatz.")
                print("\nDein neues Guthaben beträgt: " + str(Guthaben))
                save()
                goBack = input("\nPress Enter to get back to the Menu")
                menu()

        else:
            print("Bitte gib eine korrekte Zahl an! (ACHTE AUF DEIN GUTHABEN!)")

def rang():
    global Guthaben
    clear()
    if Guthaben >= 0 and Guthaben < 2500:
        currentRang = "Silber"
    elif Guthaben >= 2500 and Guthaben < 10000:
        currentRang = "Gold"
    elif Guthaben >= 10000 and Guthaben < 25000:
        currentRang = "Diamant"
    elif Guthaben >= 25000:
        currentRang = "Dr. Prof. Waibli"
    print("Dein aktueller Rang: " + currentRang)
    print("Aktuelles Guthaben: " + str(Guthaben))

    print("\nRangtabelle: ")
    print("0-2.500                Silber")
    print("  2.500-10.000         Gold")
    print("        10.000-25.000  Diamant")
    print("               25.000+ Dr. Prof. Waibli")
    goBack = input("\nPress Enter to get back to the Menu")
    menu()

def reset():
    global Guthaben
    clear()
    print("Bist du dich sicher, dass du dein Guthaben reseten willst, du kannst es danach nicht mehr rückgängig machen!\nTipp: Dieses Feature befreit dich von einem negativen Guthaben!")
    resetConfirm = input("Ja / Nein\n\n")
    if resetConfirm.upper() == "NEIN":
        print("Guthaben NICHT resetet!")
        time.sleep(1)
        menu()
    elif resetConfirm.upper() =="JA":
        f = open("Python\Blackjack\Savefile.py", "w")
        f.write("Guthaben = " + "1000")
        f.close()
        print("Spielstand resetet")
        print("Dein Guthaben wurde ERFOLGREICH resetet! (NEUSTART ERFORDERLICH!)")
        time.sleep(2)

def hilfe():
    clear()
    print("Wenn du das Spiel nicht verstehst, hast du einen IQ unter 5")


def save():
    f = open("Python\Blackjack\Savefile.py", "w")
    f.write("Guthaben = " + str(Guthaben))
    f.close()
    print("Spielstand gespeichert")


def menu():
    clear()
    print("****************************************************************")
    print("* Copyright of Noah, 2022                                      *")
    print("*                                                              *")
    print("* https://www.youtube.com/watch?v=dQw4w9WgXcQ                  *")
    print("****************************************************************") 
    print("\n[1] Normal(2x) ; [2] Risky(5x) ; [3] Rang ; [4] Reset ; [5] Hilfe")
    auswahl = input()
    if auswahl == "1":
        normalModus()
    elif auswahl == "2":
        riskyModus()
    elif auswahl == "3":
        rang()
    elif auswahl == "4":
        reset()
    elif auswahl == "5":
        hilfe()
menu()