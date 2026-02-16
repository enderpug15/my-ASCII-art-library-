from colorama import Fore, Style, init
init()
print(Fore.GREEN + "Welcome to my ASCII art library! This contains every single ASCII art I have made and just ASCII art in general. Currently I have the CTS logo, a blueberry. settings text, the Blueberry for CTS settings, Raspberry Pi raspberry, a cat, an exclamation mark, small smiley face, smiley face, a cat, basic ASCII faces, and more!")
print("This program partially utilizes my terminal system CTS." + Style.RESET_ALL)
Greeting = """ 
 __      __  ___                                   ___
 \ \    / /__| |__ ___ _ __  ___   _  _ ___ ___ _ _| |
  \ \/\/ / -_) / _/ _ \ '  \/ -_) | || (_-</ -_) '_|_|
   \_/\_/\___|_\__\___/_|_|_\___|  \_,_/__/\___|_| (_)
                                                      """
print(Fore.RED + Greeting + Style.RESET_ALL)
print("All art is free to use. If you want to use any of these pieces of art, you can! Just give me credit if you use it in a project. I will be adding more art in the future, so check back often!")
logo = """
  _______ _________ _____
 /  _____|___   ___/  ___|  
 | |         | |   | (___
 | |         | |   \____ \   
 | |_____    | |    ____) |
 \_______|   |_|   |_____/ 
  COMPUTE  TERMINAL SYSTEM  
  """   
print(Fore.GREEN + logo + Style.RESET_ALL)
print("This is the CTS logo. Art piece number 1.")
# Leaves (green)
print(Fore.GREEN + "                  .;;,                ")
print("                  ;cccl         .;,")
print("                   :cccl      ;oood")
print("                    ;cccl.  .ooood")
print("                     :cccl;looo:" + Style.RESET_ALL)

# Bottom part of blueberry (blue)
print(Fore.BLUE + "                    .;;;;;;;;;;;.  ")
print("                   ;;;;;;:::::::::   ")
print("                  .;;;;;;;;;;;;::..   ")
print("                  :::::::;;;;;;;;;:   ")
print("                   .;;;;;;;;;::::.     ")
print("                    ,::::;;;;;;;,    ")
print("                      ;:::::::;      " + Style.RESET_ALL)
print("This is the blueberry ASCII art. The icon for Compute terminal system (Developed by me).This Blueberry will be replaced at V1.0.0. Every major update the Blueberry is updated. Art piece number 2.")

 
print(Fore.GREEN +"               ___      _   _   _ ")            
print("              / __| ___| |_| |_(_)_ _  __ _ ___ ")
print("              \__ \/ -_)  _|  _| | ' \/ _` (_-< ")
print("              |___/\___|\__|\__|_|_||_\__, /__/ ")
print("                                      |___/     "+ Style.RESET_ALL)
print("This is the settings ASCII art logo. Art piece number 3.")

print(Fore.GREEN + Style.RESET_ALL) 
print(Fore.LIGHTGREEN_EX+ "                 .;;,                ")
print("                  ;cccl        .;,")
print("                   :cccl      ;oood")
print("                    ;cccl.  .ooood")
print("                     :cccl;looo:" + Style.RESET_ALL)

print(Fore.LIGHTBLUE_EX + "                    .,,,::::::,,.  ")
print("                   ....;;;;;;;....   ")
print("                  ...;;       ;;...   ")
print("                  ,,,;;       ;;,,,   ")
print("                   ,,;;       ;;,,     ")
print("                    ,..;;;;;;;..,    ")
print("                      ;.......;      " + Style.RESET_ALL)
print("Isnt much about this. Its the similar to the first blueberry but without the center. Art piece number 4")

print(Fore.GREEN + " /\_/\ ")
print("( -.- ) ")
print("(_)~(_) " + Style.RESET_ALL)
print("This is the cat. The cat is sleeping :) Art piece number 5.")

print("This is the Raspberry Pi raspberry. Art piece number 6.")

print(Fore.RED + "___")
print("| |")
print("| |")
print("|_|")
print("(_)" + Style.RESET_ALL)
print("This is that exclamation mark. Art piece number 7.")

print(Fore.GREEN + " 0 0 ")
print("\___/" + Style.RESET_ALL)
print("This is a small smiley face. Art piece number 8.")
print(Fore.LIGHTGREEN_EX + "    ___               ___ ")
print("   /III\             /III\ ")
print("  |IIIII|           |IIIII| ")
print("   \III/             \III/ ")
print("")
print("")
print(" III                     III ")                      
print("   III                 III")
print("      III           III ")
print("         IIIIIIIIIII " + Style.RESET_ALL)
print("This is a smiley face. Art piece number 9.")

print(Fore.LIGHTWHITE_EX + "   ^    ^  ")
print("(   • , •  )")
print("_(       )")
print("  _-----_" + Style.RESET_ALL)
print("This is another cat. Made by one of my friends. Art piece number 10.")

print

print("Section 2: Basic artwork. example: :) ")

print(":)")
print("Smiley face basic. Art piece number 11.")

print(" :(")
print("Sad face basic. Art piece number 12.") 

print(":D")
print("Big smiley face basic. Art piece number 13.")

print(":P")
print("Tongue out smiley face basic. Art piece number 14.")

print("8(")
print("Sad face with glasses basic. Art piece number 15.")

print(" 8)")
print("Smiley face with glasses basic. Art piece number 16.")

print(" ;) ")
print("Winking smiley face basic. Art piece number 17.")

print(" :O ")
print("Surprised face basic. Art piece number 18.")

print(" :/ ")
print("Confused face basic. Art piece number 19.")

print(":3") 
print("Cat face basic. Art piece number 20.")

print("-_-")
print("Unamused face. Contributed by my friend. Art piece number 21.")

print("O-Ö")
print("Oh! face. Contributed by my friend. Art piece number 22.")


print("End of library! All commands you can use: exit, 5 (to exit library), socials (to see my socials), and credits (to see credits). Type 'help' for more info on commands.")


while True: 
    command = input(Fore.GREEN + "\nCTS > " + Style.RESET_ALL).lower()

    if command == "exit":
        print("Thanks for visiting my ASCII art library :) Goodbye user! Type 5 to exit library")
    elif command == "5":
      break

    elif command == "socials":
        print("You can find me on Github at https://github.com/enderpug15 sorry thats all my socials for now :)")

    elif command == "credits":
        print("Credits: Italy (me) and my friend who contributed some of her art to this library.")


