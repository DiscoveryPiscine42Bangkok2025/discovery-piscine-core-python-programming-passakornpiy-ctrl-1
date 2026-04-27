#!/usr/bin/env python3

# # # This is probably an excessive amount of comments but I figured I should explain it right now so I don't stutter later. -ppiyayop//

# fixing needed : diaganol piece blocking

def checkKing(stri, piece, pos, lineCount):
    # Find if the king is in check
    match (piece):
        case 'P':
            # # # I don't think pawn needs a seperate function//
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

def checkDiagonal(stri, lineCount, pos): # idk how this works i just winged it
    #up left
    for i in range(1, lineCount):
        checking = (pos - (lineCount * i)) - i
        noLessThan = ((lineCount - i) - 1) * lineCount
        noMoreThan = (lineCount - i) * lineCount
        # print(lineCount * lineCount, "i", i, "lines",  lineCount, "positions", checking, noMoreThan, noLessThan)
        if (checking < 0 or checking < noLessThan or checking >= noMoreThan):
            break
        if (stri[checking] != "."):
            match stri[checking]:
                case 'P' | 'B' | 'R' | 'Q':
                    break
                case 'K':
                    return True
    # up right
    for i in range(1, lineCount):
        checking = (pos - (lineCount * i)) + i
        noLessThan = ((lineCount - i) - 1) * lineCount
        noMoreThan = (lineCount - i) * lineCount
        # print(lineCount * lineCount, "i", i, "lines",  lineCount, "positions", checking, noMoreThan, noLessThan)
        if (checking < 0 or checking < noLessThan or checking >= noMoreThan):
            break
        if (stri[checking] != "."):
            match stri[checking]:
                case 'P' | 'B' | 'R' | 'Q':
                    break
                case 'K':
                    return True
    # down left
    for i in range(1, lineCount):
        checking = (pos + (lineCount * i)) - i
        noLessThan = i * lineCount
        noMoreThan = (i + 1) * lineCount
        # print(lineCount * lineCount, "i", i, "lines",  lineCount, "positions", checking, noMoreThan, noLessThan)
        if (checking < 0 or checking < noLessThan or checking >= noMoreThan):
            break
        if (stri[checking] != "."):
            match stri[checking]:
                case 'P' | 'B' | 'R' | 'Q':
                    break
                case 'K':
                    return True
    # down left
    for i in range(1, lineCount):
        checking = (pos + (lineCount * i)) + i
        noLessThan = i * lineCount
        noMoreThan = (i + 1) * lineCount
        # print(lineCount * lineCount, "i", i, "lines",  lineCount, "positions", checking, noMoreThan, noLessThan)
        if (checking < 0 or checking < noLessThan or checking >= noMoreThan):
            break
        if (stri[checking] != "."):
            match stri[checking]:
                case 'P' | 'B' | 'R' | 'Q':
                    break
                case 'K':
                    return True
    """
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
        if (noLessThanUp >= 0 and upCheck1 >= noLessThanUp and upCheck1 < noMoreThanUp and stri[upCheck1] != "."):
            match stri[upCheck1]:
                case 'P' | 'B' | 'R' | 'Q':
                    return False
                case 'K':
                    return True
        if (noLessThanUp >= 0 and upCheck2 >= noLessThanUp and upCheck2 < noMoreThanUp and stri[upCheck2] != "."):
            # print("UPCHECK2", upCheck2)
            match stri[upCheck2]:
                case 'P' | 'B' | 'R' | 'Q':
                    return False
                case 'K':
                    return True
        if (noMoreThanLow <= lineCount * lineCount and lowCheck1 < noMoreThanLow and lowCheck1 >= noLessThanLow and stri[lowCheck1] != "."):
            # print("LOWCHECK1", lowCheck1)
            match stri[lowCheck1]:
                case 'P' | 'B' | 'R' | 'Q':
                    return False
                case 'K':
                    return True
        if (noMoreThanLow <= lineCount * lineCount and lowCheck2 < noMoreThanLow and lowCheck2 >= noLessThanLow and stri[lowCheck2] != "."):
            # print("LOWCHECK2", lowCheck2)
            match stri[lowCheck2]:
                case 'P' | 'B' | 'R' | 'Q':
                    return False
                case 'K':
                    return True
    return False
    """

def checkHorizontal(stri, lineCount, pos):
    column = (pos) // lineCount
    noLessThan = (column) * (lineCount)
    noMoreThan = (column + 1) * (lineCount)
    for i in range(1, lineCount):
        checking = pos + i
        # print(lineCount, column, noLessThan, noMoreThan, checking)
        if (checking >= noMoreThan):
            break
        if (stri[checking] != "."):
            # print("horizontal")
            match stri[checking]:
                case 'P' | 'B' | 'R' | 'Q':
                    break
                case 'K':
                    return True
    # print("switch side")
    for i in range(1, lineCount):
        checking = pos - i
        # print(lineCount, column, noLessThan, noMoreThan, checking)
        if (checking < noLessThan):
            break
        if (stri[checking] != "."):
            # print("horizontal")
            match stri[checking]:
                case 'P' | 'B' | 'R' | 'Q':
                    break
                case 'K':
                    return True
    return False

def checkVertical(stri, lineCount, pos): # i fucked this up big time yet it works??
    for i in range(1, lineCount):
        checkPos1 = pos - (lineCount * i)
        # print(checkPos1)
        if (checkPos1 >= 0 and stri[checkPos1] != "."):
            # print("-", checkPos1)
            match stri[checkPos1]:
                case 'K':
                    return True
            break
    for i in range(1, lineCount):
        checkPos2 = pos + (lineCount * i)
        # print(checkPos2)
        if (checkPos2 < lineCount * lineCount and stri[checkPos2] != "."):
            # print("-", checkPos2)
            match stri[checkPos2]:
                case 'K':
                    return True
            break

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
........
........
........
........
........
........
........
...K....\
"""
    # board = input()
    checkmate(board)
if __name__ == "__main__":
    main()