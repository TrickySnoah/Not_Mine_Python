import random
def encrc():
    code_upper = {'A':'P','B':'O','C':'I','D':'U','E':'Y','F':'T','G':'R','H':'E','I':'W','J':'Q','K':'L','L':'K',
            'M':'J','N':'H','O':'G','P':'F','Q':'D','R':'S','S':'A','T':'M','U':'N','V':'B','W':'V','X':'C','Y':'X','Z':'Z',
                  '1':'5','2':'6','3':'4','4':'7','5':'3','6':'8','7':'2','8':'9','9':'1','0':'9'
            }
    code={}
    for key in code_upper:
        points = code_upper[key]
        code[key] = points
        if key.isalnum():
            code[key.lower()] = points.lower()
    file = input("Enter the name of a file.")
    fl = open(file,'r')
    con = ''
    for line in fl:
        con+=line
    fl.close()
    fl = open('encryption.txt','w')
    encrcon = ''
    for char in con:
        if char==' ':
            encrcon+=' '
        elif not char.isalnum():
            encrcon+=char
        else:
            new_c=code[char]
            encrcon+=new_c
    fl.write(encrcon)
    fl.close()
    print("the contents have been encrypted.")
def dencrc():
    code_upper = {'A':'P','B':'O','C':'I','D':'U','E':'Y','F':'T','G':'R','H':'E','I':'W','J':'Q','K':'L','L':'K',
            'M':'J','N':'H','O':'G','P':'F','Q':'D','R':'S','S':'A','T':'M','U':'N','V':'B','W':'V','X':'C','Y':'X','Z':'Z',
                  '1':'5','2':'6','3':'4','4':'7','5':'3','6':'8','7':'2','8':'9','9':'1','0':'9'
            }
    code={}
    for key in code_upper:
        points = code_upper[key]
        code[points] = key
        if key.isalnum() and not key.isdigit():
            code[points.lower()] = key.lower()
    infile = open('encryption.txt','r')
    contents = ''
    for line in infile:
        contents+=line
    infile.close()
    deccont = ''
    for char in contents:
        if char==' ':
            deccont+=' '
        elif not char.isalnum():
            deccont+=char
        else:
            new_c=code[char]
            deccont+=new_c
    print('The decrypted msg is:\n')
    print(deccont)
def uniquewords():
    file=input("Enter a file.")
    file=open(file,'r')
    words=''
    for line in file:
        words+=line.rstrip('\n')
    unqwords=[]
    words=words.split()
    for word in words:
        unqwords.append(word)
    unqwords=set(unqwords)
    print(f"Here are the unique words.\n{unqwords}")
def wsw():
    file=open("WorldSeries.txt",'r')
    teams=[]
    for line in file:
        teams.append(line.rstrip('\n'))
    while True:
        year=int(input('Enter a year from 1903 to 2008.'))
        if year>2008 or year<1903:
            print("Enter a year between the dates given.")
            continue
        break
    yea=year-1903
    if yea==1 or yea==91:
        print(f"The world series was not played in {year}")
    else:
        team=teams[yea]
        times=teams.count(team)
        print(f'the {team} won in {year}\nthe {team} won {times} times.')
def blackjack():
    deck = {'Ace of Spades' : 1, '2 of Spades' : 2, '3 of Spades' : 3,
        '4 of Spades' : 4, '5 of Spades' : 5, '6 of Spades' : 6,
        '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9,
        '10 of Spades' : 10, 'Jack of Spades' : 10, 'Queen of Spades' : 10,
        'King of Spades' : 10,
        'Ace of Hearts' : 1, '2 of Hearts' : 2, '3 of Hearts' : 3,
        '4 of Hearts' : 4, '5 of Hearts' : 5, '6 of Hearts' : 6,
        '7 of Hearts' : 7, '8 of Hearts' : 8, '9 of Hearts' : 9,
        '10 of Hearts' : 10, 'Jack of Hearts' : 10, 'Queen of Hearts' : 10,
        'King of Hearts' : 10,
        'Ace of Clubs' : 1, '2 of Clubs' : 2, '3 of Clubs' : 3,
        '4 of Clubs' : 4, '5 of Clubs' : 5, '6 of Clubs' : 6,
        '7 of Clubs' : 7, '8 of Clubs' : 8, '9 of Clubs' : 9,
        '10 of Clubs' : 10, 'Jack of Clubs' : 10, 'Queen of Clubs' : 10,
        'King of Clubs' : 10,
        'Ace of Diamonds' : 1, '2 of Diamonds' : 2, '3 of Diamonds' : 3,
        '4 of Diamonds' : 4, '5 of Diamonds' : 5, '6 of Diamonds' : 6,
        '7 of Diamonds' : 7, '8 of Diamonds' : 8, '9 of Diamonds' : 9,
        '10 of Diamonds' : 10, 'Jack of Diamonds' : 10, 'Queen of Diamonds' : 10,
        'King of Diamonds' : 10}
    p1pts = 0
    p2pts = 0
    p1d = []
    p2d = []
    tts = 1
    for turn in range(1,53):
        card=random.choice(list(deck))
        points=deck.pop(card)
        if (turn%2) == 1:
            if card[:3]=='Ace'and p1pts>10:
                p1d.append(card)
                p1pts+=1
            else:
                p1d.append(card)
                p1pts+=points
        else:
            if card[:3]=='Ace'and p2pts>10:
                p2d.append(card)
                p2pts+=1
            else:
                p2d.append(card)
                p2pts+=points
        if (turn%2) == 0:
            if p1pts>21 and p2pts > 21:
                the_glorious_blood_thirsty_victor_who_beat_the_other_player = 0
                the_winnders_den(p1pts, p2pts, p1d, p2d, the_glorious_blood_thirsty_victor_who_beat_the_other_player, tts)
                tts = 0
            elif p1pts > 21:
                the_glorious_blood_thirsty_victor_who_beat_the_other_player = 1
                the_winnders_den(p1pts, p2pts, p1d, p2d, the_glorious_blood_thirsty_victor_who_beat_the_other_player, tts)
                tts = 0
            elif p2pts > 21:
                the_glorious_blood_thirsty_victor_who_beat_the_other_player = 2
                the_winnders_den(p1pts, p2pts, p1d, p2d, the_glorious_blood_thirsty_victor_who_beat_the_other_player, tts)
                tts = 0
            if tts == 0:
                p1d = []
                p2d = []
                p1pts = 0
                p2pts = 0
                print()
        tts += 1
    if p1pts == p2pts:
        msg = 'it was a draw'
    elif p1pts > p2pts:
        msg = 'player 2 won'
    elif p2pts > p1pts:
        msg = 'player 1 won'
  
def the_winnders_den(p1pts, p2pts, p1d, p2d, the_glorious_blood_thirsty_victor_who_beat_the_other_player, tts):
    d = p1d
    if the_glorious_blood_thirsty_victor_who_beat_the_other_player == 0:
        msg = 'it was a draw'
    elif the_glorious_blood_thirsty_victor_who_beat_the_other_player == 1:
        msg = 'player 2 won'
    else:
        msg = 'player 1 won'
    print(f'{msg}'+
          "\ncards")
    for num in range(int(tts-(tts/2))):
            print(f'{d[num]}\t{p2d[num]}')