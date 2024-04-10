#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import itertools

WHITE = "white"
BLACK = "black"


class Game:

    def __init__(self):
        self.playersturn = BLACK
        self.message = "Сделайте ход"
        self.gameboard = {}
        self.placePieces()
        print("шахматная программа. введите ходы в алгебраической записи, разделенные пробелом")
        self.main()

    def placePieces(self):

        for i in range(0, 8):
            self.gameboard[(i, 1)] = Pawn(WHITE, uniDict[WHITE][Pawn], 1)
            self.gameboard[(i, 6)] = Pawn(BLACK, uniDict[BLACK][Pawn], -1)

        placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(0, 8):
            self.gameboard[(i, 0)] = placers[i](WHITE, uniDict[WHITE][placers[i]])
            self.gameboard[((7 - i), 7)] = placers[i](BLACK, uniDict[BLACK][placers[i]])
        placers.reverse()

    def main(self):

        while True:
            self.printBoard()
            print(self.message)
            self.message = ""
            startpos, endpos = self.parseInput()
            try:
                target = self.gameboard[startpos]
            except:
                self.message = "не удалось найти фигуру; индекс, вероятно, вне допустимого диапазона"
                target = None

            if target:
                print("Найден " + str(target))
                if target.Color != self.playersturn:
                    self.message = "вам не разрешено перемещать эту фигуру в этот ход"
                    continue
                if target.isValid(startpos, endpos, target.Color, self.gameboard):
                    self.message = "это правильный ход"
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]
                    self.isCheck()
                    if self.playersturn == BLACK:
                        self.playersturn = WHITE
                    else:
                        self.playersturn = BLACK
                else:
                    self.message = "неверный ход" + str(target.availableMoves(startpos[0], startpos[1], self.gameboard))
                    print(target.availableMoves(startpos[0], startpos[1], self.gameboard))
            else:
                self.message = "в этом пространстве нет фигур"

    def isCheck(self):
        # выясните, где находятся короли, проверьте все фигуры противоположного цвета против этих королей, а затем, если кто-то из них получит удар, проверьте, не поставил ли он мат
        king = King
        kingDict = {}
        pieceDict = {BLACK: [], WHITE: []}
        for position, piece in self.gameboard.items():
            if type(piece) == King:
                kingDict[piece.Color] = position
            print(piece)
            pieceDict[piece.Color].append((piece, position))
        # white
        if self.canSeeKing(kingDict[WHITE], pieceDict[BLACK]):
            self.message = "Белый игрок находится под шахом"
        if self.canSeeKing(kingDict[BLACK], pieceDict[WHITE]):
            self.message = "Черный игрок находится под шахом"

    def canSeeKing(self, kingpos, piecelist):
        # проверяет, могут ли какие-либо фигуры в списке фигур (который представляет собой массив кортежей (фигуры, позиций)) увидеть короля в kingpos
        for piece, position in piecelist:
            if piece.isValid(position, kingpos, piece.Color, self.gameboard):
                return True

    def parseInput(self):
        try:
            a, b = input().split()
            a = ((ord(a[0]) - 97), int(a[1]) - 1)
            b = (ord(b[0]) - 97, int(b[1]) - 1)
            print(a, b)
            return (a, b)
        except:
            print("ошибка декодирования ввода. Пожалуйста, попробуйте еще раз")
            return ((-1, -1), (-1, -1))

   

    def printBoard(self):
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(0, 8):
            print("-" * 32)
            print(chr(i + 97), end="|")
            for j in range(0, 8):
                item = self.gameboard.get((i, j), " ")
                print(str(item) + ' |', end = " ")
            print()
        print("-" * 32)

    """класс игры. содержит следующие члены и методы:
    два массива фигур для каждого игрока
    Массив фрагментов 8x8 со ссылками на эти фрагменты
    функция разбора, которая превращает ввод пользователя в список из двух кортежей, обозначающих начальную и конечную точки
    функция checkmateExists, которая проверяет, поставил ли кто-либо из игроков мат
    функция checkExists, которая проверяет, находится ли кто-либо из игроков под шахом
    основной цикл, который принимает входные данные, пропускает их через синтаксический анализатор, спрашивает фигуру, допустимо ли движение, и перемещает фигуру, если это так. если ход конфликтует с другой фигурой, эта фигура удаляется. ischeck(mate) запускается, и если есть мат, игра выводит сообщение о том, кто выиграл"""


class Piece:

    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.Color = color

    def isValid(self, startpos, endpos, Color, gameboard):
        if endpos in self.availableMoves(startpos[0], startpos[1], gameboard, Color=Color):
            return True
        return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def availableMoves(self, x, y, gameboard):
        print("ОШИБКА: нет движения для базового класса")

    def AdNauseum(self, x, y, gameboard, Color, intervals):
        """повторяет заданный интервал до тех пор, пока не будет достигнута другая часть.
        если эта часть не того же цвета, этот квадрат добавляется и
         то список возвращается"""
        answers = []
        for xint, yint in intervals:
            xtemp, ytemp = x + xint, y + yint
            while self.isInBounds(xtemp, ytemp):
                

                target = gameboard.get((xtemp, ytemp), None)
                if target is None:
                    answers.append((xtemp, ytemp))
                elif target.Color != Color:
                    answers.append((xtemp, ytemp))
                    break
                else:
                    break

                xtemp, ytemp = xtemp + xint, ytemp + yint
        return answers

    def isInBounds(self, x, y):
        "проверяет, есть ли позиция на доске"
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    def noConflict(self, gameboard, initialColor, x, y):
        "проверяет, не противоречит ли одна позиция правилам шахмат"
        if self.isInBounds(x, y) and (((x, y) not in gameboard) or gameboard[(x, y)].Color != initialColor): return True
        return False


chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]


def knightList(x, y, int1, int2):
    """специально для ладьи, переставляет значения, необходимые вокруг позиции для тестов noConflict"""
    return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2),
            (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]


def kingList(x, y):
    return [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y), (x - 1, y + 1),
            (x - 1, y - 1)]


class Knight(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return [(xx, yy) for xx, yy in knightList(x, y, 2, 1) if self.noConflict(gameboard, Color, xx, yy)]


class Rook(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals)


class Bishop(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessDiagonals)


class Queen(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals + chessDiagonals)


class King(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return [(xx, yy) for xx, yy in kingList(x, y) if self.noConflict(gameboard, Color, xx, yy)]


class Pawn(Piece):
    def __init__(self, color, name, direction):
        self.name = name
        self.Color = color
        # конечно, самую маленькую часть кодировать труднее всего. Направление должно быть либо 1, либо -1, должно быть -1, если пешка движется "назад"
        self.direction = direction

    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        answers = []
        if (x + 1, y + self.direction) in gameboard and self.noConflict(gameboard, Color, x + 1,
                                                                        y + self.direction): answers.append(
            (x + 1, y + self.direction))
        if (x - 1, y + self.direction) in gameboard and self.noConflict(gameboard, Color, x - 1,
                                                                        y + self.direction): answers.append(
            (x - 1, y + self.direction))
        if (x, y + self.direction) not in gameboard and Color == self.Color: answers.append((x,
                                                                                             y + self.direction))  # условие после и состоит в том, чтобы убедиться, что движение без взятия не используется при расчете мата
        return answers


uniDict = {WHITE: {Pawn: "P", Rook: "R", Knight: "N", Bishop: "B", King: "K", Queen: "Q"},
           BLACK: {Pawn: "p", Rook: "r", Knight: "n", Bishop: "b", King: "k", Queen: "q"}}

Game()


# # WHITE = "white"
# BLACK = "black"
# 
# class Chessboard:
# 
#     def __init__(self):
#         self.gameboard = {}
#         self.placePieces()
# 
#     def placePieces(self):
#         for i in range(0, 8):
#             self.gameboard[(i, 1)] = Pawn(WHITE, uniDict[WHITE][Pawn], 1)
#             self.gameboard[(i, 6)] = Pawn(BLACK, uniDict[BLACK][Pawn], -1)
# 
#         placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
# 
#         for i in range(0, 8):
#             self.gameboard[(i, 0)] = placers[i](WHITE, uniDict[WHITE][placers[i]])
#             self.gameboard[((7 - i), 7)] = placers[i](BLACK, uniDict[BLACK][placers[i]])
#         placers.reverse()
# 
#     def printBoard(self):
#         print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
#         for i in range(0, 8):
#             print("-" * 32)
#             print(chr(i + 97), end="|")
#             for j in range(0, 8):
#                 item = self.gameboard.get((i, j), " ")
#                 print(str(item) + ' |', end=" ")
#             print()
#         print("-" * 32)
# 
# 
# class Piece:
# 
#     def __init__(self, color, name):
#         self.name = name
#         self.position = None
#         self.Color = color
# 
#     def __repr__(self):
#         return self.name
# 
#     def __str__(self):
#         return self.name
# 
# 
# class Pawn(Piece):
# 
#     def __init__(self, color, name, direction):
#         self.name = name
#         self.Color = color
#         self.direction = direction
# 
# 
# class Rook(Piece):
# 
#     def availableMoves(self, x, y, gameboard, Color=None):
#         return []
# 
# 
# class Knight(Piece):
# 
#     def availableMoves(self, x, y, gameboard, Color=None):
#         return []
# 
# 
# class Bishop(Piece):
# 
#     def availableMoves(self, x, y, gameboard, Color=None):
#         return []
# 
# 
# class Queen(Piece):
# 
#     def availableMoves(self, x, y, gameboard, Color=None):
#         return []
# 
# 
# class King(Piece):
# 
#     def availableMoves(self, x, y, gameboard, Color=None):
#         return []
# 
# 
# uniDict = {WHITE: {Pawn: "P", Rook: "R", Knight: "N", Bishop: "B", King: "K", Queen: "Q"},
#            BLACK: {Pawn: "p", Rook: "r", Knight: "n", Bishop: "b", King: "k", Queen: "q"}}
# 
# chessboard = Chessboard()
# chessboard.printBoard()
# 

# In[ ]:




