class Board:
    """
    This is the actual board implementation.
    It holds token collection and handles all the game logic.
    """

    def __init__(self):
        self.size = 8
        self.board = [-1] * 64

    def get_token(self, x, y):
        """
        Retrieves the token at given board coordinates
        :param x: x coordinate
        :param y: y coordinate
        :return: -1 for no token, else player index
        """
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            raise Exception(f"Wrong coordinate for token: {x}, {y}")

        return self.board[y * self.size + x]

    def set_token(self, x, y, value):
        """
        Sets the token at given board coordinates without checking game logic
        :param x: x coordinate
        :param y: y coordinate
        :param value: -1 for no token, else player index
        """
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            raise Exception(f"Wrong coordinate for token: {x}, {y}")

        self.board[y * self.size + x] = value

    def set_start_position(self):
        """
        Initialises the board in a starting game position.
        :return:
        """
        self.board = [-1] * 64
        self.set_token(3, 3, 0)
        self.set_token(4, 4, 0)
        self.set_token(3, 4, 1)
        self.set_token(4, 3, 1)