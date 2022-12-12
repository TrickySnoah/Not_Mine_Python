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
    turn='x'
    for rounds in range(0,9):
        while True:
            try:
                spot=int(input("Where would you like to move?"))
            except:
                print("Enter a number.")
                continue
            if spot<1 or spot>9:
                print("Choose something inside of the board.")
                continue
            if spot>6:
                spot-=6
                x=2
            elif spot>3:
                spot-=3
                x=1
            else:
                x=0
            if board[x][spot] != ' ':
                print("Choose a spot on the board that isn't taken.")
                continue
            else:
                board[x][spot] = turn
            if turn=='x':
                turn='o'
            else:
                turn='x'
    