class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Checkers:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.players = []
        self.current_player = None
        self.winner = None

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        self.current_player = self.players[0]
        self.fill_board()

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 17)

    def check_winner(self):
        for player in self.players:
            if not any(player.symbol in row for row in self.board):
                self.winner = self.players[0] if player == self.players[1] else self.players[1]
                return True
        return False

    def move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        if self.board[start_row][start_col] == self.current_player.symbol and self.board[end_row][end_col] == ' ':
            self.board[start_row][start_col] = ' '
            self.board[end_row][end_col] = self.current_player.symbol
            self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1]

    def fill_board(self):
        for i in range(8):
            for j in range(8):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                    self.board[i][j] = self.players[0].symbol if i < 3 else (self.players[1].symbol if i > 4 else ' ')

player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")

game = Checkers()
game.add_player(player1)
game.add_player(player2)
game.start_game()

while not game.check_winner():
    game.print_board()
    print(f"It's {game.current_player.name}'s({game.current_player.symbol}) turn.")
    start = tuple(map(int, input("Enter the starting position (row, col): ").split(',')))
    end = tuple(map(int, input("Enter the ending position (row, col): ").split(',')))
    game.move(start, end)

game.print_board()
print(f"Game over! {game.winner.name} wins!")