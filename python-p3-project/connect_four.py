class Player:
    def __init__(self, name, symbol):
        self.name = name   
        self.symbol = symbol
    
    def __str__ (self):
        return self.name
    
    def __repr__(self) -> str:
        pass

class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)] #? Creates a board using nested for loops and a list comprehension
        self.players = [] #? contains the players
        self.current_player = None #? This will be changed after each move
        self.winner = None #? This will be set to the player who wins
        self.win = None #? Will be used to store the winning combination
        self.row = 6
        self.col = 7

    def reset_game(self): #? Resets the game by resetting the board, current player,  and winner, essentially a re-initialization
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = None
        self.winner = None
        self.win = None
        self.row = 6
        self.col = 7
        
    def add_player(self, player): #? Adds a player to the game
        self.players.append(player)

    def start_game(self): #? Starts the game by setting the current player to the first player in the list of players
        self.current_player = self.players[0]

    def print_board(self): #? Prints the board that was created 
        print("This is Connect four. choose A column to place your piece")
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def check_winner(self):
        #! Check rows for matches of 4
        for row in self.board:
            for i in range(0, len(row) - 3): #? Iterates through the row and checks for matches of 4
                if row[i] == row[i+1] == row[i+2] == row[i+3] != ' ': #? checks to make sure there is a match of 4 and that it's not an empty space
                    self.winner = self.current_player
                    return True

        #! Check columns for matches of 4
        for col in range(self.col):
            for i in range(0, self.row - 3): #? Iterates through the column and checks for matches of 4
                if self.board[i][col] == self.board[i+1][col] == self.board[i+2][col] == self.board[i+3][col] != ' ':
                    self.winner = self.current_player
                    return True

        #! Check diagonals for matches of 4
        for col in range(self.col - 3):
            for row in range(self.row - 3): #? Iterates through the diagonals and checks for matches of 4
                if (self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] != ' ' or
                    self.board[row][col+3] == self.board[row+1][col+2] == self.board[row+2][col+1] == self.board[row+3][col] != ' '):
                    self.winner = self.current_player
                    return True

        return False
    
    def is_board_full(self): #? Checks if the board is full, if it is then it's a tie
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def make_move(self, col): #? Makes a move by placing the player's symbol in the column they chose, it then alternates the current player
        for i in range(self.row-1,-1,-1):
            if self.board[i][col] == ' ':
                self.board[i][col] = self.current_player.symbol
                if self.check_winner():
                    self.winner = self.current_player
                self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1] #? Alternates the current player
                return True
        return False
    
    def play_again(self): #? Asks the players if they want to play again, if they do then the game is reset and started again using the start_game() method
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'yes':
            self.reset_game()
            self.start_game()
        elif play_again.lower() == 'no':
            print("Thank you for playing!")
            exit()
        else:
            print("Invalid input. Try again.")
            self.play_again()
            
    #? This is the main game loop. It prints the board, asks the player for a column, 
    #? makes a move, checks for a winner, checks if the board is full, and then asks if the players want to play again
    def play_game(self):

        while True: #? This loop will continue until the game is over, which case, the play_again() method will be called
            self.print_board()
            print(f"It's {self.current_player.name}'s({self.current_player.symbol}) turn.")
            try:
                col = int(input("Enter the column to place your piece: "))
            except ValueError:
                print("Invalid move. Try again.")
                continue
            if type(col) == str:
                print("Invalid move. Try again.")
                continue
            if not 0 <= col < self.col or not type(col)== int or not self.make_move(col): #? Checks if the column is valid and if the move was successful
                print("Invalid move. Try again.")
                continue #? If the move was not successful, the loop will continue
            if self.check_winner(): #? Checks if there is a winner
                self.print_board()
                print(f"{self.winner.name}({self.winner.symbol}) wins!")
            elif self.is_board_full():
                self.print_board()
                print("It's a tie!")
            else:
                continue
            self.play_again()

player1 = Player("Player 1", "X") #? Creates an instance of the Player class
player2 = Player("Player 2", "O") #? Creates an instance of the Player class

game = ConnectFour() #? Creates an instance of the ConnectFour class
#? Adds the players to the game
game.add_player(player1) 
game.add_player(player2)
#? Starts the game
game.start_game()
game.play_game()
