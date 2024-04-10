import random

artlist=['''    o__ __o                   o     o     o                     o                           
   /v     v\                 <|>  _<|>_  <|>                  _<|>_                         
  />       <\                / \         < >                                                
 _\o____          o__ __o    \o/    o     |         o__ __o/    o    \o__ __o     o__  __o  
      \_\__o__   /v     v\    |    <|>    o__/_    /v     |    <|>    |     |>   /v      |> 
            \   />       <\  / \   / \    |       />     / \   / \   / \   < >  />      //  
  \         /   \         /  \o/   \o/    |       \      \o/   \o/   \o/        \o    o/    
   o       o     o       o    |     |     o        o      |     |     |          v\  /v __o 
   <\__ __/>     <\__ __/>   / \   / \    <\__     <\__  / \   / \   / \          <\/> __/> 
                                                                                            
                                                                                            
                                                                                            ''',
''' ░▒▓███████▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓████████▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░   
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
                                                                                                        
                                                                                                        ''',
'''
  ______             __  __    __                __                     
 /      \           /  |/  |  /  |              /  |                    
/$$$$$$  |  ______  $$ |$$/  _$$ |_     ______  $$/   ______    ______  
$$ \__$$/  /      \ $$ |/  |/ $$   |   /      \ /  | /      \  /      \ 
$$      \ /$$$$$$  |$$ |$$ |$$$$$$/    $$$$$$  |$$ |/$$$$$$  |/$$$$$$  |
 $$$$$$  |$$ |  $$ |$$ |$$ |  $$ | __  /    $$ |$$ |$$ |  $$/ $$    $$ |
/  \__$$ |$$ \__$$ |$$ |$$ |  $$ |/  |/$$$$$$$ |$$ |$$ |      $$$$$$$$/ 
$$    $$/ $$    $$/ $$ |$$ |  $$  $$/ $$    $$ |$$ |$$ |      $$       |
 $$$$$$/   $$$$$$/  $$/ $$/    $$$$/   $$$$$$$/ $$/ $$/        $$$$$$$/ 
                                                                        
''',
'''
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || |     ____     | || |   _____      | || |     _____    | || |  _________   | || |      __      | || |     _____    | || |  _______     | || |  _________   | |
| |   /  ___  |  | || |   .'    `.   | || |  |_   _|     | || |    |_   _|   | || | |  _   _  |  | || |     /  \     | || |    |_   _|   | || | |_   __ \    | || | |_   ___  |  | |
| |  |  (__ \_|  | || |  /  .--.  \  | || |    | |       | || |      | |     | || | |_/ | | \_|  | || |    / /\ \    | || |      | |     | || |   | |__) |   | || |   | |_  \_|  | |
| |   '.___`-.   | || |  | |    | |  | || |    | |   _   | || |      | |     | || |     | |      | || |   / ____ \   | || |      | |     | || |   |  __ /    | || |   |  _|  _   | |
| |  |`\____) |  | || |  \  `--'  /  | || |   _| |__/ |  | || |     _| |_    | || |    _| |_     | || | _/ /    \ \_ | || |     _| |_    | || |  _| |  \ \_  | || |  _| |___/ |  | |
| |  |_______.'  | || |   `.____.'   | || |  |________|  | || |    |_____|   | || |   |_____|    | || ||____|  |____|| || |    |_____|   | || | |____| |___| | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
''',
'''
   _____       _ _ _        _          
  / ____|     | (_) |      (_)         
 | (___   ___ | |_| |_ __ _ _ _ __ ___ 
  \___ \ / _ \| | | __/ _` | | '__/ _ \\
  ____) | (_) | | | || (_| | | | |  __/
 |_____/ \___/|_|_|\__\__,_|_|_|  \___|
                                       
                                       
''',
'''
.------..------..------..------..------..------..------..------..------.
|S.--. ||O.--. ||L.--. ||I.--. ||T.--. ||A.--. ||I.--. ||R.--. ||E.--. |
| :/\: || :/\: || :/\: || (\/) || :/\: || (\/) || (\/) || :(): || (\/) |
| :\/: || :\/: || (__) || :\/: || (__) || :\/: || :\/: || ()() || :\/: |
| '--'S|| '--'O|| '--'L|| '--'I|| '--'T|| '--'A|| '--'I|| '--'R|| '--'E|
`------'`------'`------'`------'`------'`------'`------'`------'`------'
PS: I really wanted to make the cards look like this :(
''',
'''
        _            _            _              _        _            _                    _          _           _      
       / /\         /\ \         _\ \           /\ \     /\ \         / /\                 /\ \       /\ \        /\ \    
      / /  \       /  \ \       /\__ \          \ \ \    \_\ \       / /  \                \ \ \     /  \ \      /  \ \   
     / / /\ \__   / /\ \ \     / /_ \_\         /\ \_\   /\__ \     / / /\ \               /\ \_\   / /\ \ \    / /\ \ \  
    / / /\ \___\ / / /\ \ \   / / /\/_/        / /\/_/  / /_ \ \   / / /\ \ \             / /\/_/  / / /\ \_\  / / /\ \_\ 
    \ \ \ \/___// / /  \ \_\ / / /            / / /    / / /\ \ \ / / /  \ \ \           / / /    / / /_/ / / / /_/_ \/_/ 
     \ \ \     / / /   / / // / /            / / /    / / /  \/_// / /___/ /\ \         / / /    / / /__\/ / / /____/\    
 _    \ \ \   / / /   / / // / / ____       / / /    / / /      / / /_____/ /\ \       / / /    / / /_____/ / /\____\/    
/_/\__/ / /  / / /___/ / // /_/_/ ___/\ ___/ / /__  / / /      / /_________/\ \ \  ___/ / /__  / / /\ \ \  / / /______    
\ \/___/ /  / / /____\/ //_______/\__\//\__\/_/___\/_/ /      / / /_       __\ \_\/\__\/_/___\/ / /  \ \ \/ / /_______\   
 \_____\/   \/_________/ \_______\/    \/_________/\_\/       \_\___\     /____/_/\/_________/\/_/    \_\/\/__________/   
                                                                                                                          
''',
'''
      ___           ___           ___                   ___           ___                       ___           ___     
     /\  \         /\  \         /\__\      ___        /\  \         /\  \          ___        /\  \         /\  \    
    /::\  \       /::\  \       /:/  /     /\  \       \:\  \       /::\  \        /\  \      /::\  \       /::\  \   
   /:/\ \  \     /:/\:\  \     /:/  /      \:\  \       \:\  \     /:/\:\  \       \:\  \    /:/\:\  \     /:/\:\  \  
  _\:\~\ \  \   /:/  \:\  \   /:/  /       /::\__\      /::\  \   /::\~\:\  \      /::\__\  /::\~\:\  \   /::\~\:\  \ 
 /\ \:\ \ \__\ /:/__/ \:\__\ /:/__/     __/:/\/__/     /:/\:\__\ /:/\:\ \:\__\  __/:/\/__/ /:/\:\ \:\__\ /:/\:\ \:\__\\
 \:\ \:\ \/__/ \:\  \ /:/  / \:\  \    /\/:/  /       /:/  \/__/ \/__\:\/:/  / /\/:/  /    \/_|::\/:/  / \:\~\:\ \/__/
  \:\ \:\__\    \:\  /:/  /   \:\  \   \::/__/       /:/  /           \::/  /  \::/__/        |:|::/  /   \:\ \:\__\  
   \:\/:/  /     \:\/:/  /     \:\  \   \:\__\       \/__/            /:/  /    \:\__\        |:|\/__/     \:\ \/__/  
    \::/  /       \::/  /       \:\__\   \/__/                       /:/  /      \/__/        |:|  |        \:\__\    
     \/__/         \/__/         \/__/                               \/__/                     \|__|         \/__/    
''',
'''
  ██████  ▒█████   ██▓     ██▓▄▄▄█████▓ ▄▄▄       ██▓ ██▀███  ▓█████ 
▒██    ▒ ▒██▒  ██▒▓██▒    ▓██▒▓  ██▒ ▓▒▒████▄    ▓██▒▓██ ▒ ██▒▓█   ▀ 
░ ▓██▄   ▒██░  ██▒▒██░    ▒██▒▒ ▓██░ ▒░▒██  ▀█▄  ▒██▒▓██ ░▄█ ▒▒███   
  ▒   ██▒▒██   ██░▒██░    ░██░░ ▓██▓ ░ ░██▄▄▄▄██ ░██░▒██▀▀█▄  ▒▓█  ▄ 
▒██████▒▒░ ████▓▒░░██████▒░██░  ▒██▒ ░  ▓█   ▓██▒░██░░██▓ ▒██▒░▒████▒
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░▓  ░░▓    ▒ ░░    ▒▒   ▓▒█░░▓  ░ ▒▓ ░▒▓░░░ ▒░ ░
░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░ ▒  ░ ▒ ░    ░      ▒   ▒▒ ░ ▒ ░  ░▒ ░ ▒░ ░ ░  ░
░  ░  ░  ░ ░ ░ ▒    ░ ░    ▒ ░  ░        ░   ▒    ▒ ░  ░░   ░    ░   
      ░      ░ ░      ░  ░ ░                 ░  ░ ░     ░        ░  ░
                                                                     
''']

def printTitle():
    print(random.choice(artlist))
    print("\nPress i to see instructions\n")
def printInst():
    print('''\n\nInstructions:
          1. Use ">" to move a card from one column to another (e.g. 1>2 moves the top card from column 1 to column 2)
          2. use "w" to go to the next card in the withdraw deck
          3. use "f>[columnNumber]" to move a card from the foundation to column (e.g. f>1 moves the top card of the same suit in foundation to column 1)
          4. use "w>[columnNumber]" to move a card from the withdraw deck to a column (e.g. w>1 moves the top card of the withdraw deck to column 1)
          5. use "w>f" to move the top card of the withdraw deck to the foundation
          6. use "q" to quit the game\n''')