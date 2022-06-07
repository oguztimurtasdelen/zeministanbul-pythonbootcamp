import random

class Hero():
    """
    race = "Human" / "God" / "Giant" / "Wizard"
    homeland = "Asgard", "Wakanda", "New York"
    weapon = "Hammer", "Shield", "Arrow", "Kick", "Cobweb"
    skill = "Thunder", "Shield", "Smash", "Kicking"
    team = 1 / 2
    power = ?/100
    """
    #constructor
    def __init__(self, name, race, homeland, weapon, skill, team) -> None:
        self.name = name.title()
        self.race = race.title()
        self.homeland = homeland.upper()
        self.weapon = weapon.title()
        self.skill = skill.lower()
        self.team = team
        self.power = self.__definePower(self.race)


    # private method
    @staticmethod
    def __definePower(p_race):
        __minPower = 1
        __maxPower = 100
        return random.randint(__minPower, __maxPower)


class Team1(Hero):
    def __init__(self, name, race, homeland, weapon, skill) -> None:
        super().__init__(name, race, homeland, weapon, skill, 'TEAM1')
        

class Team2(Hero):
    def __init__(self, name, race, homeland, weapon, skill) -> None:
        super().__init__(name, race, homeland, weapon, skill, 'TEAM2')