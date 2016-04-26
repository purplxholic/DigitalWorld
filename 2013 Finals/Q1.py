def init():
    nl =[['_']*3]*3
    return nl
# print init()

def show(b):
    grid =  ''
    for i in b:
        i.append('\n')
        for j in i:
            grid += j

    return grid
b = init()
# print show(b)

def movex(b,i,j):
    b[i-1][j-1] = 'x'
    return b

def moveo(b,i,j):
    b[i-1][j-1] = 'o'

# print movex(b,1,3)

def countmoves(b):
    moves = 0
    for i in b:
        for j in i:
            if j != '_':
                moves += 1
    return moves

# print countmoves(b)

def getmoves(b):
    moves = {}
    xmoves = []
    omoves =[]
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 'x' :
                xmoves.append((i+1,j+1))
            if b[i][j] == 'o':
                omoves.append((i+1,j+1))
            if b[i][j] == '_':
                pass
    #hardcoded 
    moves['x'] = xmoves
    moves['o'] = omoves
    return moves
print getmoves([[ 'x', 'o', '_'],['_', 'o', 'x'],['_', '_', 'x']])

def winsx(b):
    for i in b:
        
