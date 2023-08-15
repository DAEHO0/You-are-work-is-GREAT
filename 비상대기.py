# two = 5, three = 15, four = 30, five = 1 hour
# 프로그램 상으론 어느 요일이 몇 일인지 알 수 없음 -> 날짜 구분 프로그램 필요
# 1월 이면 어느 날짜가 어느 요일인지 알아야 함 -> 그래야 근무퇴근 및 off 조정 가능

print("-" * 25, "ADEMR", "-" * 25)
print("5M = 5, 15M = 15, 30M = 30, 1H = 1, Training = t, Clear = c")
print("Week = w, Month = m, Quarter = q, Half = h, Year = y")
print("")
print("예시: 1일 날 5M이면 '5' 입력, 10일 날 훈련이면 '훈' 입력")
print("-" * 60)

n = input("해당 월을 입력해주세요\t:") # 해당 월 입력
if n == '1':
    print("CODE를 입력해주세요")
    for i in range(1, 32):
        cod = input(f'{i}일 = ') # 잘못 입력하면 다시 입력할 수 있게끔 작성 필요
        if cod == '5':
            print(f'{i}일의 CODE는 5M 입니다.')
        elif cod == '15':
            print(f'{i}일의 CODE는 15M 입니다.')
        elif cod == '30':
            print(f'{i}일의 CODE는 30M 입니다.')
        elif cod == '1':
            print(f'{i}일의 CODE는 1H 입니다.')
        elif cod == 't':
            print(f'{i}일의 CODE는 Training 입니다.')
        elif cod == 'c':
            print(f'{i}일의 CODE는 Clear 입니다.')
        elif cod == 'w':
            print(f'{i}일의 CODE는 Week 입니다.')
        elif cod == 'm':
            print(f'{i}일의 CODE는 Month 입니다.')
        elif cod == 'q':
            print(f'{i}일의 CODE는 Quarter 입니다.')
        elif cod == 'h':
            print(f'{i}일의 CODE는 Half 입니다.')
        elif cod == 'y':
            print(f'{i}일의 CODE는 Year 입니다.')
        else:
            print("잘못 입력하셨습니다.")
        
        
        
# cod = input("비상대기를 입력해주세요\t:")
# if cod == '1':
#     for i in range(1,32):
#         print(input(f'{i}일 ='))
