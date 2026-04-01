import random 
answer=[
    "try again",
    "betteer luck next time",
    "ask again later",
    "most likely",
    "sorry try again later",
    "don't overthink",
    "no chance!",
    "use your brain",
]

question = input ("ask your question:")

response=random.choice(answer)
print("magic 8 ball says",response)
 