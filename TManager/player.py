import random


class Player:
    """
    player is on a single team, with many other players
    player play in a game for a team
    """

    def __init__(self, name, skill):
        self.name = name
        # player skill rankings
        self.skill = skill

    def salary(self):
        return 5000 + self.skill * 100

    # to get the string representation of the object
    def __str__(self):
        return (f'{self.name}\tSkill: {self.skill}\tSalary: ${self.salary()}')


def generate_player():
    first_names = [
        'Liam', 'Noah', 'Oliver', 'Lucas', 'Elijah', 
        'Mason', 'Logan', 'Ethan', 'James', 'Aiden', 
        'Carter', 'Jackson', 'Sebastian', 'Benjamin', 
        'Alexander', 'Michael', 'Jacob', 'Daniel', 'William'
    ]
    last_names = [
        'Smith', 'Jones', 'Williams', 'Taylor', 'Brown', 
        'Davies', 'Evans', 'Wilson', 'Thomas', 'Johnson', 
        'Roberts', 'Robinson', 'Thompson', 'Wright', 'Walker', 
        'White', 'Edwards', 'Hughes', 'Green', 'Hall', 'Lewis', 
        'Harris', 'Clarke', 'Patel', 'Jackson', 'Wood', 'Turner', 
        'Martin', 'Cooper', 'Hill', 'Ward', 'Morris', 'Moore', 'Clark'
    ]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f'{first_name} {last_name}'
    skill = 10 + random.randint(0, 90)
    return Player(full_name, skill)
