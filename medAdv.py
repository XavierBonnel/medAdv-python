from termcolor import cprint, colored 
from pyfiglet import figlet_format, Figlet

# f = Figlet(font="slant")
# print(f.renderText("Kevin Medieval Adventure's"))
cprint(figlet_format("Medieval Adventures", font ="slant"), "red", attrs=["bold"])

print ("""           
|          .-----.     |
| \ ' /   _/    )/     |
|- ( ) -('---''--).    |
| / . \((()\^_^/)().   |
|  \\_\ (()_)-((()().  |
|   '- \ )/\._./(().   |
|     '/\/( X   ) \    |
|     (___)|___/ ) \.  |
|          |.#_|(___). |
|         /\    \ ( (_ |
|         \/\/\/\) \\. |
|         | / \ |.     |
|         |(   \|.     |
|        _|_)__|_\_.   |
|        )...()...(.   |
|         | (   \ |    |
|      .-'__,)  (  \.  |
|            '\_-,     |
             mrf""")

name=input("\n \n What is your name adventurer? \n")
print("\nWelcome to this wonderful journey " + name + "\n" )
print("where do you want to go?" + "\n" )
print("1. the dark forest of the elves? ")
print("2. the cosey mines of the dwarves? ")

first_choice=input("choose: ")

if first_choice is "1":
    print ('''
     | ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^  |
     |/|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\ |
     |/|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\ |
     ||/|\/|\/|\ /|\  |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\ |
      ejm96
    ''')
    print("\nYou enter a dark mysterious and ancient forest, you ear the wind and a distant song, probably a sad one\n")

    print("What do you do?\n")
    print("1.You walked toward the voice")
    print("2.You run in the opposite direction\n")

    second_choice=input("choose:")

    if second_choice is "1":
        print (''' \n|:____|\_________b___/______.____.__|__________._______.---.__.____________:|
 |:____|/__4____|.____$______|____|__|__________|\__-,__|___|__|\_______..__:|
 |:___/|___4____'`____/______|____|__|__________|___/___|___|__|\___""______:|
 |:__('|)___________________@|___(|__|__#( )___@|._____@|__@|_@|____________:|
      "|                              mp                                    /\n''')
        print("You approach an old elve. He tells you about his youth as a great warrior in the century war he participates against the orks to protect the forest of his ancestors\n")
    elif second_choice is "2":
        print ('''                 
|                 ^                  |
|                / \                 |
|           ^   _|.|_   ^            |
|         _|I|  |I .|  |.|_          |
|         \II||~~| |~~||  /          |
|          ~\~|~~~~~~~|~/~           |
|             \|II I ..|/            |
|        /\    |II.    |    /\.      |
|       /  \  _|III .  |_  /  \.     |
|       |-~| /(|I.I I  |)\ |~-|.     |
|     _/(I | +-----------+ |. )\_.   |
|     \~-----/____-~-____\-----~/.   |
|      |I.III|  /(===)\  |  .. |.    |
|      /~~~-----_________---~~~\.    |
|     `##########!\-#####%!!!!!| |\. |
|    _/###########!!\~~-_##%!!!\_/|. |
|    \##############!!!!!/~~-_%!!!!\ |
|     ~)#################!!!!!/~~--\_|
|  __ /#####################%%!!!!/ /|
|  \,~\-_____##############%%%!!!!\/ |
|  /!!!!\ \ \~-_###########%%%!!!!\  |
| /#####!!!!!!!\~-_#######%%%!!!!!!\_|
|/#############!!!\#########%%%!!!!!!|\\n''')
        print("\nyou ran through the woods pass a hill and you see a magnificent castle beneath you")
    # print("please choose 1 or 2 adventurer")
    else:
      print("please choose 1 or 2 adventurer")




elif first_choice is "2":
    print('''               
|                      _                                                      |
|                     /#\                                                     |
|                    /###\     /\                                             |
|                   /  ###\   /##\  /\                                        |
|                  /      #\ /####\/##\                                       |
|                 /  /      /   # /  ##\             _       /\               |
|               // //  /\  /    _/  /  #\ _         /#\    _/##\    /\.       |
|              // /   /  \     /   /    #\ \      _/###\_ /   ##\__/ _\.      |
|             /  \   / .. \   / /   _   { \ \   _/       / //    /    \\.     |
|     /\     /    /\  ...  \_/   / / \   } \ | /  /\  \ /  _    /  /    \ /\. |
|  _ /  \  /// / .\  ..%:.  /... /\ . \ {:  \\   /. \     / \  /   ___   /  \ |
| /.\ .\.\// \/... \.::::..... _/..\ ..\:|:. .  / .. \\  /.. \    /...\ /  \ \|
|/...\.../..:.\. ..:::::::..:..... . ...\{:... / %... \\/..%. \  /./:..\__   \|
| .:..\:..:::....:::;;;;;;::::::::.:::::.\}.....::%.:. \ .:::. \/.%:::.:..\.  |
|::::...:::;;:::::;;;;;;;;;;;;;;:::::;;::{:::::::;;;:..  .:;:... ::;;::::..   |
|;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;];;;;;;;;;;::::::;;;;:.::;;;;;;;;:..|
|;;;;;;;;;;;;;;ii;;;;;;;;;;;;;;;;;;;;;;;;[;;;;;;;;;;;;;;;;;;;;;;:;;;;;;;;;;;;;|
|;;;;;;;;;;;;;;;;;;;iiiiiiii;;;;;;;;;;;;;;};;ii;;iiii;;;;i;;;;;;;;;;;;;;;ii;;;|
|iiii;;;iiiiiiiiiiIIIIIIIIIIIiiiiiIiiiiii{iiIIiiiiiiiiiiiiiiii;;;;;iiiilliiiii|
|IIIiiIIllllllIIlllIIIIlllIIIlIiiIIIIIIIIIIIIlIIIIIllIIIIIIIIiiiiiiiillIIIllII|
|IIIiiilIIIIIIIllTIIIIllIIlIlIIITTTTlIlIlIIIlIITTTTTTTIIIIlIIllIlIlllIIIIIIITT|
|IIIIilIIIIITTTTTTTIIIIIIIIIIIIITTTTTIIIIIIIIITTTTTTTTTTIIIIIIIIIlIIIIIIIITTTT|
|IIIIIIIIITTTTTTTTTTTTTIIIIIIIITTTTTTTTIIIIIITTTTTTTTTTTTTTIIIIIIIIIIIIIITTTTT|''')
    print("\nThe mines seems desert at first sight but you can see a comfy fire far away")

    

    print("What do you do?\n")
    print("1. You run toward the fire, and the more you approaches the more the atmosphere is strange.")
    print("2. You take your sword and walk carefully in a corridor.\n")

    third_choice=input("choose:")
    if third_choice is "1":
      print('''
|                  '                                      |
|                  )                    `                 |
|                 /(l                   /)                |
|                (  \                  / (                |
|                ) * )                ( , )               |
|                 \#/                  \#'                |
|               .-"#'-.             .-"#"=,               |
|            (  |"-.='|            '|"-,-"|               |
|            )\ |     |  ,        /(|     | /(         ,  |
|   (       /  )|     | (\       (  \     | ) )       ((. |
|   )\     (   (|     | ) )      ) , )    |/ (        ) \ |
|  /  )     ) . )     |/  (     ( # (     ( , )      /   )|
| ( * (      \#/|     (`# )      `#/|     |`#/      (  '( |
|  \#/     .-"#'-.   .-"#'-,   .-"#'-.   .-=#"-;     `#/. |
|.-"#'-.   |"=,-"|   |"-.-"|)  1"-.-"|   |"-.-"|   ,-"#"-.|
||"-.-"|   |  !  |   |     |   |     |   |     !   |"-.-"||
||     |   |     |._,|     |   |     |._,|     a   |     ||
||     |   |     |   |     |   |     |   |     p   |     ||
||     |   |     |   |     |   |     |   |     x   |     ||
|'-._,-'   '-._,-'   '-._,-'   '-._,-'   '-._,-"   '-._,-'|
      \n''')
      print("Finally, you met a group of happy dwarves smoking a lot debatting on how to get more gold out of the mountains. You share a beer with them and they invited you to the city underneath a kilometer away.")

    if third_choice is "2":
      print ('''
_____________________________________________
|.'',                                     ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',                             ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.|                         |.'.'.'.'.|
|.'.'.'.'.|===;                 ;===|.'.'.'.'.|
|.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
|.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|,',',',',|---|',|'|???????|'|,'|---|,',',',',|
|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
|.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\         ','.'.|
|.','          /%%%%%%%%%%%%%%%\          ','.|
|;____________/%%%%%Spicer%%%%%%\____________;|
      \n''')
      print ('Soon the corridor is showing you a lot of choices good... and probably bad.')

else:
    print("please choose 1 or 2 adventurer")

cprint(figlet_format("To be continued...", font ="slant"), "blue", attrs=["bold"])
