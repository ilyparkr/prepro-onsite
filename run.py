"""DDD"""
def main():
    """ddD"""
    var_total = 0
    var_pos = 0
    var_input = [float(i) for i in input().split()]
    for i in var_input:
        var_total += abs(var_pos - i)
        var_pos = i
    print("%.2f" %var_total)
main()
