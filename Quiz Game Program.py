print("QUIZ GAME \n")

questions = ["How many elements are there in periodic table?" ,
             "Which animal lays the largest egg?" ,
             "Which is the most abundant gas in earth's atmospere?" ,
             "How many bones are there in a humna body?" ,
             "Which planet in the solar system is the hottest?" ,
             ]

options = [["A.116" , "B.117" , "C.118" , "D.119"] ,
           ["A.Whale" , "B.Crocodile" , "C.Elephant" , "D.Ostrich"] ,
           ["A.Nitrogen" , "B.Oxygen" , "C.Carbondioxide" , "D.Hydrogen"] ,
           ["A.206" , "B.207" , "C.208" , "D.209"] ,
           ["A.Mercury" , "B.Venus" , "C.Earth" , "D.Mars"]]

optionindex = 0

answers = ["C" , "D" , "A" , "A" , "B"]

answerindex = 0

youranswers = []

score = 0



for question in questions:
    print("--------------------------")
    print(question)
    for option in options[optionindex]:
        print(option)

    youranswer = input("Enter one option(A , B , C, D) : ").upper()
    youranswers.append(youranswer)

    if youranswer == answers[answerindex]:
        score = score+1
        print(youranswer , "IS CORRECT!")
    else:
        print(youranswer , "INCORRECT!")
        print(answers[optionindex] , "is correct")
        
    optionindex+=1
    answerindex+=1
    
print("--------------------------")
print("          RESULT          ")
print("--------------------------")

print("Answers : " , end = " ")
for answer in answers:
    print(answer , end = " ")
print()

print("Your answers are : " , end = " ")
for youranswer in youranswers:
    print(youranswer , end = " ")
print()


score = int(score / len(questions)*100)

print(f"Your score is : {score}%")
