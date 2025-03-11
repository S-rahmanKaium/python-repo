quiz = {
    "Q1": {
        "question": "What is the name of Luffy’s devil fruit?",
        "options": [
            "a) Mera Mera no Mi",
            "b) Gomu Gomu no Mi",
            "c) Ope Ope no Mi",
            "d) Hito Hito no Mi"
        ],
        "answer": "b) Gomu Gomu no Mi"
    },
    "Q2": {
        "question": "Who was the first member to join Luffy’s crew?",
        "options": [
            "a) Sanji",
            "b) Zoro",
            "c) Usopp",
            "d) Nami"
        ],
        "answer": "b) Zoro"
    },
    "Q3": {
        "question": "Which sea is Luffy from?",
        "options": [
            "a) North Blue",
            "b) East Blue",
            "c) West Blue",
            "d) South Blue"
        ],
        "answer": "b) East Blue"
    },
    "Q4": {
        "question": "Who is the captain of the Red Haired Pirates?",
        "options": [
            "a) Shanks",
            "b) Mihawk",
            "c) Luffy",
            "d) Law"
        ],
        "answer": "a) Shanks"
    },
    "Q5": {
        "question": "What is the name of Luffy's first ship?",
        "options": [
            "a) Thousand Sunny",
            "b) Going Merry",
            "c) Black Pearl",
            "d) Sunny Go"
        ],
        "answer": "b) Going Merry"
    },
    "Q6": {
        "question": "What is the name of Luffy's first bounty hunter friend?",
        "options": [
            "a) Sanji",
            "b) Zoro",
            "c) Usopp",
            "d) Nami"
        ],
        "answer": "b) Zoro"
    },
    "Q7": {
        "question": "Which of these characters is known as the 'God Usopp'?",
        "options": [
            "a) Usopp",
            "b) Franky",
            "c) Luffy",
            "d) Zoro"
        ],
        "answer": "a) Usopp"
    },
    "Q8": {
        "question": "Who killed Whitebeard during the Marineford War?",
        "options": [
            "a) Akainu",
            "b) Blackbeard",
            "c) Shanks",
            "d) Mihawk"
        ],
        "answer": "b) Blackbeard"
    },
    "Q9": {
        "question": "Which Admiral possesses the magma-magma fruit?",
        "options": [
            "a) Aokiji",
            "b) Kizaru",
            "c) Akainu",
            "d) Sengoku"
        ],
        "answer": "c) Akainu"
    },
    "Q10": {
        "question": "How many Devil Fruits has Luffy eaten?",
        "options": [
            "a) 1",
            "b) 2",
            "c) 3",
            "d) 4"
        ],
        "answer": "a) 1"
    }
}

#----------
# Que No 1
#----------
print(quiz["Q1"]["question"])
print(quiz["Q1"]["options"] )
ans1 = input("Enter Your Answer: ")

if ans1 == 'b' :
    print("Correct ! Move To Next...")
else :
    print(f"Snap, Better Luck Next Time. The Correct Answer Is {quiz["Q1"]["answer"]}")
#----------
# Que No 2
#----------
print(quiz["Q2"]["question"])
print(quiz["Q2"]["options"] )
ans2 = input("Enter Your Answer: ")

if ans2 == 'b' :
    print("Correct ! Move To Next...")
else :
    print(f"Snap, Better Luck Next Time. The Correct Answer Is {quiz["Q2"]["answer"]}")
#----------
# Que No 3
#----------
print(quiz["Q3"]["question"])
print(quiz["Q3"]["options"] )
ans3 = input("Enter Your Answer: ")

if ans3 == 'b' :
    print("Correct ! Move To Next...")
else :
    print(f"Snap, Better Luck Next Time. The Correct Answer Is {quiz["Q3"]["answer"]}")
#----------
# Que No 4
#----------
print(quiz["Q4"]["question"])
print(quiz["Q4"]["options"] )
ans4 = input("Enter Your Answer: ")

if ans4 == 'a' :
    print("Correct ! Move To Next...")
else :
    print(f"Snap, Better Luck Next Time. The Correct Answer Is {quiz["Q4"]["answer"]}")
#----------
# Que No 5
#----------
print(quiz["Q5"]["question"])
print(quiz["Q5"]["options"] )
ans5 = input("Enter Your Answer: ")

if ans5 == 'b' :
    print("Correct ! Move To Next...")
else :
    print(f"Snap, Better Luck Next Time. The Correct Answer Is {quiz["Q5"]["answer"]}")
#----------
# Que No 6
#----------
print(quiz["Q6"]["question"])
print(quiz["Q6"]["options"] )
ans6 = input("Enter Your Answer: ")

if ans6 == 'b' :
    print("Correct ! Move To Next...")
else :
    print(f"Snap, Better Luck Next Time. The Correct Answer Is {quiz["Q6"]["answer"]}")
#----------
# Que No 7
#----------
print(quiz["Q7"]["question"])
print(quiz["Q7"]["options"] )
ans7 = input("Enter Your Answer: ")

if ans7 == 'a' :
    print("Correct ! Move To Next...")
else :
    print(f"Snap, Better Luck Next Time. The Correct Answer Is {quiz["Q7"]["answer"]}")
#----------
# Que No 8
#----------
print(quiz["Q8"]["question"])
print(quiz["Q8"]["options"] )
ans8 = input("Enter Your Answer: ")

if ans8 == 'b' :
    print("Correct ! Move To Next...")
else :
    print(f"Snap, Better Luck Next Time. The Correct Answer Is {quiz["Q8"]["answer"]}")
#----------
# Que No 9
#----------
print(quiz["Q9"]["question"])
print(quiz["Q9"]["options"] )
ans9 = input("Enter Your Answer: ")

if ans9 == 'c' :
    print("Correct ! Move To Next...")
else :
    print(f"Snap, Better Luck Next Time. The Correct Answer Is {quiz["Q9"]["answer"]}")
#----------
# Que No 10
#----------
print(quiz["Q10"]["question"])
print(quiz["Q10"]["options"] )
ans10 = input("Enter Your Answer: ")

if ans10 == 'a' :
    print("You Got The ONE PIECE")
else :
    print(f"Snap, Better Luck Next Time. The Correct Answer Is {quiz["Q10"]["answer"]}")
