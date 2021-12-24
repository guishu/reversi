from unittest import TestCase
from unittest.mock import patch

from model.board import Board, TOKEN_CREATED_EVENT, TOKEN_SWITCHED_EVENT


@patch("pygame.event.post")
class BoardTests(TestCase):
    def test_get_token_bounds(self, post):
        board = Board()
        board.board = [1] * 64

        self.assertEqual(board.get_token(8, 8), -1)
        self.assertEqual(board.get_token(7, 7), 1)
        self.assertEqual(board.get_token(8, 7), -1)
        self.assertEqual(board.get_token(7, 8), -1)
        self.assertEqual(board.get_token(-1, -1), -1)
        self.assertEqual(board.get_token(0, 0), 1)
        self.assertEqual(board.get_token(-1, 0), -1)
        self.assertEqual(board.get_token(0, -1), -1)

    def test_get_token(self, post):
        board = Board()
        board.set_start_position()
        self.assertEqual(board.get_token(3, 3), 0)
        self.assertEqual(board.get_token(1, 2), -1)
        self.assertEqual(board.get_token(3, 4), 1)

    def test_set_token_bounds(self, post):
        board = Board()

        with self.assertRaises(Exception):
            board.set_token(-1, -1, 0)
        with self.assertRaises(Exception):
            board.set_token(8, 8, 0)
        with self.assertRaises(Exception):
            board.set_token(-1, 0, 0)
        with self.assertRaises(Exception):
            board.set_token(7, 8, 0)

        post.assert_not_called()

    def test_create_token(self, post):
        board = Board()
        board.board = [-1] * 64

        board.set_token(2, 3, 0)

        post.assert_called_once()
        event = post.call_args[0][0]

        self.assertEqual(event.type, TOKEN_CREATED_EVENT)

        self.assertEqual(board.get_token(2, 3), 0)
        self.assertEqual(board.get_token(3, 3), -1)
        self.assertEqual(board.get_token(2, 2), -1)

    def test_switch_token(self, post):
        board = Board()
        board.board = [1] * 64

        board.set_token(2, 3, 0)

        post.assert_called_once()
        event = post.call_args[0][0]

        self.assertEqual(event.type, TOKEN_SWITCHED_EVENT)

        self.assertEqual(board.get_token(2, 3), 0)
