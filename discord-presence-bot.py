from pypresence import Presence
import time
import os
import os.path
import traceback

rpc = Presence("1097539948648878223")

def getfromconfig(config_path, string):
    with open("configs/" + config_path) as f:
        for line in f:
            line2 = line.replace("\n", "").split("=")
            if(line2[0] == string):
                return line2[1]

def setdefaultconfig():
    config = input("Enter the config name -> ")
    f = open("configs/config.yml", "w")
    if(configexists(config) or config == "none"):
        f.write("def_config=" + config)
        print("Set default config to " + config)
    else:
        print("Config does not exist.")

def configexists(config_name):
    if(os.path.exists("configs/" + config_name + ".txt")):
        return True
    else:
        return False

def createconfig():
    name = input("Enter config name -> ")
    firstline = input("Input the first line of your rich presence ->")
    secondline = input("Input the second line of your rich presence ->")
    if not os.path.exists("configs"):
        os.makedirs("configs")
    try:
        f = open("configs/" + name + ".txt", "w")
        f.write("firstline=" + firstline + "\nsecondline="+ secondline +"")
        f.close()
        prompt = input("Want to add some buttons (y/n) -> ")
        f = open("configs/" + name + ".txt", "a")
        if(prompt == "y"):
            button_label = input("Enter the text of your button -> ")
            button_url = input("Enter the URL of your button -> ")
            prompt = input("Want to create another button? (y/n) -> ")
            if(button_url and button_label == ""):
                print("The values cannot be empty! Please retry!")
                return
            if(not button_url.startswith("http")):
                button_url = "http://" + button_url
            f.write("\nbutton_1=1\nbutton_1_label=" + button_label +"\nbutton_1_url=" + button_url + "")
            if(prompt == "y"):
                button_label = input("Enter the text of your button -> ")
                button_url = input("Enter the URL of your button -> ")
                if(not button_url.startswith("http")):
                    button_url = "http://" + button_url
                if(button_url == "" or button_label == "" or button_url == None or button_label == None):
                    print("The values cannot be empty! Please retry!")
                    return
                f.write("\nbutton_2=1\nbutton_2_label=" + button_label +"\nbutton_2_url=" + button_url + "")
            else:
                f.write("\nbutton_2=0")

        else:
            f.write("\nbutton_1=0\nbutton_2=0")
        f.close()
        print("Config created!")
    except:
        print("An error occured. Please confirm that all the values are given and in correct form.")

def loadconfig(config_name):
    try:
        rpc.clear()
    except:
        None
    try:
        firstline = getfromconfig(config_name + ".txt", "firstline")
        secondline = getfromconfig(config_name + ".txt", "secondline")
        button_1 = getfromconfig(config_name + ".txt", "button_1")
        button_1_label = getfromconfig(config_name + ".txt", "button_1_label")
        button_1_url = getfromconfig(config_name + ".txt", "button_1_url")
        button_2 = getfromconfig(config_name + ".txt", "button_2")
        button_2_label = getfromconfig(config_name + ".txt", "button_2_label")
        button_2_url = getfromconfig(config_name + ".txt", "button_2_url")

        print("Config " + config_name + " loaded.")
        rpc.connect()
        if(button_1 == "1" and button_2 == "1"):
            rpc.update(
                state=secondline,
                    details=firstline,
                    large_image="mein_projekt", 
                    start=time.time(),
                    large_text="Discord Rich Presence Customizer by Brusky", 
                    small_image="download", 
                    small_text="Get the feature at brusky.net/rich-presence", 
                buttons=[{"label": button_1_label, "url": button_1_url}, {"label": button_2_label, "url": button_2_url}]
            )
        elif(button_1 == "1"):
            rpc.update(
                state=secondline,
                    details=firstline,
                    large_image="mein_projekt", 
                    start=time.time(),
                    large_text="Discord Rich Presence Customizer by Brusky", 
                    small_image="download", 
                    small_text="Get the feature at brusky.net/rich-presence", 
                buttons=[{"label": button_1_label, "url": button_1_url}]
            )
        elif(button_2 == "1"):
            rpc.update(
                state=secondline,
                    details=firstline,
                    large_image="mein_projekt", 
                    start=time.time(),
                    large_text="Discord Rich Presence Customizer by Brusky", 
                    small_image="download", 
                    small_text="Get the feature at brusky.net/rich-presence", 
            buttons=[{"label": button_2_label, "url": button_2_url}]
        )
        print("Connected to Discord.")
    except:
        print("There was an error loading this config. Please try again. If the error keeps occuring, please create an issue on GitHub")

def commandinput():
    exit = False
    command = input(">> ")
    match command:
        case "createconfig":
            createconfig()
        case "loadconfig":
            configname = input("Config name (just the name, without any addons) -> ")
            loadconfig(configname)
        case "defaultconfig":
            setdefaultconfig()
        case "stop":
            rpc.close()
            print("Disconnected from Discord.")
        case "commands":
            print("createconfig - creates a configuration file\nloadconfig - loades a configuration file\ndefaultconfig - applies a default config, which is loaded, when you start the program\nstop - Cancels the connection to discord.\nexit - Exit the program")
        case "exit":
            exit = True
        case "clear":
            os.system("cls")
        case __:
            print("Unknown command. Type commands for a list of commands")
    if(not exit):
        commandinput()
if(os.path.exists("configs/config.yml")):
    with open("configs/config.yml") as f:
            for line in f:
                split = line.replace("\n", "").split("=")
                if(split[0] == "def_config" and split[1] != "none"):
                    loadconfig(split[1])
commandinput()