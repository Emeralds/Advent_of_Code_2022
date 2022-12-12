## Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

text_file = open("Day 1\Day1_Input.txt", "r")
lines = text_file.readlines()
text_file.close()

calories =[]
a = 0
for x in lines:
    if (x == "") or (x =="\n"):
        calories.append(a)
        a = 0
    else:
        a = a + int(x)
calories.sort()
print("Sum of top 3 elves calories is:", (calories[-1]+calories[-2]+calories[-3]))