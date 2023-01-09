# def team(tco, tca, com):
#     print('-' * 23, ' n월 ', '-' * 23) # 해달 월 입력
#     print(f'n일\t: TCO = {tco}, TCA = {tca}, COMMO = {com}')
#     # 해당 월에 맞게 해당 날짜까지 출력(예: 3월을 입력하면 31일까지 출력)
#     print('-' * 53)
    
# team('조성원', '김대호', '한대인')
import random

tco = ['이원찬', '조성원', '정민서', '박선빈']
tca = ['김동규', '박상준', '방지언', '박진호', '정광렬', '김대호', '한대인']
com = ['김동규', '박상준', '방지언', '박진호', '정광렬', '김대호', '한대인']

# 당일 근무자는 다음 날 근무자가 될 수 없다 

n = input("해당 월을 입력해주세요\t:") # 해당 월 입력
if n == '1':
    def team(r_tco, r_tca, r_com, leave, off):
        print('-' * 23, ' 1월 ', '-' * 23)  # 1을 입력하면 1월 출력
        day = 1
        while day < 32: # 1월, 1 ~ 31일까지
            r_tco = random.choice(tco)  # TCO 1명 랜덤 추출
            r_tca = random.choice(tca)   # TCA 1명 랜덤 추출
            r_com = random.choice(com)   # TCA 1명 랜덤 추출
            if r_tca == r_com: # tca와 commo가 같으면 다시 랜덤
                r_tco = random.choice(tco)
                r_tca = random.choice(tca)
                r_com = random.choice(com)
            print(f'{day}일 : TCO = {r_tco}, TCA = {r_tca}, COMMO = {r_com}')
            print(f'근무퇴근 : {leave}')
            print(f'근무OFF  : {off}')
            day += 1
        print('-' * 53)
    team('tco', 'tca', 'com', 'leave', 'off')
    
# 이 코드를 n월을 입력하면 m일도 자동으로 변경되어 m일에 맞게끔 변경하면?
    
# elif n == '2':
#     def team(r_tco, r_tc, leave, off):
#         print('-' * 23, ' 2월 ', '-' * 23)
#         day = 1
#         while day < 28: # 2월, 1 ~ 28일까지(또는 29일), 평년 윤년 구분 필요
#             r_tco = random.choice(tco)
#             r_tc = random.sample(tca_com, 2)
#             print(f'{day}일 : TCO = {r_tco}, TCA/COMMO = {r_tc}')
#             print(f'근무퇴근 : {leave}')
#             print(f'근무OFF  : {off}')
#             day += 1
#         print('-' * 53)
#     team('tco', 'tca/commo', 'leave', 'off')
    
#   1. 해당 월을 입력함
#       -> 몇 월인지 입력해주세요.
#   2. 사용자가 입력한 숫자대로 해당 월과 날짜 출력
#   3. code 입력
#       -> code를 입력해주세요.
#   4. 공휴일 등을 입력함
#       -> 휴일을 입력해주세요.
#   5. 입력한 값에 맞게끔 근무자의 근무퇴근 및 OFF 조정
#   !. 해당 날짜에 근무가 안 되는 조원도 고려해서 조정 가능?
    
# 22.11.13 -내용 수정-