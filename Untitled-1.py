"""DDD"""
def main():
    """DDD"""
    grade = float(input())
    if grade < 1.00:
        print("I'm so sad.")
    elif grade < 2.00:
        grade = 4.00 - grade
        print("%.2f" %(grade))
    else:
        print("I'm so happy.")
main()
