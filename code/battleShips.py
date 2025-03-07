import numpy as np
      
class board():
    def __init__(self):
        self.scale = 10
        self.playerBoard = np.full((self.scale,self.scale),None,dtype=object)
    
    def returnArray(self):
        return self.playerBoard 
       
    
class carrier(board):
    def __init__(self):
        super().__init__()
        self.length = 5
        self.identifier = "CA"
        
    def placeOnBoard(self, initialRotation, x, y):
        # Make a copy of the board before making changes
        dupeBoard = self.playerBoard.copy()
        
        # Attempt to place the ship
        temp = 1
        try:
            self.playerBoard[y, x] = self.identifier
            while temp != self.length:
                if initialRotation == "V":
                    if y + temp >= self.scale or self.playerBoard[y + temp, x] is not None:
                        # Revert to the original board if an issue occurs
                        self.playerBoard = dupeBoard
                        raise ValueError("There is a ship here already or out of bounds.")
                    else:    
                        self.playerBoard[y + temp, x] = self.identifier
                        temp += 1
                elif initialRotation == "H":
                    if x + temp >= self.scale or self.playerBoard[y, x + temp] is not None:
                        # Revert to the original board if an issue occurs
                        self.playerBoard = dupeBoard
                        raise ValueError("There is a ship here already or out of bounds.")
                    else:    
                        self.playerBoard[y, x + temp] = self.identifier
                        temp += 1

            print(self.playerBoard)  #? Debug: Print the board after placement
            return self.playerBoard
        except ValueError as e:
            print(e)
            return dupeBoard  # Return the original board if placement fails

    def returnIdentifier(self):
        return self.identifier
                
class battleship(board):
    def __init__(self):
        super().__init__()
        self.length = 4
        self.identifier = "BA"
        
    def placeOnBoard(self, initialRotation, x, y):
        # Make a copy of the board before making changes
        dupeBoard = self.playerBoard.copy()
        
        # Attempt to place the ship
        temp = 1
        try:
            self.playerBoard[y, x] = self.identifier
            while temp != self.length:
                if initialRotation == "V":
                    if y + temp >= self.scale or self.playerBoard[y + temp, x] is not None:
                        # Revert to the original board if an issue occurs
                        self.playerBoard = dupeBoard
                        raise ValueError("There is a ship here already or out of bounds.")
                    else:    
                        self.playerBoard[y + temp, x] = self.identifier
                        temp += 1
                elif initialRotation == "H":
                    if x + temp >= self.scale or self.playerBoard[y, x + temp] is not None:
                        # Revert to the original board if an issue occurs
                        self.playerBoard = dupeBoard
                        raise ValueError("There is a ship here already or out of bounds.")
                    else:    
                        self.playerBoard[y, x + temp] = self.identifier
                        temp += 1

            print(self.playerBoard)  # Debug: Print the board after placement
            return self.playerBoard
        except ValueError as e:
            print(e)
            return dupeBoard  # Return the original board if placement fails
   
    def returnIdentifier(self):
        return self.identifier 
        
class Submarine(board):
    def __init__(self):
        super().__init__()
        self.length = 3  
        self.identifier = "SU"  
        
    def placeOnBoard(self, initialRotation, x, y):
        # Make a copy of the board before making changes
        dupeBoard = self.playerBoard.copy()
        
        # Attempt to place the ship
        temp = 1
        try:
            self.playerBoard[y, x] = self.identifier
            while temp != self.length:
                if initialRotation == "V":
                    if y + temp >= self.scale or self.playerBoard[y + temp, x] is not None:
                        # Revert to the original board if an issue occurs
                        self.playerBoard = dupeBoard
                        raise ValueError("There is a ship here already or out of bounds.")
                    else:    
                        self.playerBoard[y + temp, x] = self.identifier
                        temp += 1
                elif initialRotation == "H":
                    if x + temp >= self.scale or self.playerBoard[y, x + temp] is not None:
                        # Revert to the original board if an issue occurs
                        self.playerBoard = dupeBoard
                        raise ValueError("There is a ship here already or out of bounds.")
                    else:    
                        self.playerBoard[y, x + temp] = self.identifier
                        temp += 1

            print(self.playerBoard)  # Debug: Print the board after placement
            return self.playerBoard
        except ValueError as e:
            print(e)
            return dupeBoard  # Return the original board if placement fails

    def returnIdentifier(self):
        return self.identifier

class crusier(board):
    def __init__(self):
        super().__init__()
        self.length = 3
        self.identifier = "CR"
        
    def placeOnBoard(self, initialRotation, x, y):
        # Make a copy of the board before making changes
        dupeBoard = self.playerBoard.copy()
        
        # Attempt to place the ship
        temp = 1
        try:
            self.playerBoard[y, x] = self.identifier
            while temp != self.length:
                if initialRotation == "V":
                    if y + temp >= self.scale or self.playerBoard[y + temp, x] is not None:
                        # Revert to the original board if an issue occurs
                        self.playerBoard = dupeBoard
                        raise ValueError("There is a ship here already or out of bounds.")
                    else:    
                        self.playerBoard[y + temp, x] = self.identifier
                        temp += 1
                elif initialRotation == "H":
                    if x + temp >= self.scale or self.playerBoard[y, x + temp] is not None:
                        # Revert to the original board if an issue occurs
                        self.playerBoard = dupeBoard
                        raise ValueError("There is a ship here already or out of bounds.")
                    else:    
                        self.playerBoard[y, x + temp] = self.identifier
                        temp += 1

            print(self.playerBoard)  # Debug: Print the board after placement
            return self.playerBoard
        except ValueError as e:
            print(e)
            return dupeBoard  # Return the original board if placement fails

    def returnIdentifier(self):
        return self.identifier 
        
class destroyer(board):
    def __init__(self):
        super().__init__()
        self.length = 2  
        self.identifier = "DE"             
    
    def placeOnBoard(self, initialRotation, x, y):
        # Make a copy of the board before making changes
        dupeBoard = self.playerBoard.copy()
        
        # Attempt to place the ship
        temp = 1
        try:
            self.playerBoard[y, x] = self.identifier
            while temp != self.length:
                if initialRotation == "V":
                    if y + temp >= self.scale or self.playerBoard[y + temp, x] is not None:
                        # Revert to the original board if an issue occurs
                        self.playerBoard = dupeBoard
                        raise ValueError("There is a ship here already or out of bounds.")
                    else:    
                        self.playerBoard[y + temp, x] = self.identifier
                        temp += 1
                elif initialRotation == "H":
                    if x + temp >= self.scale or self.playerBoard[y, x + temp] is not None:
                        # Revert to the original board if an issue occurs
                        self.playerBoard = dupeBoard
                        raise ValueError("There is a ship here already or out of bounds.")
                    else:    
                        self.playerBoard[y, x + temp] = self.identifier
                        temp += 1

            print(self.playerBoard)  # Debug: Print the board after placement
            return self.playerBoard
        except ValueError as e:
            print(e)
            return dupeBoard  # Return the original board if placement fails
  
    def returnIdentifier(self):
        return self.identifier    
