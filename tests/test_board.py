# -*- coding: UTF-8 -*-

import unittest
from term2048.board import Board

_BSIZE = Board.SIZE

class TestBoard(unittest.TestCase):

    def setUp(self):
        Board.SIZE = _BSIZE
        self.b = Board()

    # == init == #
    def test_init_dimensions(self):
        self.assertEqual(len(self.b.cells), Board.SIZE)
        self.assertEqual(len(self.b.cells[0]), Board.SIZE)
        if Board.SIZE > 1:
            self.assertEqual(len(self.b.cells[1]), Board.SIZE)

    def test_init_dimensions_1(self):
        Board.SIZE = 1
        b = Board()
        self.assertEqual(b.cells, [[2]])

    def test_init_only_two_tiles(self):
        t = 0
        for x in xrange(Board.SIZE):
            for y in xrange(Board.SIZE):
                c = self.b.cells[y][x]
                if c == 2:
                    t += 1
                else:
                    self.assertEqual(c, 0, 'board[%d][%d] should be 0' % (y, x))

        self.assertEqual(t, 2)

    def test_init_not_won(self):
        self.assertFalse(self.b.won())

    def test_init_not_filled(self):
        self.assertFalse(self.b.filled())

    # == .won == #
    def test_won(self):
        self.b._Board__won = True
        self.assertTrue(self.b.won())
        self.b._Board__won = False
        self.assertFalse(self.b.won())

    # == .filled == #
    def test_filled(self):
        self.b.cells = [[1]*Board.SIZE for _ in xrange(Board.SIZE)]
        self.assertTrue(self.b.filled())

    # == .addTile == #
    def test_addTile(self):
        Board.SIZE = 1
        b = Board()
        b.cells = [[0]]
        b.addTile(value=42)
        self.assertEqual(b.cells[0][0], 42)

    # == .getCell == #
    def test_getCell(self):
        x, y = 3, 1
        v = 42
        self.b.cells[y][x] = v
        self.assertEqual(self.b.getCell(x, y), v)

    # == .getCell == #
    def test_getCellStr_empty(self):
        x, y = 3, 1
        self.b.cells[y][x] = 0
        self.assertEqual(self.b.getCellStr(x, y), '   .')

    def test_getCellStr_2(self):
        x, y = 3, 1
        self.b.cells[y][x] = 2
        self.assertEqual(self.b.getCellStr(x, y), '   2')

    def test_getCellStr_2048(self):
        x, y = 3, 1
        self.b.cells[y][x] = 2048
        self.assertEqual(self.b.getCellStr(x, y), '2048')

    # == .setCell == #
    def test_setCell(self):
        x, y = 2, 3
        v = 42
        self.b.setCell(x, y, v)
        self.assertEqual(self.b.cells[y][x], v)

    # == .getLine == #
    def test_getLine(self):
        Board.SIZE = 4
        b = Board()
        l = [42, 17, 12, 3]
        b.cells = [
            [0]*4,
            l,
            [0]*4,
            [0]*4
        ]
        self.assertSequenceEqual(b.getLine(1), l)

    # == .getCol == #
    def test_getLine(self):
        self.assertFalse(True) # TODO

    # == .setLine == #
    def test_setLine(self):
        i = 2
        l = [1, 2, 3, 4]
        self.b.setLine(i, l)
        self.assertEqual(self.b.getLine(i), l)

    # == .setCol == #
    def test_setLine(self):
        i = 2
        l = [1, 2, 3, 4]
        self.b.setCol(i, l)
        self.assertEqual(self.b.getCol(i), l)

    # == .getEmptyCells == #
    def test_getEmptyCells(self):
        self.assertFalse(True) # TODO

    def test_getEmptyCells_filled(self):
        self.assertFalse(True) # TODO

    # == .move == #
    def test_move(self):
        self.assertFalse(True) # TODO

    # == .__str__ == #
    def test_str(self):
        self.assertFalse(True) # TODO