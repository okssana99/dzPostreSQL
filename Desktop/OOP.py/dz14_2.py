class ChessPiece:
    def __init__(self, color: str, position: tuple[int, int]):
        self.color = color
        self.position = position
    
    def change_color(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"
    
    def change_position(self, x: int, y: int):
        if self._is_valid_position(x, y):
            self.position = (x, y)
        else:
            print("Invalid position")
    
    def _is_valid_position(self, x: int, y: int) -> bool:
        return 0 <= x <= 7 and 0 <= y <= 7
    
    def check_potential_move(self, x: int, y: int) -> bool:
        pass

class Pawn(ChessPiece):
    def check_potential_move(self, x: int, y: int) -> bool:
        # Пішак може рухатися тільки вперед на одну клітинку
        return (self.position[0] == x and 
                (y == self.position[1] + 1 or 
                 (self.color == "white" and y == self.position[1] + 2)))
        

class Knight(ChessPiece):
    def check_potential_move(self, x: int, y: int) -> bool:
        # Кінь може рухатися "L" - дві клітинки в одному напрямку і одна в перпендикулярному
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)


class Bishop(ChessPiece):
    def check_potential_move(self, x: int, y: int) -> bool:
        # Офіцер може рухатися по діагоналі
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return dx == dy


class Rook(ChessPiece):
    def check_potential_move(self, x: int, y: int) -> bool:
        # Тура може рухатися по вертикалі або горизонталі
        return x == self.position[0] or y == self.position[1]


class Queen(ChessPiece):
    def check_potential_move(self, x: int, y: int) -> bool:
        # Ферзь може рухатися по вертикалі, горизонталі або діагоналі
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return (x == self.position[0] or y == self.position[1] or dx == dy)


class King(ChessPiece):
    def check_potential_move(self, x: int, y: int) -> bool:
        # Король може рухатися на одну клітинку у будь-якому напрямку
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return dx <= 1 and dy <= 1

def get_possible_moves(pieces: list[ChessPiece], x: int, y: int) -> list[ChessPiece]:
    possible_moves = []
    for piece in pieces:
        if piece.check_potential_move(x, y):
            possible_moves.append(piece)
    return possible_moves
