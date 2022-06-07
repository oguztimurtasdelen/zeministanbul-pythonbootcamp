import random

def fight(p_superHero1, p_superHero2):
    print( p_superHero1.name + " from " + p_superHero1.homeland + " hit " + p_superHero2.name + " in " + p_superHero1.skill + " with " + p_superHero1.weapon + " -> Damage Point: " + str(p_superHero1.power) )
    return p_superHero1.power


def startBattle(p_listSuperHero):
    listTeam1       = []
    listTeam2       = []
    v_countTeam1    = 0
    v_countTeam2    = 0
    v_scoreTeam1    = 0
    v_scoreTeam2    = 0


    for i in p_listSuperHero:
        if i.team == "TEAM1":
            listTeam1.append(i)
            v_countTeam1 += 1
        else: # TEAM2
            listTeam2.append(i)
            v_countTeam2 += 1
    
    print('')
    
    for t1 in listTeam1:
        v_scoreTeam1 += fight(t1, listTeam2[ random.randint(0, v_countTeam2 - 1) ])
    
    for t2 in listTeam2:
        v_scoreTeam2 += fight(t2, listTeam1[ random.randint(0, v_countTeam1 - 1) ])

    print('')
    print("Team 1: " + str(v_scoreTeam1) + " - " + str(v_scoreTeam2) + " :Team 2")

    if v_scoreTeam1 > v_scoreTeam2:
        print('Team 1 WON!')
        for teamMembers in listTeam1:
            print(teamMembers.race + " " + teamMembers.name + " from " + teamMembers.homeland + " uses " + teamMembers.weapon + " to " + teamMembers.skill + " for " + teamMembers.team + " with " + str(teamMembers.power) + " damage point.")
    elif v_scoreTeam1 < v_scoreTeam2:
        print('Team 2 WON!')
        for teamMembers in listTeam2:
            print(teamMembers.race + " " + teamMembers.name + " from " + teamMembers.homeland + " uses " + teamMembers.weapon + " to " + teamMembers.skill + " for " + teamMembers.team + " with " + str(teamMembers.power) + " damage point.")

    else: # v_scoreTeam1 = v_scoreTeam2
        pass
