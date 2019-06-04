from MainTest import Menu

@Menu
def MenuSecond():
    print("원하는 값을 선택하세요")
    a,b = map(int, input().split())
    Sum = a-b
    print("값은 : {0}입니다".format(Sum))

MenuSecond()
