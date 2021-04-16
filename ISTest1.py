"""
The program is made to determine which method of payment is better (pays more $)

First option pays flat $100 per day for 10 days.
Second option pays $1 for the first day and doubles amound each day for 10 days.

option1 will output 100 * 10 days
option2 will loop 10 times, addgit ing to previous total, doubling the amount each time and adding to total

If total amount for each option is equal, output "Option 1 and Option 2 pays the same"
If option1 pays better, we output "Option 1 is better"
If option2 pays better, we output "Option 2 is better"
"""

"""
# option1
return 10 * 100

# option2
pay_2 = 1
total_2 = 0
for i=1 to 10
total_2 = total_2 + pay_2
pay_2 = 2*pay_2

# main
If option1 == option2
"Option 1 and 2 pays the same"
if option1 < option 2
"Option 2 is better"
else
"Option 1 is better"


"""
def option1():
    return 10 * 100

def option2():
    amount =1
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *= 2
    total = sum(list1)
    return total

def main():
    answer = " "
    opt1 = option1()
    opt2 = option2()
    if opt1 == opt2:
        answer = "Option 1 and Option 2 pays the same"
    if opt1 < opt2:
        answer = "Option 2 is better"
    else:
        answer = "Option 1 is better"
    print(answer)

main()