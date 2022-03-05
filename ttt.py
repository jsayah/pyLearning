g_size = 0
game = []
p1score = 0
p2score = 0
pt = 0
playing = True

def play():
    global game
    while(True):
            try:
                p = input('Would you like to play Tic Tac Toe? Y/N: ').lower()
                if p == 'y':
                    break
                elif p == 'n':
                    quit()
            except:
                print('Invalid Entry.')
    while(True):
        game = gen_game(game)
        game = prnt_game(game, just_display=True)
        while playing:
            rc = 0
            cc = 0 
            print('Player', pt, 'turn.')
            try:
                rc = int(input('Row: '))
            except:
                print('Numbers only please.')
            try:
                cc = int(input('Row: '))
            except:
                print('Numbers only please.')
            game = prnt_game(game, pt, rc, cc)
            win(game)
        print('------ Final Score ------')
        print('Player 1: ', p1score)
        print('Player 2: ', p2score)
        break
            

def gen_game(g):
    global pt
    pt = 1
    size = True
    while size:
        try:
            g_size = int(input("How many in a row to win? (Max 9): "))
            if g_size >= 10:
                raise ValueError
            else:    
                size = False
        except:
            print('Oops something went wrong!')
            
    for c in range(g_size):
        row = []
        for co in range(g_size):
            row.append(0)
        game.append(row)
    return g

def prnt_game(g_map, player = 0, row = 0, col = 0, just_display=False):
    global pt
    cl = []
    for c in range(len(game)):
        cl.append(str(c))
    try:
        print('  ','  '.join(cl))
        if not just_display and g_map[row][col] == 0:
            g_map[row][col] = player
            if pt == 1:
                pt += 1
            else:
                pt -= 1
        for (r, row) in enumerate(g_map, start=0):   
            print(r, row)
        return g_map
    except:
        print('Oops, Something went wrong! Please try again.')

def win(c_game):
    diag1 = []
    diag2 = []
    for row in c_game:
        cwin(row)
    for col in range(len(c_game)):
        check = []
        for row in c_game:
            check.append(row[col])
        cwin(check)  
    for c in range(len(c_game)):
        diag1.append(game[c][c])
    cwin(diag1)
    for cx, cz in enumerate(reversed(range(len(c_game)))):
        diag2.append(game[cz][cx])
    cwin(diag2)

def score(s):
    global p1score
    global p2score
    if s == 1:
        p1score += 1
    else:
        p2score += 1

def replay(player):
    global game
    global playing
    print('Player',player,'Wins!')
    while(True):
        try:
            r = input('Would you like to play again? Y/N: ').lower()
            if r == 'n':
                playing = False
                break
            elif r == 'y':
                game = []
                game = gen_game(game)
                game = prnt_game(game, just_display=True)
                break
        except:
            print('Invalid Entry.')

def cwin(li):
    if li.count(li[0]) == len(li) and li[0] != 0:
            score(li[0])
            replay(li[0])

play()
