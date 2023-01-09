# 월 마다 공휴일 수가 다르다
#a, b, c, d, e, f = map(int, input("공휴일을 지정해 주세요.\t:").split())

n = input("해당 월을 입력해주세요\t:") # 해당 월 입력
if n == '1':
    while n < '2':
        print("(공)휴일을 지정해주세요")
        day_off = input()
        print(f'{day_off}일은 휴일입니다.')
        if input == "":
            break