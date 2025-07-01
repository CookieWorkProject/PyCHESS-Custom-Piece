from main import move_piece, checkMate, staleMate, update_atrs
from classes import *


def test_checkMate():
    gs = Game_State()
    gs.board = [
    [Castle("../assets/images/bR.png", "black"), '--', Bishop("../assets/images/bB.png", "black"), '--', King("../assets/images/bK.png", "black"), '--', Knight("../assets/images/bN.png", "black"), Castle("../assets/images/bR.png", "black")],
    [Pawn("../assets/images/bp.png", "black"), Pawn("../assets/images/bp.png", "black"), Pawn("../assets/images/bp.png", "black"), Pawn("../assets/images/bp.png", "black"), Pawn("../assets/images/bp.png", "black"), '--', '--', Pawn("../assets/images/bp.png", "black")],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', Pawn("../assets/images/wp.png", "white"), '--',  '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', Queen("../assets/images/wQ.png", "white"), '--', '--', '--', Knight("../assets/images/wN.png", "white"), '--', '--'],
    [Pawn("../assets/images/wp.png", "white"), '--', Pawn("../assets/images/wp.png", "white"), '--', Pawn("../assets/images/wp.png", "white"), Pawn("../assets/images/wp.png", "white"), Pawn("../assets/images/wp.png", "white"), Pawn("../assets/images/wp.png", "white")],
    [Castle("../assets/images/wR.png", "white"), Knight("../assets/images/wN.png", "white"),Queen("../assets/images/bQ.png", "black"), '--', King("../assets/images/wK.png", "white"), Bishop("../assets/images/wB.png", "white"), '--', Castle("../assets/images/wR.png", "white")]
    ]

    update_atrs(gs)

    assert checkMate(gs, turn="white") == True
    printBoard(gs.board)


def test_move_piece():
    gs = Game_State()
    update_atrs(gs)
    assert move_piece([(6,0), (5,0)], gs, turn="white") == True


    gs = Game_State()
    gs.board = [
    [Castle("../assets/images/bR.png", "black"), '--', Bishop("../assets/images/bB.png", "black"), '--', King("../assets/images/bK.png", "black"), '--', Knight("../assets/images/bN.png", "black"), Castle("../assets/images/bR.png", "black")],
    [Pawn("../assets/images/bp.png", "black"), Pawn("../assets/images/bp.png", "black"), Pawn("../assets/images/bp.png", "black"), Pawn("../assets/images/bp.png", "black"), Pawn("../assets/images/bp.png", "black"), '--', '--', Pawn("../assets/images/bp.png", "black")],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', Pawn("../assets/images/wp.png", "white"), '--',  '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', Queen("../assets/images/wQ.png", "white"), '--', '--', '--', Knight("../assets/images/wN.png", "white"), '--', '--'],
    [Pawn("../assets/images/wp.png", "white"), '--', Pawn("../assets/images/wp.png", "white"), '--', Pawn("../assets/images/wp.png", "white"), Pawn("../assets/images/wp.png", "white"), Pawn("../assets/images/wp.png", "white"), Pawn("../assets/images/wp.png", "white")],
    [Castle("../assets/images/wR.png", "white"), Knight("../assets/images/wN.png", "white"),Queen("../assets/images/bQ.png", "black"), '--', King("../assets/images/wK.png", "white"), Bishop("../assets/images/wB.png", "white"), '--', Castle("../assets/images/wR.png", "white")]
    ]

    update_atrs(gs)

    assert move_piece([(7,4),(7,3)], gs, turn="white") == False
    printBoard(gs.board)


def test_staleMate():
    gs = Game_State()
    gs.board = [
    ['--' for n in range(8)],
    ['--' for n in range(8)],
    ['--' for n in range(8)],
    ['--' for n in range(8)],
    ['--' for n in range(8)],
    ['--' for n in range(8)],
    ['--', '--', '--', Queen("../assets/images/bQ.png", "black"), '--', '--', '--',  King("../assets/images/bK.png", "black")],
    ['--', '--','--', '--', '--', King("../assets/images/wK.png", "white"), '--', '--']
    ]
    update_atrs(gs)
    staleMate(gs, turn="white")
    printBoard(gs.board)
    
def printBoard(board):
    for a in board:
        for b in a:
            if type(b) is King:
                print("K", end="")
            elif type(b) is Queen:
                print("Q", end="")
            elif type(b) is Knight:
                print("N", end="")
            elif type(b) is Bishop:
                print("B", end="")
            elif type(b) is Castle:
                print("R", end="")
            else:
                print("-", end="")
        print("")
    print("")
if __name__ == "__main__":
    test_checkMate()
    test_move_piece()
    test_staleMate()