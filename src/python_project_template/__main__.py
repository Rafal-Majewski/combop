from .mymathpackage import is_even

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"{number} is " + ("even" if is_even(number) else "odd"))
