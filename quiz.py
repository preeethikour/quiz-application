test=str(input("enter a name"))
class Question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer

question_prompts=[
  "what color are apples?\n(a)Red\n(b)Green\n (c)Orange\n your answer:",
  "what color are banana?\n(a)Red\n(b)Green\n (c)yellow\n your answer:",
]

questions=[
     Question(question_prompts[0],"a"),
     Question(question_prompts[1],"c")
]


def run_quiz(questions):
    score=0
    for question in questions:
         answer=input(question.prompt)
         if answer==question.answer:
            score+=1
    print("hi",test,"you got",score,"correct answer","out off",len(questions))

run_quiz(questions)
