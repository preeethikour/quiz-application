test=str(input("enter a name:"))
class Question:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

given_question=[
  "what color are apples?\n(a)Red\n(b)Green\n (c)Orange\n your answer:",
  "what color are banana?\n(a)Red\n(b)Green\n (c)yellow\n your answer:",
]

questions=[
     Question(given_question[0],"a"),
     Question(given_question[1],"c")
]


def run_quiz(questions):
    score=0
    for question in questions:
         answer=input(question.question)
         if answer==question.answer:
            score+=1
    print("hi",test,"you got",score,"correct answer","out off",len(questions))

run_quiz(questions)
