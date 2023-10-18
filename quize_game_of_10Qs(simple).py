questions = [
  [
    "How many fingers in our hand ?", "two", "three", "five",
    "seven", 3
  ],
  [
    "How many fingers in our hand ?", "two", "three", "five",
    "seven", 3
  ],
   [
    "How many fingers in our hand ?", "two", "three", "five",
    "seven", 3
  ],
   [
    "How many fingers in our hand ? ", "two", "three", "five",
    "seven", 3
  ],
   [
    "How many fingers in our hand ?", "two", "three", "five",
    "seven", 3
  ],
   [
    "How many fingers in our hand ?", "two", "three", "five",
    "seven", 3
  ],
   [
    "How many fingers in our hand ?", "two", "three", "five",
    "seven", 3
  ],
   [
    "How many fingers in our hand ?", "two", "three", "five",
    "seven", 3
  ],
   [
    "How many fingers in our hand ?", "two", "three", "five",
    "seven", 3
  ],
   [
    "How many fingers in our hand ?", "two", "three", "five",
    "seven", 3
  ],
  
]

points = [5, 5, 10, 10, 15, 20, 25, 25, 30, 30]
total_points = 0

print("This quiz game is consist of 10 questions, every quesion has it's own points")
for i in range(0, len(questions)):
  
  question = questions[i]
  
  print(f"\nQuestion for points {points[i]}")
  print("\n")
  print(question[0])
  print(f"1. {question[1]}          2. {question[2]} ")
  print(f"3. {question[3]}          4. {question[4]} ")
  print("\n")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    total_points = points[i-1]
    break
  if(reply == question[-1]):
    print(f"\nCorrect answer, You got {points[i]} points")
    total_points= points[i]+total_points
  else:
    print("Wrong answer!")
    
print('Game finished')
print(f"Your total points are {total_points}")




