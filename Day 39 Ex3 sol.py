questions = [
    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],
    
    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ],

    [
        "Which language was used to create facebook","French","JavaScript","Php","None","Python",3
    ]
]

money = [
            1000,
            2000,
            3000,
            5000,
            10000,
            20000,
            40000,
            80000,
            160000,
            320000,
            640000,
            1250000,
            2500000,
            5000000,
            7500000,
            10000000,
            75000000
        ]

money_won = 0

# print(len(questions))
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs. {money[i]} is:-\n{question[0]}\n")
    print(f"A. {question[1]}                    B. {question[2]}")
    print(f"C. {question[3]}                       D. {question[4]}")
    reply = int(input("Entre Your In Answer (1-4): "))
    if reply == question[-1]:
        money_won = money[i]
        print(f"\nCorrect answer!!, Your balance is ₹{money_won}")
    else:
        print(f"\nYou have given wrong answer!\n\nSo you are now out of game\n\nWell played!!\n\nWou have won total ammount of ₹{money_won}\n\nCongratulations!!")
        break
else:
    print(f"\nYou Have Won The Game!!\n\nYou have won total ammount of ₹{money_won}\n\nCongratulations!!")

