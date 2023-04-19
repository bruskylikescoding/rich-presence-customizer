from pypresence import Presence
import time
import os

globalrpc = None

if not os.path.exists("configs"):
   os.mkdir("configs")
def saveinconfig(config_path, string, value):
    lines = []
    added = False
    if(not os.path.exists("configs/" + config_path)):
        f = open("configs/" + config_path, "x")
        f.close()
    with open("configs/" + config_path) as f:
        for line in f:
            if(line.startswith(string)):
                lines.append(string + "=" + value + "\n")
                added = True
            else:
                lines.append(line)
        if not added:
                lines.append(string + "=" + value + "\n")
    
    f = open("configs/" + config_path, "w")
    f.writelines(lines)
    f.close()

def deleteconfig(config_name):
    if(configexists(config_name)):
        os.remove("configs/" + config_name + ".txt")

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
    deleteconfig(name)
    saveinconfig(name + ".txt", "name", name)
    mode = input("Enter the mode (default, custom [Custom allows you to use custom Discord Application. You need a Application ID. Please see the docs for more information.]) -> ")
    saveinconfig(name + ".txt", "mode", mode)
    if(mode == "custom"):
        saveinconfig(name + ".txt", "id", input("Enter the Application ID -> "))
        saveinconfig(name + ".txt", "big_image", input("Enter the name of the attachment, which shell be used for the big image -> "))
        saveinconfig(name + ".txt", "small_image", input("Enter the name of the attachment, which shell be used for the small image -> "))
    
    saveinconfig(name + ".txt", "firstline", input("Input the first line of your rich presence ->"))
    saveinconfig(name + ".txt", "secondline", input("Input the second line of your rich presence ->"))
    if not os.path.exists("configs"):
        os.makedirs("configs")
    try:
        prompt = input("Want to add some buttons (y/n) -> ")
        if(prompt == "y"):
            button_label = input("Enter the text of your button -> ")
            button_url = input("Enter the URL of your button -> ")
            prompt = input("Want to create another button? (y/n) -> ")
            if(button_url and button_label == ""):
                print("The values cannot be empty! Please retry!")
                return
            if(not button_url.startswith("http")):
                button_url = "http://" + button_url
            saveinconfig(name + ".txt", "button_1", "1")
            saveinconfig(name + ".txt", "button_1_label", button_label)
            saveinconfig(name + ".txt", "button_1_url", button_url)
            if(prompt == "y"):
                button_label = input("Enter the text of your button -> ")
                button_url = input("Enter the URL of your button -> ")
                if(not button_url.startswith("http")):
                    button_url = "http://" + button_url
                if(button_url == "" or button_label == "" or button_url == None or button_label == None):
                    print("The values cannot be empty! Please retry!")
                    return
                saveinconfig(name + ".txt", "button_2", "1")
                saveinconfig(name + ".txt", "button_2_label", button_label)
                saveinconfig(name + ".txt", "button_2_url", button_url)
            else:
                saveinconfig(name + ".txt", "button_2", "0")

        else:
            saveinconfig(name + ".txt", "button_1", "0")
            saveinconfig(name + ".txt", "button_2", "0")
        print("Config created!")
    except Exception as e:
        print(e)
        print("An error occured. Please confirm that all the values are given and in correct form.")

def loadconfig(config_name):
    global globalrpc
    if(not globalrpc == None):
        Presence.clear(globalrpc)
        Presence.close(globalrpc)
    
    mode = getfromconfig(config_name + ".txt", "mode")
    big_image = ""
    small_image = ""
    try:
        match mode:
            case "default":
                rpc = Presence("1097553838841536512")
                big_image = "big"
                small_image = "small"
            case "custom":
                rpc = Presence(str(getfromconfig(config_name + ".txt", "id")))
                big_image = getfromconfig(config_name + ".txt","big_image")
                small_image = getfromconfig(config_name + ".txt","small_image")
                if(big_image == ""):
                    big_image = "gommemode"
                if(small_image == ""):
                    small_image = "gommemode"
            case __:
                print("There is no use mode set for this config. Using default mode.")
                rpc = Presence("1097553838841536512")
    except:
        print("An error occured. Possible reasons:\n-> Discord is not started or not installed\n-> The application ID is invalid (only if the mode custom is enabled.)\n--> If the error keeps existing please create an issue on GitHub")
        return
    
    globalrpc = rpc
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
                    large_image=big_image, 
                    start=time.time(),
                    large_text="Discord Rich Presence Customizer by Brusky", 
                    small_image=small_image, 
                    small_text="Get the feature at brusky.net/rich-presence", 
                buttons=[{"label": button_1_label, "url": button_1_url}, {"label": button_2_label, "url": button_2_url}]
            )
        elif(button_1 == "1"):
            rpc.update(
                state=secondline,
                    details=firstline,
                    large_image=big_image, 
                    start=time.time(),
                    large_text="Discord Rich Presence Customizer by Brusky", 
                    small_image=small_image, 
                    small_text="Get the feature at brusky.net/rich-presence", 
                buttons=[{"label": button_1_label, "url": button_1_url}]
            )
        elif(button_2 == "1"):
            rpc.update(
                state=secondline,
                    details=firstline,
                    large_image=big_image, 
                    start=time.time(),
                    large_text="Discord Rich Presence Customizer by Brusky", 
                    small_image=small_image, 
                    small_text="Get the feature at brusky.net/rich-presence", 
            buttons=[{"label": button_2_label, "url": button_2_url}]
        )
        else:
           rpc.update(
                state=secondline,
                    details=firstline,
                    large_image=big_image, 
                    start=time.time(),
                    large_text="Discord Rich Presence Customizer by Brusky", 
                    small_image=small_image, 
                    small_text="Get the feature at brusky.net/rich-presence"
        ) 
        print("Connected to Discord.")
        return rpc
    except Exception as e:
        print(e)
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
    if(getfromconfig("config.yml", "def_config") != "none"):
        loadconfig(getfromconfig("config.yml", "def_config"))
commandinput()