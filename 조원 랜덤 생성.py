import random

tco = []
tca_com = []

#   -> 근무자 랜덤 생성, 리스트 안 객체들을 무작위로 생성해내는 코드 필요(O)
#      단, tca와 com 랜덤하게 생성하되 tca와 com은 같으면 안 됨(O)
#      당일 근무자는 다음 날 근무를 설 수 없음(이틀 연속으로 근무 못 함)

n = input("해당 월을 입력해주세요\t:")
if n == '1':
    def team(r_tco, r_tca, r_com, leave, off):
        print('-' * 23, ' 1월 ', '-' * 23) # 해당 월 입력
        day = 1
        while day < 32: # 1월, 1 ~ 31일까지
            r_tco = random.choice(tco)  # TCO 1명 랜덤 추출
            r_tc = random.sample(tca_com, 2)    # TCA, COM 2명 중복 제외 랜덤 추출
            print(f'{day}일 : TCO = {r_tco}, TCA/COMMO = {r_tc}')
            print(f'근무퇴근 : {leave}')
            print(f'근무OFF  : {off}')
            day += 1
        print('-' * 53)
    team( 'tco','tca', 'com', 'leave', 'off')