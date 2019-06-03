from random import randint



class Menu:
    def __init__(self, Menu):
        self.FirstMenu = Menu
        self.SecondMenu = Menu
        self.ThirdMenu = Menu
        self.FourthMenu = Menu
        self.Default = Menu

    # def print_menu(self):
    #     print("Init...")
    #     print("원하시는 버튼을 선택하세요")
    #     MenuInput = input()
    #     return int(MenuInput)

    def __call__(self):
        print("원하시는 버튼을 선택하세요")
        MenuInput = input()
        MenuList = []
        while 1:
            if MenuInput is 1:
                self.FirstMenu()
                MenuList.append(MenuFirst)
            elif MenuInput is 2:
                self.SecondMenu()
                MenuList.append(MenuSecond)
            elif MenuInput is 3:
                self.ThirdMenu()
                MenuList.append(MenuThrid)
            elif MenuInput is 4:
                self.FourthMenu()
                MenuList.append(MenuFourth)
            else:
                self.Default()
                MenuList.append(SetDefault)


@Menu
def MenuFirst():
    print("원하는 연산 값을 선택하세요")
    a, b = map(int, input().split())
    Sum = a + b
    print("값은 : {0}입니다.".format(Sum))

    n = randint(1, 100)

    while True:
        ans = input("Guess my number (Q to exit): ")
        if ans.upper() == "Q":
            break
        ians = int(ans)
        if n is ians:
            print("Correct!")
            SetDefault()
        elif n > ians:
            print("Choose higher number")
        else:
            print("Choose lower number")
    # return Sum


def MenuSecond():
    print("원하는 연산 값을 선택하세요")
    a, b = map(int, input().split())
    Sum = a - b
    print("값은 : {0}입니다.".format(Sum))
    # return Sum


def MenuThrid():
    print("원하는 연산 값을 선택하세요")
    a, b = map(int, input().split())
    Sum = a * b
    print("값은 : {0}입니다.".format(Sum))
    # return Sum


def MenuFourth():
    print("원하는 연산 값을 선택하세요")
    a, b = map(int, input().split())
    Sum = a / b
    print("값은 : {0}입니다.".format(Sum))
    # return Sum


def SetDefault():
    print("프로그램 종료...")
    exit(0)


MenuFirst()
MenuSecond()
MenuThrid()
MenuFourth()
SetDefault()
