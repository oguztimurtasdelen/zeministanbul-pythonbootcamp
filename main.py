from distutils.log import error
import welcome as pyWelcome
import hero as pyHero
import battle as pyBattle


"""
Thor            = Hero("God", "Asgard", "Hammer", "Thunder", 1, 90)
BlackPanther    = Hero("Human", "Wakanda", "Black Panther Suit", "Fight", 2, 87)
Hulk            = Hero("Giant", "America", "Smash", "Punch", 2, 92)
ScarletWitch    = Hero("Human", "Sokovia", "Mind", "Mythical Ability", 2, 98)

print(Thor.UsePower())
"""


def createBattle():
    print("Please define the number of heros that you want for each team.")
    print("1) 1v1")
    print("2) 2v2")
    print("3) 3v3")
    
    try:
        v_input = int(input('Your Option: '))
        if v_input == 1 or v_input == 2 or v_input == 3:
            pass
        else:
            v_input = error
    except:
        v_input = error
    finally:
        return v_input



def createHero(v_index):
    print('')
    print('Superhero #' + str(v_index))
    v_name      = input('Name: ')
    v_race      = input('Race: ')
    v_homeland  = input('Homeland: ')
    v_weapon    = input('Weapon: ')
    v_skill     = input('Skill: ')
    v_team      = input('Team (1 or 2): ')

    while v_team not in ["1", "2"]:
        v_warningMessage = 'Please enter only "1" or "2" to choose a team for your superhero!'
        print(v_warningMessage.upper())
        v_team = input('Team (1 or 2): ')
    
    if int(v_team) == 1:
        obj_superhero = pyHero.Team1(v_name, v_race, v_homeland, v_weapon, v_skill)
    elif int(v_team) == 2:
        obj_superhero = pyHero.Team2(v_name, v_race, v_homeland, v_weapon, v_skill)
    else:
        pass # not possible as an option

    return obj_superhero



def checkTeams(p_numberOfHero, p_list):
    v_team1 = 0

    for i in p_list: # Turn for each superhero in the list
        if i.team == "TEAM1": # Get the total number of superhero for TEAM1
            v_team1 += 1

    if v_team1 == p_numberOfHero:
        return True
    else:
        return False




def main():
    # Define variables here
    listSuperHero   = []

    v_userName = input('Please enter your name: ')
    print('')

    # Welcome text
    pyWelcome.f_introducing(v_userName)
    
    v_numberOfHero = createBattle()
    # If there is an issue with the input by user, ask him/her again, but not recursively
    if v_numberOfHero == error:
        v_numberOfHero = createBattle()
    
    for i in range(v_numberOfHero * 2): # Multiply with 2 because there are two teams in a battle
        v_hero = createHero(i + 1)
        listSuperHero.append(v_hero)

    v_checkTeams = checkTeams(v_numberOfHero, listSuperHero)
    
    if v_checkTeams:
        print('Teams builded up successfully'.upper())
        print('')
        print('Marvel universe of ' + v_userName + ' Civil War is starting!'.title())
        print('')
        print('')
        pyBattle.startBattle(listSuperHero)

    else:
        print('')
        print('Please define equal number of superheros for each team. The battle has to be in fair!'.upper())
        print('')
        main()
    

if __name__ == "__main__":
    main()



