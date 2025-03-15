import numpy as np
      
class board():
    def __init__(self):
        self.scale = 10
    
    def returnArray(self):
        return self.playerBoard
    
    def createBoard(self):
        temp = np.full((self.scale,self.scale),None)
        return temp
    
    def shoot(self,y,x,board,player):
        
        if not np.isin(board, ["CA", "BA", "SU", "CR", "DE"]).any():
            return "gameOver"
        
        else:
            if board[x,y] is not None and board[x,y] != "X" and board[x,y] != "O":
                board[x,y] = "X"
                
            elif board[x,y] is None and board[x,y] != "X" and board[x,y] != "O":
                board[x,y] = "O"   
                
            else:
                pass         
                
            print(player + ":","\n\n",board)
            return board
          
class carrier(board):
    def __init__(self,board):
        super().__init__()
        self.length = 5
        self.identifier = "CA"
        self.playerBoard = board
          
    def placeOnBoard(self, initialRotation, x, y):
        
        # Attempt to place the ship
        temp = 1
        if x <= (self.scale-1) - self.length or y <= (self.scale-1) - self.length:
            self.playerBoard[y, x] = self.identifier
            while temp != self.length:
                if initialRotation == "V":
                    if y + temp >= self.scale or self.playerBoard[y + temp, x] is not None:
                        # Revert to the original board if an issue occurs
                        """self.playerBoard = np.copy(dupeBoard)
                        raise ValueError("There is a ship here already or out of bounds.")"""
                        pass
                    else:    
                        self.playerBoard[y + temp, x] = self.identifier
                        temp += 1
                elif initialRotation == "H":
                    if x + temp >= self.scale or self.playerBoard[y, x + temp] is not None:
                        # Revert to the original board if an issue occurs
                        """self.playerBoard = np.copy(dupeBoard)
                        raise ValueError("There is a ship here already or out of bounds.")"""
                        pass
                    else:    
                        self.playerBoard[y, x + temp] = self.identifier
                        temp += 1

            #print(self.playerBoard)  # Debug: Print the board after placement
            return self.playerBoard
        else:
            return "error"
        
    def returnIdentifier(self):
        return self.identifier
                
class battleship(board):
    def __init__(self,board):
        super().__init__()
        self.length = 4
        self.identifier = "BA"
        self.playerBoard = board
        
    def placeOnBoard(self, initialRotation, x, y):
        
        # Attempt to place the ship
        temp = 1
        try:
            self.playerBoard[y, x] = self.identifier
            while temp != self.length:
                if initialRotation == "V":
                    if y + temp >= self.scale or self.playerBoard[y + temp, x] is not None:
                        # Revert to the original board if an issue occurs
                        """self.playerBoard = np.copy(dupeBoard)
                        raise ValueError("There is a ship here already or out of bounds.")"""
                        pass
                    else:    
                        self.playerBoard[y + temp, x] = self.identifier
                        temp += 1
                elif initialRotation == "H":
                    if x + temp >= self.scale or self.playerBoard[y, x + temp] is not None:
                        # Revert to the original board if an issue occurs
                        """self.playerBoard = np.copy(dupeBoard)
                        raise ValueError("There is a ship here already or out of bounds.")"""
                        pass
                    else:    
                        self.playerBoard[y, x + temp] = self.identifier
                        temp += 1

            #print(self.playerBoard)  # Debug: Print the board after placement
            return self.playerBoard
        except:
            return "error"
        
    def returnIdentifier(self):
        return self.identifier 
        
class Submarine(board):
    def __init__(self,board):
        super().__init__()
        self.length = 3  
        self.identifier = "SU"  
        self.playerBoard = board
        
    def placeOnBoard(self, initialRotation, x, y):
        
        # Attempt to place the ship
        temp = 1
        try:
            self.playerBoard[y, x] = self.identifier
            while temp != self.length:
                if initialRotation == "V":
                    if y + temp >= self.scale or self.playerBoard[y + temp, x] is not None:
                        # Revert to the original board if an issue occurs
                        """self.playerBoard = np.copy(dupeBoard)
                        raise ValueError("There is a ship here already or out of bounds.")"""
                        pass
                    else:    
                        self.playerBoard[y + temp, x] = self.identifier
                        temp += 1
                elif initialRotation == "H":
                    if x + temp >= self.scale or self.playerBoard[y, x + temp] is not None:
                        # Revert to the original board if an issue occurs
                        """self.playerBoard = np.copy(dupeBoard)
                        raise ValueError("There is a ship here already or out of bounds.")"""
                        pass
                    else:    
                        self.playerBoard[y, x + temp] = self.identifier
                        temp += 1

            #print(self.playerBoard)  # Debug: Print the board after placement
            return self.playerBoard
        except:
            return "error"

    def returnIdentifier(self):
        return self.identifier

class crusier(board):
    def __init__(self,board):
        super().__init__()
        self.length = 3
        self.identifier = "CR"
        self.playerBoard = board
        
    def placeOnBoard(self, initialRotation, x, y):
        
        # Attempt to place the ship
        temp = 1
        
        print(self.playerBoard)  # Debug: Print the board after placement
        try:
            self.playerBoard[y, x] = self.identifier
            while temp != self.length:
                if initialRotation == "V":
                    if y + temp >= self.scale or self.playerBoard[y + temp, x] is not None:
                        return "error"
                    else:    
                        self.playerBoard[y + temp, x] = self.identifier
                        temp += 1
                elif initialRotation == "H":
                    if x + temp >= self.scale or self.playerBoard[y, x + temp] is not None:
                        return "error"
                    else:    
                        self.playerBoard[y, x + temp] = self.identifier
                        temp += 1

            print(self.playerBoard)  # Debug: Print the board after placement
            return self.playerBoard
        except:
            return "error"
        
    def returnIdentifier(self):
        return self.identifier 
        
class destroyer(board):
    def __init__(self,board):
        super().__init__()
        self.length = 2  
        self.identifier = "DE" 
        self.playerBoard = board            
    
    def placeOnBoard(self, initialRotation, x, y):
        
        # Attempt to place the ship
        temp = 1
        try:
            self.playerBoard[y, x] = self.identifier
            while temp != self.length:
                if initialRotation == "V":
                    if y + temp >= self.scale or self.playerBoard[y + temp, x] is not None:
                        # Revert to the original board if an issue occurs
                        """self.playerBoard = np.copy(dupeBoard)
                        raise ValueError("There is a ship here already or out of bounds.")"""
                        pass
                    else:    
                        self.playerBoard[y + temp, x] = self.identifier
                        temp += 1
                elif initialRotation == "H":
                    if x + temp >= self.scale or self.playerBoard[y, x + temp] is not None:
                        # Revert to the original board if an issue occurs
                        """self.playerBoard = np.copy(dupeBoard)
                        raise ValueError("There is a ship here already or out of bounds.")"""
                        pass
                    else:    
                        self.playerBoard[y, x + temp] = self.identifier
                        temp += 1

            #print(self.playerBoard)  # Debug: Print the board after placement
            return self.playerBoard
        except:
            return "error"
          # Return the original board if placement fails
  
    def returnIdentifier(self):
        return self.identifier    

