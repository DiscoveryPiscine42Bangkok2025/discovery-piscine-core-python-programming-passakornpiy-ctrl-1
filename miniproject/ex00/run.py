#!/usr/bin/env python3

# # # This is probably an excessive amount of comments but I figured I should explain it right now so I don't stutter later. -ppiyayop

def checkKing(stri, piece, pos, lineCount):
    # Find if the king is in check
    match (piece):
        case 'P':
            checkPos = pos - lineCount
            if (checkPos < 0):
                return False
            if (stri[checkPos- 1] == "K" or stri[checkPos + 1] == "K" ):
                # print("pawn")
                return True
        case 'B':
            inCheck = checkDiagonal(stri, lineCount, pos)
            # if (inCheck): print("bishop")
            return inCheck
        case 'R':
            inCheck = checkVertical(stri, lineCount, pos) or checkHorizontal(stri, lineCount, pos)
            # if (inCheck): print("rook")
            return inCheck
        case 'Q':
            inCheck = checkVertical(stri, lineCount, pos) or checkHorizontal(stri, lineCount, pos) or checkDiagonal(stri, lineCount, pos)
            # if (inCheck): print("queen")
            return inCheck
    return False

def checkDiagonal(stri, lineCount, pos): # # idk how this works i just winged it
    for i in range(1, lineCount):
        upperCell = pos - (lineCount * i)
        lowerCell = pos + (lineCount * i)
        upCheck1 = upperCell - i # # # Up left
        upCheck2 = upperCell + i # # # Up right
        lowCheck1 = lowerCell - i # # # Down left
        lowCheck2 = lowerCell + i # # # Down right
        # # # Prevent from checking different columns
        noLessThanUp = (upperCell // lineCount) * lineCount
        noMoreThanUp = (upperCell // lineCount + 1) * lineCount
        noLessThanLow = (lowerCell // lineCount) * lineCount
        noMoreThanLow = ((lowerCell // lineCount) + 1) * lineCount
        # print(lineCount * lineCount, "i", i, "lines",  lineCount, "upper", upperCell, "lower", lowerCell, "up check", upCheck1, upCheck2, noLessThanUp, noMoreThanUp, "low check", lowCheck1, lowCheck2, noLessThanLow, noMoreThanLow)
        if (noLessThanUp >= 0 and upCheck1 >= noLessThanUp and upCheck1 < noMoreThanUp and stri[upCheck1] == "K"):
            # print("UPCHECK1", upCheck1)
            return True
        if (noLessThanUp >= 0 and upCheck2 >= noLessThanUp and upCheck2 < noMoreThanUp and stri[upCheck2] == "K"):
            # print("UPCHECK2", upCheck2)
            return True
        if (noMoreThanLow <= lineCount * lineCount and lowCheck1 < noMoreThanLow and lowCheck1 >= noLessThanLow and stri[lowCheck1] == "K"):
            # print("LOWCHECK1", lowCheck1)
            return True
        if (noMoreThanLow <= lineCount * lineCount and lowCheck2 < noMoreThanLow and lowCheck2 >= noLessThanLow and stri[lowCheck2] == "K"):
            # print("LOWCHECK2", lowCheck2)
            return True
    return False

def checkHorizontal(stri, lineCount, pos):
    column = (pos) // lineCount
    for i in range(lineCount):
        checking = (column * lineCount) + i
        # print(column, checking)
        if (stri[checking] == "K"):
            # print("horizontal")
            return True
    return False

def checkVertical(stri, lineCount, pos): # i fucked this up big time yet it works??
    for i in range(lineCount):
        checkPos = (lineCount * i) + (pos % lineCount)
        # print(checkPos)
        if (checkPos <= (lineCount * i) + (pos % lineCount) and stri[checkPos] == "K"):
            # print("-", checkPos)
            return True
    return False

def checkmate(stri):
    # # # Checking if it's a square
    lineCount = (stri.count(("""
""")) + 1)
    letterCount = len(stri) - lineCount + 1
    if (lineCount * lineCount != letterCount):
        print("This is not a square. Please input an actual square.")
        return
    
    # # # Making the board a straight line
    board = stri.replace("""
""", "")
    # # # Find a check.
    inCheck = False
    for index in range(len(board)):
        # print(board[index], index)
        match board[index]:
            case 'P' | 'B' | 'R' | 'Q':
                inCheck = checkKing(board ,board[index], index, lineCount)
                if (inCheck == True):
                    print("Success")
                return
    print("Fail")
    return
def main():
    board = """\
....Q
.....
.....
.....
K....\
"""
    # board = input()
    checkmate(board)
if __name__ == "__main__":
    main()