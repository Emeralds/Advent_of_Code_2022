""" Input example
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

## Find the Elf carrying the most Calories. How many total Calories is that Elf carrying? In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

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

# Answer Part 1
print("Part 1 - Highest sum of calories is:", calories[-1])

# Answer Part 2
print("Part 2 - Sum of top 3 elves calories is:", (calories[-1]+calories[-2]+calories[-3]))