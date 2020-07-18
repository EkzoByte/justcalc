import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.GREEN + "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("&&&&&&&&       &&&&&&&&&&          &&&&&&&")
print("&&&&&&&  &&&&&&&&&&&&&&&&  &&&&&&&&  &&&&&")
print("&&&&&&  &&&&&&&&&&&&&&&&&  &&&&&&&&  &&&&&")
print("&&&&&&  &&&&&&&&&&&&&&&&&  &&&&&&&&  &&&&&")
print("&&&&&&  &&&&&&&&&&&&&&&&&  &&&&&&&&  &&&&&")
print("&&&&&&  &&&&&&&&&&&&&&&&&            &&&&&")
print("&&&&&&  &&&&&&&&&&&&&&&&&  &&&&&&&&&&&&&&&")
print("&&&&&&  &&&&&&&&&&&&&&&&&  &&&&&&&&&&&&&&&")
print("&&&&&&  &&&&&&&&&&&&&&&&&  &&&&&&&&&&&&&&&")
print("&&&&&&  &&&&&&&&&&&&&&&&&  &&&&&&&&&&&&&&&")
print("&&&&&&  &&&&&&&&&&&&&&&&&  &&&&&&&&&&&&&&&")
print("&&&&&&&  &&&&&&&&&&&&&&&&  &&&&&&&&&&&&&&&")
print("&&&&&&&&      &&&&&&&&&&&  &&&&&&&&&&&&&&&")
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

print(Style.RESET_ALL)

print("\033[36m{}\033[0m".format("Ноль в качестве знака операции"
      "\nзавершит работу программы"))
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in (F'+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("\033[31m{}\033[0m".format("Деление на ноль!"))
    else:
        print("\033[31m{}\033[0m".format("Неверный знак операции!"))