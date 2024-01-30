# Bill Splitter for expanse sharing --

n = int(input("Enter total number of people: "))

# add feature names, to make it more personalized,
# ask user if he wants this feature of not -- choice == 0 / 1

names_person = []
expanses = []
toBePaid = []

for l in range(n):
    expanses.append(int(input(f"Enter amount for person {l + 1}: ")))

for k in range(n):
    toBePaid.append(0)

for i in range(n):
    money = expanses[i] / n
    # print(money)
    for j in range(n):
        if j == i:
            toBePaid[j] += 0
        else:
            toBePaid[j] += money

# to Whom have to pay
per_head_sum_cost = sum(expanses) / n

print(f"\nPer head expanses = {per_head_sum_cost}")
print("Total expanses in the journey for each people: ", expanses)
print("Each Person have to pay this much money: ", toBePaid)

for i in range(n):
    m = toBePaid[i]
    to_whom = []
    up = []
    for r in range(n):
        if r == i:
            pass
        else:
            to_whom.append(r + 1)  # to whom that person will pay his money
            up.append(expanses[r])

    down = sum(up)

    print(f"\nPerson {i + 1}--")
    for t in range(n - 1):
        pay = (m * up[t]) // down  # how much money he will pay to whom:
        print(f"Person {i + 1} has to pay to person {to_whom[t]}: Rs. {pay}/-")
