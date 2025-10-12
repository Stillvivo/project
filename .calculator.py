class calculator:
    def add(self, *args):
        return sum(args)

    def sub(self, *args):
        if len(args) < 2:
            return "can't operate on more than 2 arguments"
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(self, *args):
        if len(args) < 2:
            return "can't operate on more than 2 arguments"
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "can't divide by zero"
            result /= num
            return result


calc = calculator()
while True:
    print("please choice your operation")
    print("1.add(+)")
    print("2.sub(-)")
    print("3.multiply(*)")
    print("4.divide(/)")
    print("5.exit")
    choice = input("please choice your options:")
    if choice == "5":
        print("GoodBye")
        break
    if choice not in ["1", "2", "3", "4", "5"]:
        print("invalid choice")
        continue
    while True:
        try:
            numbers = input("please enter your numbers with space:").split()
            numbers = [float(n) for n in numbers]
            if len(numbers) == 0:
                print("plese enter a number")
                continue
            break
        except ValueError:
            print("please enter number.not word!!")
            continue

    if choice == "1":
        print("result is: ", calc.add(*numbers))
    if choice == "2":
        print("result is: ", calc.sub(*numbers))
    if choice == "3":
        print("result is :", calc.multiply(*numbers))
    if choice == "4":
        print("result is: ", calc.divide(*numbers))
