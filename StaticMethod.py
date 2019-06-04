from MainTest import Menu


@Menu
def MenuFirst():
    print("원하는 값을 선택하세요")
    a,b = map(int, input().split())
    Sum = a+b
    print("값은 : {0}입니다".format(Sum))

    n = randint(1, 100)
    while True:
        ans = input("Guess my Number (1 ~ 100)")
        if ans.upper() == 'Q':
            break
        ians = int(ans)
        if n is ians:
            print("Correct!")
            SetDefault()

        elif n > ians:
            print("Choose Higher number")
        else:
            print("Choose lower number")


MenuFirst()
