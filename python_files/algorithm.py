import sys
import board_utils


def algorithm(board, playRow, playCol, currColour, us):
    boardCheckResult = sub_board_is_full(board, playRow, playCol)

    if boardCheckResult == '0':
        return getScore(board, playRow, playCol, currColour, us)

    #We would have to make a bad move, by sending the opponent to a full or won section
    if currColour == us:
        return -1000

    #the opponent would make a bad move by sending us to a full or won section
    else:
        return 1000

def getScore(board, checkRow, checkCol, currColour, us):
    pointTotal = 0;
    for k2 in range(3):
        for l2 in range(3):

          curr = board[checkRow][checkCol][k2][l2]

          if curr == us:
            if k2 == 1 and l2 == 1:
              pointTotal += 5
            elif (k2+l2) % 2 == 0:
              pointTotal += 3;
            else:
              pointTotal += 1;
          elif curr == opposite(us):
            if k2 == 1 and l2 == 1:
              pointTotal -= 5;
            elif (k2+l2) % 2 == 0:
              pointTotal -= 3;
            else:
              pointTotal -= 1;


          #printf("%c  %d\n", curr, pointTotal);

    return pointTotal;

if __name__ == "__main__":
    print("Testing")
