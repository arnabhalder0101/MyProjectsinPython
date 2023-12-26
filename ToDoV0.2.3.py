import testTwilio1
import pushBulletSetup
import time
import random
import pywhatkit


# updates -
# -------
# Function for to-do list - use schedule (later)
# arrange times orderly manner
# user can add in any time format - not only 24 hours needed! Fix it!
# write what the code does for future use
# add code to send remainder for deadline is coming in 5 mins! Finish the job...
# task time must be at least 2 mins; no lesser allowed
# To Notify in the meantime,(avg time notify the) user if the diff bet deadline and starting is more than 6 hours!
# -----------------


def timeMinDiff(t1, t2):
    tH1 = int(t1[:2])
    tH2 = int(t2[:2])
    tM1 = int(t1[3:])
    tM2 = int(t2[3:])
    mins_ = abs(tH1 - tH2) * 60 + abs(tM1 - tM2)
    return mins_


# Initializations
run = True
list_to_do = []
list_to_do_time = []
list_of_deadline = []
combineTime = []
titleStart = "Act on 😤: "
titleFinish = "Time is ticking ⏰⏱: "
Quotes = [
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. -Christian D. Larson",
    "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. -Steve Jobs",
    "You don't have to be great to start, but you have to start to be great. -Zig Ziglar",
    "The only person you are destined to become is the person you decide to be. -Ralph Waldo Emerson",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. -Winston Churchill",
    "Believe you can and you're halfway there. -Theodore Roosevelt",
    "The best way to predict the future is to invent it. -Alan Kay",
    "Just do your duty, God will give what you deserve. If you do 100 will get 100, do 90, will only get 90. -Bhagabad Gita",
    "Do your job people will do there -Unknown",
    "Be disciplined! Decide you're a Winner or a Fucking Looser. Do what you're supposed to do! Be Disciplined... -Andrew Tate",
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

sec = 0
n = 0
varSpot = 0

# inputs from user
while n != num_of_tasks:
    print(f"Task{n + 1}:")
    task = input(f"Enter Task{n + 1}: ")
    time_todo = input(f"Enter time to start (HH:MM): ")
    time_finish = input(f"Enter deadline Time (HH:MM): ")

    # throw alert for invalid inputs
    if int(time_todo[:2]) > 24 or int(time_todo[3:]) > 59 or int(time_finish[:2]) > 24 or int(time_finish[3:]) > 59:
        print("*** Invalid Time inputs! ***")
        print("Eg, 13:60 not possible. Write 14:00 instead")
        print("Minutes can't be more than 59 & hours can't be more than 24.")
        continue

    # task time must be at least 3 mins; no lesser allowed
    if timeMinDiff(time_todo, time_finish) <= 3:
        print("\nTime for a task must me at least 3 minutes.")
        print("***Please maintain the Ethics! Enter valid Timings...***\n")
        continue

    # if the 2nd task start time is between the start & ending of 1st task, through invalid starting time,
    # tell him start 2nd task after
    # completing the 1st one!
    if n > 0:
        # comparing the difference with n-1 value and recent value
        if timeMinDiff(list_to_do_time[n - 1], list_of_deadline[varSpot]) > timeMinDiff(list_to_do_time[n - 1],
                                                                                        time_todo):
            print("\n***Invalid Time for start the work!***")
            print("You must finish the 1st Task, before starting the 2nd Task!")
            print(f"Enter Task{n + 1} again:")
            continue

        varSpot += 1  # getting proper spot index for line 91; updating it if, IF condition is false!

    list_to_do.append(task)
    list_to_do_time.append(time_todo)
    list_of_deadline.append(time_finish)
    n += 1

# storing in list and packing in dictionary for better uses of the user data/time
for i in range(num_of_tasks):
    l1 = [list_to_do_time[i], list_of_deadline[i]]
    combineTime.append(l1)

for keys, values in zip(list_to_do, combineTime):
    dicTime[keys] = values

print(
    f"\nHave to complete following tasks! \n{list_to_do}, Starting time: {list_to_do_time}, Deadline: {list_of_deadline}")

dicKeys = list(dicTime.keys())
print(dicTime, "\n")
while run:
    # taking the 0th key-always,as, when 1st notification send -> pop it out, so next task comes in the 0th index!
    warningTimeHour = int(dicTime[f"{dicKeys[0]}"][0][:2])
    warningTimeMin = int(dicTime[f"{dicKeys[0]}"][0][3:])
    warningTimeSec = 1  # AT the 1st second, of that min, hour I need the notification

    # Deadline Notification
    deadlineHour = int(dicTime[f"{dicKeys[0]}"][1][:2])
    deadlineMin = int(dicTime[f"{dicKeys[0]}"][1][3:]) - 2  # 2 min prior notify user

    # only goes inside the loop if sec == 1; so, only once message will be sent to the user;
    if warningTimeHour == time.localtime().tm_hour and warningTimeMin == time.localtime().tm_min and warningTimeSec == time.localtime().tm_sec:
        messageS = f"'{dicKeys[0]}'\nDeadline: {dicTime[f'{dicKeys[0]}'][1]}\n- - - -" \
                   f"\n{Quotes[random.randint(0, len(Quotes) - 1)]}"

        pushBulletSetup.PushMessage(titleStart, messageS)

        # except:
        #     pywhatkit.sendwhatmsg("+916296790017", messageS, time_hour=warningTimeHour,
        #                           time_min=warningTimeMin,
        #                           wait_time=20, tab_close=True, close_time=5)
        # finally:
        #     print(f"\nMessage sent! for - {dicKeys[0]}\n")

    if deadlineHour == time.localtime().tm_hour and deadlineMin == time.localtime().tm_min and warningTimeSec == time.localtime().tm_sec:
        messageF = f"2 mins left to complete: '{dicKeys[0]}'\nDeadline: {dicTime[f'{dicKeys[0]}'][1]}\n- - - -" \
                   f"\n{Quotes[random.randint(0, len(Quotes) - 1)]}"
        pushBulletSetup.PushMessage(titleFinish, messageF)
        print(f"\nDeadline Message sent! for - {dicKeys[0]}\n")

        # pop the dictionary -
        dicTime.pop(dicKeys[0])
        dicKeys.pop(0)
        print(f"\n{len(dicKeys)} Tasks left: {dicKeys}")

    if len(dicKeys) == 0:
        print("So, Here we're done with all your tasks! \nThanks for using this program! \nSee you soon...")
        run = False
        continue

    print(sec, end=" ")
    sec += 1
    time.sleep(1)
