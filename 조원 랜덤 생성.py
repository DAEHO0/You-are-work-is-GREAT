import random

tco = ['이원찬', '조성원', '정민서', '박선빈']
tca = ['김동규', '박상준', '방지언', '박진호', '정광렬', '김대호', '한대인']
com = ['한대인', '김대호', '정광렬', '박진호', '방지언', '박상준', '김동규']

#   -> 근무자 랜덤 생성, 리스트 안 객체들을 무작위로 생성해내는 코드 필요(O)
#      단, tca와 com 랜덤하게 생성하되 tca와 com은 같으면 안 됨(O)
#      당일 근무자는 다음 날 근무를 설 수 없음(이틀 연속으로 근무 못 함)
'''
day = 0

while day < 32: 
    r_tco = random.choice(tco) # TCO 1명 랜덤 추출
    r_tc = random.sample(tca_com, 2) # TCA, COM 2명 중복 제외 랜덤 추출
#       -> 각 날마다 tco, tca_com 모두 달라야 함
    print(day, '일', r_tco, r_tc)
    day += 1
'''

n = input("해당 월을 입력해주세요\t:")
if n == '1':
    def team(r_tco, r_tca, r_com, leave, off):
        print('-' * 23, ' 1월 ', '-' * 23) # 해당 월 입력
        day = 1
        while day < 32: # 1월, 1 ~ 31일까지
            r_tco = random.choice(tco) # TCO 1명 랜덤 추출
            r_tca = random.choice(tca) # TCA 1명 랜덤 추출
            r_com = random.choice(com) # COMMO 1명 랜덤 추출
            print(f'{day}일\t: TCO = {r_tco}, TCA = {r_tca}, COMMO = {r_com}')
            print(f'근무퇴근 : {leave}')
            print(f'근무OFF  : {off}')
            day += 1
        print('-' * 53)
    team( 'tco','tca', 'com', 'leave', 'off')