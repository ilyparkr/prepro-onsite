"""DDD"""
def main():
    """DLDDL"""
    tape = int(input())
    ans = 0
    if tape == 0:
        print("No Tape Measure")
    else:
        while True:
            measure = input()
            if measure == "No more!":
                break
            else:
                for i in range(1, tape+1):
                    if i == int(measure):
                        ans += i
        if ans == 0:
            print("Not Found Number")
        else:
            print("Sum of Found Number = %d" %ans)
main()
