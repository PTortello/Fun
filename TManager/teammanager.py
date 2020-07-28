from helpers import select_from_menu

class TeamManager:
    """
    runs a team
    """
    def __init__(self, team, league):
        self.team = team
        self.league = league
        self.inputs = {
            1: self.view_players_head,
            2: self.view_market,
            3: self.trade_players,
            4: self.next_round
        }
        self.finished = False
        print('You are a manager')
        print(f'You manage {self.team}')
        print('Good luck')
    
    def manage(self):
        """
        before every round, we can make changes as a manager
        """
        print('')
        print(f'Your team is {self.team}')
        print(f'You have {self.team.wins} wins out ' 
                f'of {self.league.rounds_played} games')
        print(f'You currently have ${self.team.money}')
        print('')
        while not self.finished:
            self.print_menu()
            select_from_menu(self.inputs)
        self.finished = False
        print('')
    
    def print_menu(self):
        print('1. View your team players')
        print('2. View your players on the market')
        print('3. Trade players')
        print('4. Play the next round')
    
    def view_market(self):
        for i, player in enumerate(self.league.players):
            print(f'{i}: {player}')

    def view_players_head(self):
        print(f'{self.team.name}\tTeam rating: {self.team.rating()}\tTeam payroll: ${self.team.payroll()}')
        print('-' * 55)
        self.view_players()

    def view_players(self):
        for i, player in enumerate(self.team.players):
            print(f'{i}: {player}')

    def trade_players(self):
        """
        switch a player from your team for a free agent
        """
        # select a player from your team
        self.view_players()
        player_index = int(input('\nWhich player do you want to switch: '))
        # select a player from the free agents
        self.view_market()
        market_index = int(input('\nWhich player do you want to hire: '))
        # switch em
        print(
            f'\nSwitching:\n'
            f'{self.team.players[player_index]}'
            '\n\nFor:\n'
            f'{self.league.players[market_index]}'
        )
        player_from_team = self.team.players.pop(player_index)
        player_from_market = self.league.players.pop(market_index)
        self.team.players.append(player_from_market)
        self.league.players.append(player_from_team)

    def next_round(self):
        self.finished = True
