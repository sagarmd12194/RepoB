class Calculator:
    def add_func(self,num1,num2):
        print("Addition Function is Started...")
        return num1+num2


def main():
    calc=Calculator()
    num1,num2=10,20
    result=calc.add_func(num1,num2)
    print("Addition of %d and %d = %d"%(num1,num2,result))

if __name__ == '__main__':
    main()


