quiz = {
    "Question 1":{
"Question":'What is the capital of Pkistan?',
 "Answer":"Islamabad"
    },  "Question 2":{
"Question":'What is the capital of India?',
 "Answer":"Mumbai"
    }, "Question 3":{
"Question":'What is the capital of France?',
 "Answer":"Paris"
    }, "Question 4":{
"Question":'What is the capital of Germany?',
 "Answer":"Berlin"
    }, "Question 5":{
"Question":'What is the capital of Italy?',
 "Answer":"Rome"
    }, "Question 6":{
"Question":'What is the capital of Spain?',
 "Answer":"Madrid"
    }, "Question 7":{
"Question":'What is the capital of Switzerland?',
 "Answer":"Bern"
    }
}
score = 0

for key, value in quiz.items():
    print('')
    print(value['Question'])
    answer = input("Answer?")

    if answer.lower() == value['Answer'].lower():
        print('correct')  
        score = score+1
        print("Your score is ",score)
    
    else:

        print("Wrong!")
        print("The answer is "+ value["Answer"])
        print("Your score is ", score)
        print('')
       

        
print("Game over.")
print("You got score "+ str(score) + " out of 7 questions correctly")
print("Your percentage is "+ str(int(score/7*100)) + "%")