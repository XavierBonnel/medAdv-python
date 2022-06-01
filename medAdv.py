from termcolor import cprint, colored 
from pyfiglet import figlet_format, Figlet

# f = Figlet(font="slant")
# print(f.renderText("Kevin Medieval Adventure's"))
cprint(figlet_format("Medieval Adventure's", font ="slant"), "red", attrs=["bold"])

print ("""           .-----.
 \ ' /   _/    )/
- ( ) -('---''--)
 / . \((()\^_^/)()
  \\_\ (()_)-((()()
   '- \ )/\._./(()
     '/\/( X   ) \
     (___)|___/ ) \
          |.#_|(___)
         /\    \ ( (_
         \/\/\/\) \\
         | / \ |
         |(   \|
        _|_)__|_\_
        )...()...(
         | (   \ |     
      .-'__,)  (  \
  mrf           '\_-,""")

name=input("\n \n What is your name adventurer? \n")
print("\nWelcome to this wonderful journey " + name + "\n" )
print("where do you want to go?" + "\n" )
print("1. the dark forest of the elves? ")
print("2. the cosey mines of the dwarves? ")

first_choice=input("choose: ")

if first_choice is "1":
    print ('''
       ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
      /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\
      /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\
ejm96 /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\
    ''')
    print("You enter a dark mysterious and ancient forest, you ear the wind and a distant song, probably a sad one\n")

    print("What do you do?\n")
    print("1.You walked toward the voice")
    print("2.You run in the opposite direction\n")

    second_choice=input("choose:")

    if second_choice is "1":
        print (''' |:____|\_________b___/______.____.__|__________._______.---.__.____________:|
 |:____|/__4____|.____$______|____|__|__________|\__-,__|___|__|\_______..__:|
 |:___/|___4____'`____/______|____|__|__________|___/___|___|__|\___""______:|
 |:__('|)___________________@|___(|__|__#( )___@|._____@|__@|_@|____________:|
      "|                              mp                                    /\n''')
      print("You approach an old elve. He tells you about his youth as a great warrior in the century war he participates against the orks to protect the forest of his ancestors")
    elif second_choice is "2":
        print ('''                  ^
                 / \
            ^   _|.|_   ^
          _|I|  |I .|  |.|_
          \II||~~| |~~||  /
           ~\~|~~~~~~~|~/~
             \|II I ..|/
        /\    |II.    |    /\
       /  \  _|III .  |_  /  \
       |-~| /(|I.I I  |)\ |~-|
     _/(I | +-----------+ |. )\_
     \~-----/____-~-____\-----~/
      |I.III|  /(===)\  |  .. |
      /~~~-----_________---~~~\
     `##########!\-#####%!!!!!| |\
    _/###########!!\~~-_##%!!!\_/|
    \##############!!!!!/~~-_%!!!!\
     ~)#################!!!!!/~~--\_
  __ /#####################%%!!!!/ /
  \,~\-_____##############%%%!!!!\/
  /!!!!\ \ \~-_###########%%%!!!!\
 /#####!!!!!!!\~-_#######%%%!!!!!!\_
/#############!!!\#########%%%!!!!!!\\n''')
        print("you ran through the woods pass a hill and you see a magnificent castle beneath you")



elif first_choice is "2":
    print('''                      _
                     /#\
                    /###\     /\
                   /  ###\   /##\  /\
                  /      #\ /####\/##\
                 /  /      /   # /  ##\             _       /\
               // //  /\  /    _/  /  #\ _         /#\    _/##\    /\
              // /   /  \     /   /    #\ \      _/###\_ /   ##\__/ _\
             /  \   / .. \   / /   _   { \ \   _/       / //    /    \\
     /\     /    /\  ...  \_/   / / \   } \ | /  /\  \ /  _    /  /    \ /\
  _ /  \  /// / .\  ..%:.  /... /\ . \ {:  \\   /. \     / \  /   ___   /  \
 /.\ .\.\// \/... \.::::..... _/..\ ..\:|:. .  / .. \\  /.. \    /...\ /  \ \
/...\.../..:.\. ..:::::::..:..... . ...\{:... / %... \\/..%. \  /./:..\__   \
 .:..\:..:::....:::;;;;;;::::::::.:::::.\}.....::%.:. \ .:::. \/.%:::.:..\
::::...:::;;:::::;;;;;;;;;;;;;;:::::;;::{:::::::;;;:..  .:;:... ::;;::::..
;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;];;;;;;;;;;::::::;;;;:.::;;;;;;;;:..
;;;;;;;;;;;;;;ii;;;;;;;;;;;;;;;;;;;;;;;;[;;;;;;;;;;;;;;;;;;;;;;:;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;iiiiiiii;;;;;;;;;;;;;;};;ii;;iiii;;;;i;;;;;;;;;;;;;;;ii;;;
iiii;;;iiiiiiiiiiIIIIIIIIIIIiiiiiIiiiiii{iiIIiiiiiiiiiiiiiiii;;;;;iiiilliiiii
IIIiiIIllllllIIlllIIIIlllIIIlIiiIIIIIIIIIIIIlIIIIIllIIIIIIIIiiiiiiiillIIIllII
IIIiiilIIIIIIIllTIIIIllIIlIlIIITTTTlIlIlIIIlIITTTTTTTIIIIlIIllIlIlllIIIIIIITT
IIIIilIIIIITTTTTTTIIIIIIIIIIIIITTTTTIIIIIIIIITTTTTTTTTTIIIIIIIIIlIIIIIIIITTTT
IIIIIIIIITTTTTTTTTTTTTIIIIIIIITTTTTTTTIIIIIITTTTTTTTTTTTTTIIIIIIIIIIIIIITTTTT''')
    print("\nThe mines seems desert at first sight but you can see a comfy fire far away")
else:
    print("please choose 1 or 2 adventurer")

cprint(figlet_format("The end", font ="slant"), "blue", attrs=["bold"])
