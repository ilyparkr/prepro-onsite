"""Ddd"""
def main():
    """DDD"""
    money = int(input())
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    
    money1 = money - water
    if money1 % 3 == 0:
        money1 -= 10 * snack1
        cast1 = 10 * snack1
    elif money1 % 3 == 1:
        money1 -= 15 * snack1
        cast1 = 15 * snack1
    elif money1 % 3 == 2:
        money1 -= 20 * snack1
        cast1 = 20 * snack1

    if money1 % 3 == 0:
        money1 -= 12 * snack2
        cast2 = 12 * snack2
    elif money1 % 3 == 1:
        money1 -= 15 * snack2
        cast2 = 15 * snack2
    elif money1 % 3 == 2:
        money1 -= 18 * snack2
        cast2 = 18 * snack2

    if money1 % 3 == 0:
        money1 -= 5 * snack3
        cast3 = 5 * snack3
    elif money1 % 3 == 1:
        money1 -= 7 * snack3
        cast3 = 7 * snack3
    elif money1 % 3 == 2:
        money1 -= 9 * snack3
        cast3 = 9 * snack3
    
    if money1 < 0:
        print("Now you have %d left" %money)
        print('You don’t have enough money!')
    else:
        print("Now you have %d left" %money1)
        print("Here's your order!")
        print("Water: %d baht" % water)
        print("Snack number 1: %d baht" % cast1)
        print("Snack number 2: %d baht" % cast2)
        print("Snack number 3: %d baht" % cast3)

main()
