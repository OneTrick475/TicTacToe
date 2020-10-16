class Tictactoe:
    def __init__(self):
        self.board = [' ' for x in range(9)]
        self.current_move = 0

    winning_combos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    def show_board(self):
        print(f'''
 {self.board[0]} | {self.board[1]} | {self.board[2]} 
-----------
 {self.board[3]} | {self.board[4]} | {self.board[5]} 
-----------
 {self.board[6]} | {self.board[7]} | {self.board[8]} 
''')

    def minimax(self, is_max, player):
        if self.won():
            return -1 if is_max else 1

        if self.draw():
            return 0

        other_player = 'X' if player == 'O' else 'O'
        best_score = float('-inf') if is_max else float('inf')
        for i in range(9):
            if self.valid_move(i):
                self.board[i] = player if is_max else other_player
                score = self.minimax(not is_max, player)
                self.board[i] = ' '
                best_score = max(best_score, score) if is_max else min(
                    best_score, score)
        return best_score
    
    def best_move(self):
        best_score = float('-inf')
        move = 0
        for i in range(9):
            if self.valid_move(i):
                self.board[i] = self.current_player()
                score = self.minimax(False, self.current_player())
                self.board[i] = ' '

                if score > best_score:
                    best_score = score
                    move = i

        return move

    def move_ai(self):
        self.board[self.best_move()] = self.current_player()
        self.current_move += 1
        self.show_board()

    def move(self, player):
        if player == 'player':
            try:
                place = int(input('Where do you want to move?')) - 1
            except ValueError:
                print('Must be a number 1-9')
                return
            if place <= 8 and place >= 0 and self.valid_move(place):
                self.board[place] = self.current_player()
                self.current_move += 1
                self.show_board()
        else:
            self.move_ai()

    def valid_move(self, place):
        if self.board[place] == ' ':
            return True
        return False

    def valid_input(self, user_input):
        try:
            user_input = int(user_input) - 1
            return user_input <= 9 and user_input >= 1
        except ValueError:
            return False

    def current_player(self):
        return 'X' if self.current_move % 2 == 0 else 'O'

    def won(self):
        for combo in self.winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] and self.board[combo[0]] == self.board[combo[2]] and (self.board[combo[0]] == 'O' or self.board[combo[0]] == 'X'):
                return True
        return False

    def winner(self):
        return 'O' if self.current_player() == 'X' else 'X'

    def clear(self):
        self.__init__()

    def draw(self):
        return ' ' not in self.board and not self.won()

    def play(self):
        user_input = input('''Play - 1
Exit - 2
''')
        while user_input != '2':
            player_x = input('player or ai? ')
            player_o = input('player or ai? ')
            self.show_board()
            while True:
                player = self.current_player()
                if player == 'X':
                    self.move(player_x)
                else:
                    self.move(player_o)
                if self.won():
                    print(f'{self.winner()} won!')
                    self.clear()
                    break
                elif self.draw():
                    print('There is a draw')
                    self.clear()
                    break
            user_input = input('''Play - 1
Exit - 2
''')


idk = Tictactoe()
idk.play()
