def main():
    import os
    import ctypes
    from ctypes import wintypes
    import time
    from colorama import init
    init()
    from colorama import Fore, Back, Style

    print("_____________________________________________________________________________________________________V 0.75b")
    print("Reakce bot - BS beta")
    print(Fore.RED+"! Pro funkčnost je potřeba naistalovat Pynput a Colorama [pip install pynput && pip install colorama]"+Style.RESET_ALL)
    print("------------------------------------------------------------------------------------------------------------")
    with open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r") as logfile:
        for line in logfile:
            if "[Reakce] Napis rychle" in line:
                words_in_line = line.split()
                print(words_in_line[0],"REAKCE > CHAT:",words_in_line[-1]);
            if "vyhral za" in line:
                slova_na_radku = line.split()
                
    cas = words_in_line[0];
    dohry = words_in_line[-1].replace("!", "")
    print("------------------------------------------------------------------------------------------------------------")

    import datetime

    def split(dohry): 
        return list(dohry)
    print("Délka listu: ",dohry.__len__())
    from pynput.keyboard import Key, Controller
    keyboard = Controller()

    currentDT = datetime.datetime.now()

    casted = (currentDT.strftime("%H%M%S"))
    casbefore0 = cas.replace(":", "")
    casbefore1 = casbefore0.replace("[", "")
    casbefore_final = casbefore1.replace("]", "")
    print("Poslední Reakce : "+cas+" > "+Fore.GREEN + dohry + Style.RESET_ALL + " s vítězem " + Fore.YELLOW + slova_na_radku[4] + Style.RESET_ALL + " v čase " + slova_na_radku[7])
    #print(casbefore_final+" "+casted)
    e = float(casbefore_final)
    f = float(casted)
    print("Další reakce v :",e+1102)
    if f <= e+4:
       keyboard.type(dohry)
       keyboard.press(Key.enter)
       time.sleep(0.2)
       keyboard.release(Key.enter)
       keyboard.press('t')
       time.sleep(0.2)
       keyboard.release('t')
    restart = "automaticky"
    if restart == "automaticky":
        time.sleep(1.5)
        main()
main()
