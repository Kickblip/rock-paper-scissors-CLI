def title():
    '''drawing title'''
    print(
        r"""
     ______     ______   ______        __         __     ______   ______    
    /\  == \   /\  == \ /\  ___\      /\ \       /\ \   /\__  _\ /\  ___\   
    \ \  __<   \ \  _-/ \ \___  \     \ \ \____  \ \ \  \/_/\ \/ \ \  __\   
     \ \_\ \_\  \ \_\    \/\_____\     \ \_____\  \ \_\    \ \_\  \ \_____\ 
      \/_/ /_/   \/_/     \/_____/      \/_____/   \/_/     \/_/   \/_____/                                                                                                                       
        """
    )

# r""" notation -> https://stackoverflow.com/a/49142875

def newgame():
    '''part 2 of the title'''
    print(
        r"""
                                                    _________
                   ,--.--._                         |.-----.|
            ------" _, \___)                        ||x . x||
                    / _/____)       New Game        ||_.-._||
                    \//(____)                       `--)-(--`
            ------\     (__)                       __[=== o]___
                   `-----"                        |:::::::::::|\ 
                                                  `-=========-`()
        """
    )


def playerWin():
    '''print that the player wins'''
    print(
        r"""
        __  ______  __  __   _       _______   __
        \ \/ / __ \/ / / /  | |     / /  _/ | / /
         \  / / / / / / /   | | /| / // //  |/ / 
         / / /_/ / /_/ /    | |/ |/ // // /|  /  
        /_/\____/\____/     |__/|__/___/_/ |_/   
                                         
        """
    )


def playerLoss():
    '''print that the player loses'''
    print(
        r"""
        __  ______  __  __   __    ____  ___________
        \ \/ / __ \/ / / /  / /   / __ \/ ___/_  __/
         \  / / / / / / /  / /   / / / /\__ \ / /   
         / / /_/ / /_/ /  / /___/ /_/ /___/ // /    
        /_/\____/\____/  /_____/\____//____//_/     
                                            
        """
    )


def playerTie():
    '''print that the player ties'''
    print(
        r"""
            _______________    ___       ________________
           /  _/_  __/ ___/   /   |     /_  __/  _/ ____/
           / /  / /  \__ \   / /| |      / /  / // __/   
         _/ /  / /  ___/ /  / ___ |     / / _/ // /___   
        /___/ /_/  /____/  /_/  |_|    /_/ /___/_____/   
                                                 
        """
    )


def decideWinner(user, comp):
    '''prints winner and return true/false based on win/lose'''
    if (user == comp):
        playerTie()

    elif ((user == "rock" and comp == "scissors")
          or (user == "paper" and comp == "rock")
            or (user == "scissors" and comp == "paper")):
        playerWin()
        return True

    elif ((user == "rock" and comp == "paper")
          or (user == "paper" and comp == "scissors")
            or (user == "scissors" and comp == "rock")):
        playerLoss()
        return False

    else:
        print("something went wrong...")
