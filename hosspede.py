#Game made from scratch for Unix bash or maybe Windows command prompt (haven't tested)
#Date: Sep 16 2012
#Chris Laverdiere
#This is just a simple centipede type game with manual controls and real life money.

import random
import sys
import os

def main():

    os.system('cls' if os.name=='nt' else 'clear') 
    print '##################################################'
    print '                    HOSSPEDE                      '
    print '##################################################\n'

    diff = raw_input("Choose Difficulty: \n1. easy\n2. medium\n3. hard\n-> ")

    if diff == 'easy' or diff == '1':
        lim = 8 
        lim2 = 8
    elif diff == 'medium' or diff == '2':
        lim = 16                                    #Difficulty Settings
        lim2 = 16
    elif diff == 'hard' or diff == '3':
        lim = 24
        lim2 = 24
    else:
        'Enter easy, medium, or hard next time'

    m = [lim/2,lim2/2]

    t = [random.randint(1,lim-1),random.randint(1,lim2-1)]
    c = 100
                                                   #List and Variable creation
    ray2 = [['.' for i in xrange(lim)] for i in xrange(lim2)]
    ray2[lim/2][lim2/2] = 'o'
    ray2[t[0]][t[1]] = '$'

    draw(ray2,m,t,c)

def draw(l,m,t,c):     # l: list  m: middle  t: top dolla (i don't know lol)  c: cash

    os.system('cls' if os.name=='nt' else 'clear') 

    if (t[0] == m[0]) and (t[1] == m[1]):
        t = [random.randint(0,len(l) - 1), random.randint(0,len(l[m[0]]) - 1)]
        l[t[0]][t[1]] = '$'
        c *= 1.3                         #Checks if money is collected

    for i in l:
        for j in l[l.index(i)]:
            sys.stdout.write(str(j))         #Displays display
        sys.stdout.write('\n')

    print 'You have %.2f monies!' % c
    dir = raw_input("Hit enter to quit.\nAwaiting move [u - d - l - r]: ")

    if dir == 'u':
        l[m[0]][m[1]] = '.' 
        m[0] -= 1

        if m[0] < 0:
            print 'out of bounds!'
            return

        l[m[0]][m[1]] = 'o'
        draw(l,m,t,c)
        
    elif dir == 'd':
        l[m[0]][m[1]] = '.' 
        m[0] += 1

        if m[0] > (len(l) - 1):
            print 'out of bounds!'
            return
                                           #Direction input logic
        l[m[0]][m[1]] = 'o'
        draw(l,m,t,c)

    elif dir == 'l':
        l[m[0]][m[1]] = '.' 
        m[1] -= 1

        if m[1] < 0:
            print 'out of bounds!'
            return

        l[m[0]][m[1]] = 'o'
        draw(l,m,t,c)

    elif dir == 'r':
        l[m[0]][m[1]] = '.' 
        m[1] += 1

        if m[1] > (len(l[m[0]]) - 1):
            print 'out of bounds!'
            return

        l[m[0]][m[1]] = 'o'
        draw(l,m,t,c)

    else:
        print "Bye! (You win, by the way. Everyone who plays my game is a winner.)"

if __name__ == "__main__":
    main()

