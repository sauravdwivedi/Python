"""Python script to print "Fizz" if a number is divisible by 3, print 
"Buzz" if a number is divisible by 5, and print "FizzBuzz" if a number 
is divisible by both 3 and 5 for numbers in a given range"""

def fizz_buzz(target):
    for x in range(target):
        if (x % 3 == 0) and (x % 5 == 0):
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
            
if __name__ == '__main__':
    target = int(input("Enter range of numbers: "))
    fizz_buzz(target)


