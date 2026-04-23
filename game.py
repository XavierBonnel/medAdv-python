from pyfiglet import figlet_format

RED   = '\033[1;31m'
BLUE  = '\033[1;34m'
RESET = '\033[0m'


async def main():
    print(RED + figlet_format("Medieval Adventures", font="slant") + RESET)

    print("""
|          .-----.     |
| \\ ' /   _/    )/     |
|- ( ) -('---''--).    |
| / . \\(((()\\^_^/)().  |
|  \\\\_\\ (()_)-((()().  |
|   '- \\ )/\\._./(().   |
|     '/\\/( X   ) \\    |
|     (___)|___/ ) \\.  |
|          |.#_|(___). |
|         /\\    \\ ( (_ |
|         \\/\\/\\/\\) \\\\.  |
|         | / \\ |.     |
|         |(   \\|.     |
|        _|_)__|_\\_.   |
|        )...()...(.   |
|         | (   \\ |    |
|      .-'__,)  (  \\. |
|            '\\_-,     |
             mrf""")

    name = await input("\n\n What is your name adventurer?\n")
    print("\nWelcome to this wonderful journey " + name + "\n")
    print("where do you want to go?\n")
    print("1. the dark forest of the elves?")
    print("2. the cosey mines of the dwarves?\n")

    first_choice = await input("choose: ")

    if first_choice == "1":
        print(r"""
     | ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^  |
     |/|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\ |
     |/|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\ |
     ||/|\/|\/|\ /|\  |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\ |
      ejm96
        """)
        print("\nYou enter a dark mysterious and ancient forest, you hear the wind and a distant song, probably a sad one\n")
        print("What do you do?\n")
        print("1. You walk toward the voice")
        print("2. You run in the opposite direction\n")

        second_choice = await input("choose: ")

        if second_choice == "1":
            print(r"""
|:____|\_________b___/______.____.__|__________._______.---.__.____________:|
|:____|/__4____|.____$______|____|__|__________|\__-,__|___|__|\_______..__:|
|:___/|___4____'`____/______|____|__|__________|___/___|___|__|\___""______:|
|:__('|)___________________@|___(|__|__#( )___@|._____@|__@|_@|____________:|
     "|                              mp                                    /
""")
            print("You approach an old elf. He tells you about his youth as a great warrior in the century war he participated in against the orks to protect the forest of his ancestors.\n")

            print("What do you do?\n")
            print("1. You knock him out from behind and steal his enchanted equipment")
            print("2. You ask him for magic secrets that could help your quest\n")

            elf_choice = await input("choose: ")

            if elf_choice == "1":
                print(r"""
                _.--.
            _.-'_:-'||
        _.-'_.-::::'||
   _.-:'_.-::::::'  ||
 .'`-.-:::::::'     ||
/.'`;|:::::::'      ||_
||   ||::::::'     _.;._'-._
||   ||:::::'  _.-!oo @.!-._'-.
\'.  ||:::::.-!()oo @!()@.-'_.|
 '.'-;|:.-'.&$@.& ()$%-'o.'\U||
   `>'-.!@%()@'@_%-'_.-o _.|'||
    ||-._'-.@.-'_.-' _.-o  |'||
    ||=[ '-._.-\U/.-'    o |'||
    || '-.]=|| |'|      o  |'||
    ||      || |'|        _| ';
    ||      || |'|    _.-'_.-'
    |'-._   || |'|_.-'_.-'
 jgs '-._'-.|| |' `_.-'
         '-.||_/.-'
""")
                print("You strike the old elf from behind and seize his enchanted bow. The forest shudders as you flee into the shadows with your stolen prize.\n")

            elif elf_choice == "2":
                print(r"""
                       ,`-.
                     ,'   |
                   ,'     |
                 ,'       :
               ,<\        \
             ,' //         .
           ,' ,'/          :
         ,'  /,'           |
        /._,'/             |
       /.__,'              |
      /                    |
   .-'                     |
   '.                      |
     |`-._          ,      |
     ; -. `-.     ,'|      :
    / |@)\  |   ,', ;      '
   /        |  : /| |     /
  /         |  |: | |     :
,'          |  |'-' ;     |
|   .      ,'`._|   /-._   `
`-.\ )   ,'       -'    `-,-'
   |    :                :
   ;._                   |
   \__`.         )       |
   /_         ,-'        |
  ,'       ,-'           |
 (     _,-'\             |
  `._,'     :            | SSt
            '
""")
                print("The old elf smiles and reveals a powerful incantation capable of opening any sealed door. He places an ancient scroll in your hands, his eyes gleaming with quiet hope.\n")

            else:
                print("please choose 1 or 2 adventurer")

        elif second_choice == "2":
            print(r"""
|                 ^                  |
|                / \                 |
|           ^   _|.|_   ^            |
|         _|I|  |I .|  |.|_          |
|         \II||~~| |~~||  /          |
|          ~\~|~~~~~~~|~/~           |
|             \|II I ..|/            |
|        /\    |II.    |    /\.      |
|       /  \  _|III .  |_  /  \.    |
|       |-~| /(|I.I I  |)\ |~-|.    |
|     _/(I | +-----------+ |. )\_.  |
|     \~-----/____-~-____\-----~/.  |
|      |I.III|  /(===)\  |  .. |.   |
|      /~~~-----_________---~~~\.   |
|     `##########!\-#####%!!!!!| |\ |
|    _/###########!!\~~-_##%!!!\_/|.|
|    \##############!!!!!/~~-_%!!!!\ |
|     ~)#################!!!!!/~~--\_|
|  __ /#####################%%!!!!/ /|
|  \,~\-_____##############%%%!!!!\/ |
|  /!!!!\ \ \~-_###########%%%!!!!\  |
| /#####!!!!!!!\~-_#######%%%!!!!!!\_|
|/#############!!!\#########%%%!!!!!!|\
""")
            print("\nYou ran through the woods past a hill and you see a magnificent castle beneath you\n")

            print("What do you do?\n")
            print("1. You approach the castle — the atmosphere grows heavy, growls echo from within")
            print("2. You skirt the building along the walls, looking for a hidden breach\n")

            castle_choice = await input("choose: ")

            if castle_choice == "1":
                print(r"""
8888888  |::L.L:::+:" _.--:_:-'::.`.    _.-'    :"|':|:|. . . .JY88888b
 8888888   L:| |::::|\ \_:-'     `::.`.-'    :"|-'. .J:J. . , . F Y88888b
 Y888888    \:L L:::L:\ `.      _.-'_.=+ :"|-: . , . |:| , . , |   Y88888b
 `888888b    \|.|:::|:::. \ _.-'_.=: . |-', . . , . J:J . . . J     Y88888b
  Y888888     +'\:::J::::\ '_.='. . . .F . .,-T`\. .|:|. , ,-'      )888888
   Y88888b.      \:::L::::+. . , . . .J . ,/  |:O .J:J. ,-'        .d888888
    Y888888b      \::|::::| . . . , . |. . F  ::|,-'+|-'         .d88888888
     Y888888b      \:J::::|. . . . . .F , J .::-:              .od88888888P
      Y888888b      \:L:::| . , . , .J . .|::' ` \d8888888888888888888888P
       Y888888b      \|:::|. , . . , |. ,-'`.  `\ `+88888888888888888888P
        Y888888b.     J:::| . . , . .F-'     \\ ` \ \88888888888888888P'
         Y8888888b     L::|, . . , .J       d8+.`\  \`+8888888888888P'
          Y8888888b    |::| . , . ._+      d8888\  ` .'  `Y888888P'
          `88888888b   J::|. . ._-'     .od888888\.-'
           Y88888888b   \:| ._-'     d888888888P'              ,==. o
           `888888888b   \|-'       d88888888'                 |/ "'/L
            `Y88888888b            d8888888P'                 ,-_) '>>
""")
                print("You approach the great gates. A deep resonant growl shakes the stones. Something ancient and terrible stirs behind the walls.\n")

            elif castle_choice == "2":
                print(r"""
                  ,.=,,==. ,,_
                  _ ,====, _    |I|`` ||  `|I `|
                 |`I|    || `==,|``   ^^   ``  |
                 | ``    ^^    ||_,===TT`==,,_ |
                 |,==Y``Y==,,__| \L=_-`'   +J/`
                  \|=_  ' -=#J/..-|=_-     =|
                   |=_   -;-='`. .|=_-     =|----T--,
                   |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                   |=||  -|=_-. . |=_-| |  =|-|-||::\____
                   |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                   |=_   -|=_-_.  |=_-     =|-|-||:::::::
                   |=_   -|=//^\. |=_-     =||-|-|:::::::
               ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
            ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
        ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::
       |;:;K`__,...;=\_____,=``           %%%&     %#,---
       |;::::::::::::|       `'.________+-------\   ``
      /8M%;:::;;:::::|                  |        `-------
""")
                print("You circle the castle for what feels like hours. Behind a curtain of wild ivy, you find a narrow crack in the ancient stone — just wide enough to slip through.\n")

            else:
                print("please choose 1 or 2 adventurer")

        else:
            print("please choose 1 or 2 adventurer")

    elif first_choice == "2":
        print(r"""
|                      _                                                      |
|                     /#\                                                     |
|                    /###\     /\                                             |
|                   /  ###\   /##\  /\                                        |
|                  /      #\ /####\/##\                                       |
|                 /  /      /   # /  ##\             _       /\               |
|               // //  /\  /    _/  /  #\ _         /#\    _/##\    /\.       |
|              // /   /  \     /   /    #\ \      _/###\_ /   ##\__/ _\.      |
|             /  \   / .. \   / /   _   { \ \   _/       / //    /    \\.     |
|     /\     /    /\  ...  \_/   / / \   } \ | /  /\  \ /  _    /  /    \ /\.|
|  _ /  \  /// / .\  ..%:.  /... /\ . \ {:  \\   /. \     / \  /   ___   /  \|
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
|IIIIIIIIITTTTTTTTTTTTTIIIIIIIITTTTTTTTIIIIIITTTTTTTTTTTTTTIIIIIIIIIIIIIITTTTT|
        """)
        print("\nThe mines seem deserted at first sight but you can see a cozy fire far away\n")
        print("What do you do?\n")
        print("1. You run toward the fire — the closer you get, the stranger the atmosphere.")
        print("2. You take your sword and walk carefully down a corridor.\n")

        third_choice = await input("choose: ")

        if third_choice == "1":
            print(r"""
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
|  \#/     .-"#'-.   .-"#'-,   .-"#'-.   .-=#"-;     `#/.|
|.-"#'-.   |"=,-"|   |"-.-"|)  1"-.-"|   |"-.-"|   ,-"#"-.|
||"-.-"|   |  !  |   |     |   |     |   |     !   |"-.-"||
||     |   |     |._,|     |   |     |._,|     a   |     ||
||     |   |     |   |     |   |     |   |     p   |     ||
||     |   |     |   |     |   |     |   |     x   |     ||
|'-._,-'   '-._,-'   '-._,-'   '-._,-'   '-._,-"   '-._,-'|
""")
            print("Finally, you meet a group of happy dwarves smoking and debating on how to get more gold out of the mountain. You share a beer with them and they invite you to the city a kilometer below.\n")

            print("What do you do?\n")
            print("1. You follow the dwarves deeper underground toward their city")
            print("2. You challenge the biggest dwarf to an arm wrestling contest\n")

            dwarf_choice = await input("choose: ")

            if dwarf_choice == "1":
                print(r"""
:::8888888888888888888888888888888P""""""48888888888888888888888::::88
::::8888888888888888888888P   ____.------.____   488888888888888:::888
::::88888888888888888P __.--""    _._         ""--.__ 4888888888:::888
:::::888888888888P _.-"        .-~ | ~-.             "-._ 488888:::888
:::::888888888P _-"            |   |   |                 "-_ 488::8888
::::::888888P ,'               |  _:_  |                    .-:~--.._8
8:::::88888 ,'            .  .-"~~ | ~~"-.                .~  |      |
88:::::88P /_.-~:.   .   :   |     |     |       .        |   |      |
888::::8P /|    | `.o    !   |     |     |        :       |   |      |
8P_..--~:-.|    |  |    d    |     |     | .       o      |   |      |
8|      |  ~.   |  |    o    |  __.:.__  | ;       b      |   |      |
8|      |   |   |  |   d8  .-"~~   |   ~~"-.o       8     |   |      |
8|      |   |  _|.--~:-98  |       |       |8b      8.:~-.|   |      |
8|      A   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
8|      M   | |      |   | |       |  |   |     |  |  |   |   |      |
8|      C   | |      |   | |       |  |   |     |  |  |   |   O      |
8|      |   | |      |   | |       |  |   |     |  |  |   |   j      |
8|      9   | |      |   | |       |  |   |     |  |  |   |   o      |
8|      9   | |      |   | |       |  |   |     |  |  |   |   |      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
                print("You follow the dwarves for hours, descending spiral tunnels carved with ancient runes. At last you emerge into a vast underground city, lit by a thousand amber lanterns carved from living rock.\n")

            elif dwarf_choice == "2":
                print(r"""
       \                                           ___/________
  ___   )                    ,  @                    /    \  \
@___, \ /                  @__\  /\              @___/      \@/
/\__,   |                  /\_, \/ /             /\__/        |
/ \    / @\                / \   (               / \ /        / \
/__|___/___/_______________/__|____\_____________/__/__________|__\__
""")
                print("You slam your arm on the table with a grin. The biggest dwarf cracks his knuckles. Three seconds later the whole tavern erupts — mugs flying, benches splintering, and everyone cheering.\n")

            else:
                print("please choose 1 or 2 adventurer")

        elif third_choice == "2":
            print(r"""
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
""")
            print('Soon the corridor reveals many choices — good... and probably bad.\n')

            print("What do you do?\n")
            print("1. You take the left corridor — a familiar voice softly calls your name")
            print("2. You take the right corridor — something large sways in the shadows\n")

            corridor_choice = await input("choose: ")

            if corridor_choice == "1":
                print(r"""
             ..-.--..
           ,','.-`.-.`.
          :.',;'     `.\.
          ||//----,-.--\|
         `:|/-----`-'--||'
          \|:    |:'
          `||      \   |!
          |!|          ;|
          !||:.   --  /|!
         /||!||:.___.|!||\
        /|!|||!|    |!||!\\:.
     ,'//!||!||!`._.||!||,:\\\
    : :: |!|||!| SSt|!||! |!::
    | |! !||!|||`---!|!|| ||!|
    | || |!|||!|    |!||! |!||
""")
                print("You follow the voice into the darkness. At the end of the corridor stands a figure — your exact reflection. But its eyes are hollow, its grin too wide, its posture twisted by something that was once a mind.\n")

            elif corridor_choice == "2":
                print(r"""
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_          _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
""")
                print("A massive chest hangs from chains in the vaulted darkness, slowly swinging. Its ornate arms stretch toward you as if reaching. It is waiting.\n")

            else:
                print("please choose 1 or 2 adventurer")

        else:
            print("please choose 1 or 2 adventurer")

    else:
        print("please choose 1 or 2 adventurer")

    print(BLUE + figlet_format("To be continued...", font="slant") + RESET)


await main()
