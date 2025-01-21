from sympy import *
from sympy.abc import x, y
import time
print("\nWelcome to Point Plotter Utility\n\n--------\n\nThis is for linear equation graphing on a rectangle coordinate system. This program gives you output on 7 different solutions in the form of ordered pairs from x = -3 to 3. May expand later.\nI hope this little tool helps! ^-^\n\n- Falon Freed, developer\n")
while True:
    str_expr = input("Enter your equation(Leave blank to exit): y = ")
    if str_expr == "":
        print("\nClosing...")
        time.sleep(1.5)
        break
    try:
        expr = sympify(str_expr)
        print("Displaying solutions where x = -3 to 3...")
        for i in range(-3, 4):
            print(f"({i}, {expr.subs(x, i)})")
    except:
        print("Expression invalid.")

    
