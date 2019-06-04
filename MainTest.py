from random import randint

class Menu:
    def __init__(self, Menu):
        self.FirstMenu = Menu
        self.SecondMenu = Menu
        self.ThirdMenu = Menu
        self.FourthMenu = Menu
        self.Default = Menu
        
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
                MenuList.append(MenuThird)
            elif MenuList is 4:
                self.FourthMenu()
                MenuList.append(MenuFourth)
            else:
                print("버튼을 다시 선택해주세요")
                self.Default()
                MenuList.append(SetDefault)

            



