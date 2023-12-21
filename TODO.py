import testTwilio1
import time
import random

run = True
list_to_do = []
list_to_do_time = []
list_of_deadline = []
combineTime = []
Quotes = [
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. -Christian D. Larson",
    "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. -Steve Jobs",
    "You don't have to be great to start, but you have to start to be great. -Zig Ziglar",
    "The only person you are destined to become is the person you decide to be. -Ralph Waldo Emerson",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. -Winston Churchill",
    "Believe you can and you're halfway there. -Theodore Roosevelt",
    "The best way to predict the future is to invent it. -Alan Kay",
    "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
    "The best preparation for tomorrow is doing your best today. -H. Jackson Brown Jr.",
    "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
    "If you want to achieve greatness stop asking for permission. -Anonymous",
    "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
    "I have not failed. I've just found 10,000 ways that won't work. -Thomas Edison",
    "It does not matter how slowly you go as long as you do not stop. -Confucius",
    "The only thing standing between you and your goal is the story you keep telling yourself that you can't achieve it. -Jordan Belfort",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. -Helen Keller",
    "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. -Jimmy Dean",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. -Zig Ziglar",
    "The only way to do great work is to love what you do. -Steve Jobs",
    "You miss 100% of the shots you don't take. -Wayne Gretzky",
    "The only source of knowledge is experience. -Albert Einstein",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. -Helen Keller",
    "The best way to find yourself is to lose yourself in the service of others. -Mahatma Gandhi",
    "The only thing we have to fear is fear itself. -Franklin D. Roosevelt",
    "The journey of a thousand miles begins with one step. -Lao Tzu",
    "The only true wisdom is in knowing you know nothing. -Socrates",
    "The only thing necessary for the triumph of evil is for good men to do nothing. -Edmund Burke",
    "The best revenge is massive success. -Frank Sinatra",
    "The only thing we know for sure is that we know nothing at all. -Socrates",
    "The only thing worse than being blind is having sight but no vision. -Helen Keller",
    "The only thing standing between you and your goal is the bullshit story you keep telling yourself as to why you can't achieve it. -Jordan Belfort",
    "The only way to have a good day is to start it with a positive attitude. -Anonymous",
    "The only way to do great work is to love what you do. -Steve Jobs"
]
num_of_tasks = eval(input("Enter no of tasks to complete: "))

dicTime = {}

for i in range(num_of_tasks):
    print(f"Task{i + 1}:")
    list_to_do.append(input(f"Enter Task{i + 1}: "))
    list_to_do_time.append(input(f"Enter time to start (HH:MM): "))
    list_of_deadline.append(input(f"Enter deadline Time (HH:MM): "))


for i in range(num_of_tasks):
    l1 = [list_to_do_time[i], list_of_deadline[i]]
    combineTime.append(l1)

for keys, values in zip(list_to_do, combineTime):
    dicTime[keys] = values

print(f"Have to complete following tasks! \n{list_to_do}, {list_of_deadline}, {list_to_do_time}")
# while 1:
#     if int(time1[:2]) == localTimeHour and int(time1[3:]) == localTimeMin:
#         testTwilio1.MessageNotify(f"Time to Perform Task: {list_to_do[0]} \nDeadline: {list_of_deadline[0]}", "+916296790017")
#         print("Message sent")

warningTimeHour = 0
warningTimeMin = 0
dicKeys = list(dicTime.keys())
dicKeysCpy = dicKeys.copy()

while run:
    # for i in range(len(dicKeys)):
    warningTimeHour = int(dicTime[f"{dicKeysCpy[0]}"][0][:2])   # indexing problem<-- 23:20
    warningTimeMin = int(dicTime[f"{dicKeysCpy[0]}"][0][3:])

    if warningTimeHour == time.localtime().tm_hour and warningTimeMin == time.localtime().tm_min:
        testTwilio1.MessageNotify(f"\tTime to Act on: '{dicKeysCpy[0]}'\nDeadline: {dicTime[f'{dicKeysCpy[0]}'][1]}"
                                  f"\n- - - -"
                                  f"\n{Quotes[random.randint(0, len(Quotes) - 1)]}", "+916296790017")

        print(f"Message sent! for - {dicKeysCpy[0]}")

        # pop the dictionary -
        dicTime.pop(dicKeysCpy[0])
        dicKeysCpy.pop(0)
        print(dicKeysCpy)

    if len(dicKeysCpy) == 0:
        run = False
