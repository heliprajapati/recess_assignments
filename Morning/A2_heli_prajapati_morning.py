#For iteration we use loops
#For Loop 
fruits=["apple","banana"]
for fruit in fruits:
    print(fruit)
#While Loop
i = 1
while(i <= 5):
    print(i)
    i = i + 1

#control flow
#conditional statements(if, elif, else)
age=21
if age < 18:
    print("you are underage")# only executed if condition 1 is true
elif age >= 18 and age <=65:
    print("you are adult")#only executed if condition 2 is true
else:
    print("You are a senior citizen")

#Break & Continue
#Break statement
for number in range(1,10):
    if number == 5:
        break
    print(number)
#Continue statement
    for number in range(1,10):
        if number == 5:
            continue
        print(number)

#Exception handling (try, except, finally and raise)
try:
    x = 10/0
except ZeroDivisionError:
    print('Error:division by zero')
finally:
    print('This is always executed')


#Exercise 
#prompt students on scale of 1 to 10 to rate their mental health
print("*****************Exercise 1 output**************************************************************")
emotion = {
    1:"Try to be happy",
    2:'Nice',
    3:'I understand',
    4:'Am glad',
    5:'Thats great',
    6:'Good job!',
    7:'Wonderfull',
    8:'Okay',
    9:'Thats the spirit',
    10:'Alright',
}
student_emotion= input("On a scale of 1 to 10 how are you feeling today")
try:
    student_emotion = int(student_emotion)
except ValueError:
    print("Choose a number btw 1-10")
    exit()
#convert user input to lower case
#student_emotion = student_emotion.lower()
if student_emotion in emotion:
    print(emotion[student_emotion])
else:
    print("M sorry i dont understand, choose a number btw 1-10")

