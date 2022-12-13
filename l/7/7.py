import random
import matplotlib.pyplot as pchart

def license_exam():
    answer_key=[]
    answers=[]
    key=open("driver_test_key.txt","r")
    for line in key:
        answer_key.append(line.rstrip("\n"))
    while True:
        file=input("what file do you want to open?")
        try:
            file=open(file,"r")
            for line in file:
                answers.append(line.rstrip("\n"))
            right=0
            wrong=0
            wrong_questions=[]
            for num in range(0,20):
                if answer_key[num] == answers[num]:
                    right+=1
                else:
                    wrong+=1
                    wrong_questions.append(str(num))
            print("Grading done.")
            print(f"You answerd {right} questions out of 20 questions.")
            print(f"You missed {wrong} questions in total.")
            if wrong>5:
                print("You failed.")
            else:
                print("You didn't fail.")
            print(f"Here are the questions you missed. {wrong_questions}")
            another=input("Check another test? (y/n)")
            if another!='y':
                break
        except:
            print("the file doesn't exist.")     
def ttt():
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]
    xboard = [[0,0,0],[0,0,0],[0,0]]
    oboard = [[0,0,0],[0,0,0],[0,0]]
    turn='x'
    win=''
    for rounds in range(0,9):
        if win!='':
            break
        while True:
            if turn=='x':
                print("It's x's turn.\n")
                try:
                    spot=int(input("Where would you like to move?"))
                except:
                    print("Enter a number.")
                    continue
                if spot<1 or spot>9:
                    print("Choose something inside of the board.")
                    continue
                if spot>6:
                    spot-=7
                    x=2
                elif spot > 3:
                    spot -= 4
                    x = 1
                else:
                    spot -= 1
                    x = 0
                if board[x][spot] != ' ':
                    print("Choose a spot on the board that isn't taken.")
                    continue
                else:
                    board[x][spot] = turn
                    xboard[0][x]+=1
                    xboard[1][spot]+=1
                    if x==0 and spot==0 or x==1 and spot==1 or x==2 and spot==2:
                        xboard[2][0]+=1
                    if x==0 and spot==2 or x==1 and spot==1 or x==2 and spot==0:
                        xboard[2][1]+=1
                if turn=='x':
                    turn='o'
                else:
                    turn='x'
                break
            else:
                print("It's o's turn.\n")
                while True:
                    x=random.randint(0,2)
                    y=random.randint(0,2)
                    if board[x][y]=='x' or board[x][y]=='o':
                        continue
                    else:
                        board[x][y]=turn
                        break
                turn='x'
                oboard[0][x]+=1
                oboard[1][y]+=1
                if x==0 and y==0 or x==1 and y==1 or x==2 and y==2:
                    oboard[2][0]+=1
                if x==0 and y==2 or x==1 and y==1 or x==2 and y==0:
                    oboard[2][1]+=1
                break
        if rounds>3:
            for lists in xboard:
                for num in lists:
                    if num==3:
                        win='x'
                        break
            for lists in oboard:
                for num in lists:
                    if num==3:
                        win='o'
                        break
        print(board[0],board[1],board[2],sep='\n')
        print()
    if win!='o' and win!='x':
        print("The game ended in a tie.")
    elif win=='o':
        print("Player o won.")
    else:
        print("Player x won.")
def secret_santa():
    dev_dep=['Julia','Oliver','Abigail']
    hr_dep=['Camden','Kayleigh','Cooper','Kerrigan']
    sales_dep=['Avery','Charlotte','Elle']
    random.shuffle(dev_dep)
    random.shuffle(hr_dep)
    random.shuffle(sales_dep)
    print(f'{dev_dep[0]} gifts to {hr_dep[0]}')
    print(f'{hr_dep[0]} gifts to {sales_dep[0]}')
    print(f'{sales_dep[0]} gifts to {dev_dep[1]}')
    print(f'{dev_dep[1]} gifts to {hr_dep[1]}')
    print(f'{hr_dep[1]} gifts to {sales_dep[1]}')
    print(f'{sales_dep[1]} gifts to {dev_dep[2]}')
    print(f'{dev_dep[2]} gifts to {hr_dep[2]}')
    print(f'{hr_dep[2]} gifts to {sales_dep[2]}')
    print(f'{sales_dep[2]} gifts to {hr_dep[3]}')
    print(f'{hr_dep[3]} gifts to {dev_dep[0]}')
def ateball():
    responses=[]
    another='y'
    all_responses=open('8_ball_responses.txt','r')
    for line in all_responses:
        responses.append(line)
    while another=='y':
        question=input("What's your question?")
        print()
        num=random.randint(0,11)
        print(responses[num])
        another=input("Ask another question? (y/n)")
    print("Bye")
def piechart():
    expenses=open('expenses.txt','w')
    categories=['rent','gas','food','clothing','car payment','misc']
    count=0
    more=False
    while not more:
        try:
            print(f"how much was spent on {categories[count]}",end='')
            money=int(input("?"))
            if money>=0:
                more=False
                expenses.write(str(money)+'\n')
                count+=1
            else:
                print('\nPlease enter a proper number\n')
        except:
            more = True
    expenses.close()
    display(categories)
def display(categories):
    expenses=open('expenses.txt','r')
    name=categories
    size=[]
    line=expenses.readline()
    while line!='':
        size.append(line.rstrip('\n'))
        line=expenses.readline()
    pchart.pie(size, labels=name)
    pchart.title('$ Spend')
    pchart.show()
def gaschart():
    infile = open('1994_Weekly_Gas_Averages.txt','r')
    pchart.xlim(xmin=0,xmax=52)
    pchart.ylim(ymin=0,ymax=52)
    y_ticks=[[],[]]
    cou=0
    for line in infile:
        y_ticks[0].append(cou)
        cou+=1
        y_ticks[1].append(line.rstrip('\n'))
    pchart.yticks(y_ticks[0],y_ticks[1])
    pchart.xticks([10,20,30,40,50],['10','20','30','40','50'])
    pchart.title('gas prices')
    pchart.xlabel('weeks')
    pchart.ylabel('gas price')
    x_coords=[0,9,10,11,12,13,34,35,36,40,41,42,52]
    y_coords=[0,8,5,4,5,9,34,33,35,40,30,41,52]
    pchart.plot(x_coords,y_coords)
    pchart.show()