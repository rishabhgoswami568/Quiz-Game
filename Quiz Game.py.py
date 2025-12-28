questions = [
    ["What is the capital of India?",
"Mumbai","New Delhi","Kolkata","Chennai",1],
    ["Which planet is known as the red Planet?",
"Venus","Mars","Jupiter","Saturn",1],
    ["Who wrote the Indian national anthem?",
"Bankim Chandra Chattopadhyay","Rabindranath Tagore","Mahatma Gandhi","Jawaharlal Nehru",1],
    ["What is the name of the largest ocean on Earth?",
"Atlantic Ocean","Indian Ocean","Pacific Ocean","Arctic Ocean",2],
    ["Which gas is used to extinguish fires?",
"Oxygen","Nitrogen","Carbon dioxide","Hydrogen",2] ,
    ["What is the chemical symbol for water?",
"H2O"," CO2","NaCl","O2 ",0],
    ["What is the largest planet in our solar system?",
"Earth","Mars","Jupiter","Saturn ",2],
    ["What is the process by which plants make their own food?",
"Respiration","Photosynthesis","Digestion","Circulation Mentimeter ",1],
    ["What is the smallest unit of matter?",
"Cell","Molecule","Atom","Organ",2],
    ["What is the name of the Earth's only natural satellite?",
"Sun","Moon","Mars","Venus",1],
    ["What is the capital of France?",
"Berlin","Rome","Paris","London ",2],
    ["What is the name of the world's longest river?",
"Amazon","Nile","Yangtze","Mississippi ",1],
    ["What is the name of Mickey Mouse's dog?",
"Pluto","Goofy","Donald","Minnie",0],
    ["How many days are there in a week?",
"5","6","7","8",2],
    ["What color is the sky on a clear day?",
"Red","Green","Blue","Yellow ",2],
    ["Which city in the country of India is the largest in terms of population?",
"Delhi","Kolkata","Jaipur","Mumbai",3],
    ["Which gas planet is the largest planet in the Solar System?",
"Jupiter","Saturn","Uranus","Neptune",0],  

]

levels = [1000 , 2000 , 3000 , 5000 , 10000 , 20000 , 40000 , 80000 , 160000 , 320000 , 640000 , 1250000 , 2500000 , 5000000 , 7500000 , 10000000 , 75000000]
money = 0
for i in range(0 , len(questions)):

    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}               b. {question[2]} ")
    print(f"c. {question[3]}               d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or quit:\n "))
    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer , you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 7500000
        elif(i == 16):
            money = 75000000
    else:
        print("Wrong amswer!")
        break

print(f"Your take home money is {money}")                                                                                                        