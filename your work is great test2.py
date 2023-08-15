import random

tco = ['name', 'name', 'name', 'name']
tca = ['name', 'name', 'name', 'name', 'name', 'name', 'name']
com = ['name', 'name', 'name', 'name', 'name', 'name', 'name']

n = input("해당 월을 입력해주세요\t:") # 해당 월 입력
if n == '1':
    def team(r_tco, r_tca, r_com, leave, off):
        day = 1
        print("-" * 25, "ADEMR", "-" * 25)
        print("5M = 5, 15M = 15, 30M = 30, 1H = 1, Training = t, Clear = c")
        print("Week = w, Month = m, Quarter = q, Half = h, Year = y")
        print("")
        print("예시: 1일 날 5M이면 '5' 입력, 10일 날 Training이면 't' 입력")
        print("-" * 60)
        print("CODE를 입력해주세요")
    
        for day in range(1, 32):
            cod = input(f'{day}일 = ') # 잘못 입력하면 다시 입력할 수 있게끔 작성 필요
            if cod == '5':
                print(f'{day}일의 CODE는 5M 입니다.')
            elif cod == '15':
                print(f'{day}일의 CODE는 15M 입니다.')
            elif cod == '30':
                print(f'{day}일의 CODE는 30M 입니다.')
            elif cod == '1':
                print(f'{day}일의 CODE는 1H 입니다.')
            elif cod == 't':
                print(f'{day}일의 CODE는 Training 입니다.')
            elif cod == 'c':
                print(f'{day}일의 CODE는 Clear 입니다.')
            elif cod == 'w':
                print(f'{day}일의 CODE는 Week 입니다.')
            elif cod == 'm':
                print(f'{day}일의 CODE는 Month 입니다.')
            elif cod == 'q':
                print(f'{day}일의 CODE는 Quarter 입니다.')
            elif cod == 'h':
                print(f'{day}일의 CODE는 Half 입니다.')
            elif cod == 'y':
                print(f'{day}일의 CODE는 Year 입니다.')
            else:
                print("잘못 입력하셨습니다.")
        
        print('-' * 23, ' 1월 ', '-' * 23)  # 1을 입력하면 1월 출력
        day = 1
        while day < 32: # 1월, 1 ~ 31일까지
            r_tco = random.choice(tco)  # TCO 1명 랜덤 추출
            r_tca = random.choice(tca)  # TCA 1명 랜덤 추출
            r_com = random.choice(com)  # COMMO 1명 랜덤 추출
            if r_tca == r_com: # tca와 commo가 같으면 다시 랜덤
                r_tco = random.choice(tco)
                r_tca = random.choice(tca)
                r_com = random.choice(com)
                
# 여기에 근무퇴근, 근무OFF 변수 추가

            print(f'{day}일 : TCO = {r_tco}, TCA = {r_tca}, COMMO = {r_com}')
            print(f'근무퇴근 : {leave}')
            print(f'근무OFF  : {off}')
            day += 1
        print('-' * 53)
    team('tco', 'tca', 'com', 'leave', 'off')
    
#   1. 해당 월을 입력함
#       -> 몇 월인지 입력해주세요.
#   2. 사용자가 입력한 숫자대로 해당 월과 날짜 출력
#   3. code 입력
#       -> code를 입력해주세요.
#   4. 공휴일 등을 입력함
#       -> 휴일을 입력해주세요.
#   5. 입력한 값에 맞게끔 근무자의 근무퇴근 및 OFF 조정
#   !. 해당 날짜에 근무가 안 되는 조원도 고려해서 조정 가능?
    
# 23.8.15 -masking-
