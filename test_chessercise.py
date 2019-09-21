from chessercise import calc_moves_knight, calc_moves_queen, calc_moves_rook


def test_knight():
    # Test knight output from space d2
    expected_moves = ['b1', 'f1', 'b3', 'f3', 'c4', 'e4']
    assert len(expected_moves) == len(calc_moves_knight(4, 2))
    assert set(expected_moves) == set(calc_moves_knight(4, 2))

def test_rook():
    # Test Rook output from space d2
    expected_moves = ['d1', 'a2', 'b2', 'c2', 'e2', 'f2', 'g2', 'h2', 'd3' ,'d4' ,'d5', 'd6', 'd7', 'd8']
    assert len(expected_moves) == len(calc_moves_rook(4, 2))
    assert set(expected_moves) == set(calc_moves_rook(4, 2))

def test_queen():
    # Test Queen output from space d2
    expected_moves = ['c1', 'd1', 'e1', 'a2', 'b2', 'c2', 'e2', 'f2', 'g2', 'h2', 'c3', 'd3', 'e3' ,'b4', 'd4', 'f4', 'a5', 'd5', 'g5', 'd6', 'h6', 'd7', 'd8']
    print(calc_moves_queen(4, 2))
    print(expected_moves)

    print(len(expected_moves), len(calc_moves_queen(4, 2)))
    assert len(expected_moves) == len(calc_moves_queen(4, 2))
    assert set(expected_moves) == set(calc_moves_queen(4, 2))

