import random
"""
Hanoi tower
Move all the panel from A to C and small panel only can put above the big panel

base question:
1.Move n-1 panel from A to B via C
2.Move nth panel from A to C
3.Move n-1 panel from B to C via A
"""
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, b, c)
        print("Moving from %s to %s" % (a,c))
        hanoi(n-1, b, a, c)

if __name__ == "__main__":
    hanoi(7, 'A', 'B', 'C')