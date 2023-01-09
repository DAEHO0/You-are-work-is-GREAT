import random

num = input('TCO는 몇 명입니까?(입력 값 범위: 3 ~ 6):  ')

if '1' <= num <= '2':
    print(f'TCO는 {num}명 입니다, {num}명으론 무리입니다.')
    print('다시 입력해주세요.')
    
elif num == '3':
    print(f'TCO는 {num}명 입니다.')
    print('TCO 이름을 입력해주세요.')
    TCO1 = input('TCO1:  ')
    print(f'TCO1은 {TCO1} 입니다.')
    TCO2 = input('TCO2:  ')
    print(f'TCO2은 {TCO2} 입니다.')
    TCO3 = input('TCO3:  ')
    print(f'TCO3은 {TCO3} 입니다.')
    tco = [TCO1, TCO2, TCO3]
    
elif num == '4':
    print(f'TCO는 {num}명 입니다.')
    print('TCO 이름을 입력해주세요.')
    TCO1 = input('TCO1:  ')
    print(f'TCO1은 {TCO1} 입니다.')
    TCO2 = input('TCO2:  ')
    print(f'TCO2은 {TCO2} 입니다.')
    TCO3 = input('TCO3:  ')
    print(f'TCO3은 {TCO3} 입니다.')
    TCO4 = input('TCO4:  ')
    print(f'TCO4은 {TCO4} 입니다.')
    tco = [TCO1, TCO2, TCO3, TCO4]
    
elif num == '5':
    print(f'TCO는 {num}명 입니다.')
    print('TCO 이름을 입력해주세요.')
    TCO1 = input('TCO1:  ')
    print(f'TCO1은 {TCO1} 입니다.')
    TCO2 = input('TCO2:  ')
    print(f'TCO2은 {TCO2} 입니다.')
    TCO3 = input('TCO3:  ')
    print(f'TCO3은 {TCO3} 입니다.')
    TCO4 = input('TCO4:  ')
    print(f'TCO4은 {TCO3} 입니다.')
    TCO5 = input('TCO5:  ')
    print(f'TCO5은 {TCO5} 입니다.')
    tco = [TCO1, TCO2, TCO3, TCO4, TCO5]
    
elif num == '6':
    print(f'TCO는 {num}명 입니다.')
    print('TCO 이름을 입력해주세요.')
    TCO1 = input('TCO1:  ')
    print(f'TCO1은 {TCO1} 입니다.')
    TCO2 = input('TCO2:  ')
    print(f'TCO2은 {TCO2} 입니다.')
    TCO3 = input('TCO3:  ')
    print(f'TCO3은 {TCO3} 입니다.')
    TCO4 = input('TCO4:  ')
    print(f'TCO4은 {TCO3} 입니다.')
    TCO5 = input('TCO5:  ')
    print(f'TCO5은 {TCO5} 입니다.')
    TCO6 = input('TCO6:  ')
    print(f'TCO6은 {TCO6} 입니다.')
    tco = [TCO1, TCO2, TCO3, TCO4, TCO5, TCO6]
    
else:
    print('입력 값 범위를 초과했습니다.')

num2 = input('TCA는 총 몇 명입니까?(입력 값 범위: 3 ~ 8):  ')

if '1' <= num2 <= '2':
    print(f'TCA는 총 {num2}명 입니다, {num2}명으론 무리입니다.')
    print('다시 입력해주세요.')
    
elif num2 == '3':
    print(f'TCA는 총 {num2}명 입니다.')
    print('TCA 이름을 입력해주세요.')
    TCA1 = input('TCA1:  ')
    print(f'TCA1은 {TCA1} 입니다.')
    TCA2 = input('TCA2:  ')
    print(f'TCA2은 {TCA2} 입니다.')
    TCA3 = input('TCA3:  ')
    print(f'TCA3은 {TCA3} 입니다.')
    tca = [TCA1, TCA2, TCA3]
    
elif num2 == '4':
    print(f'TCA는 총 {num2}명 입니다.')
    print('TCA 이름을 입력해주세요.')
    TCA1 = input('TCA1:  ')
    print(f'TCA1은 {TCA1} 입니다.')
    TCA2 = input('TCA2:  ')
    print(f'TCA2은 {TCA2} 입니다.')
    TCA3 = input('TCA3:  ')
    print(f'TCA3은 {TCA3} 입니다.')
    TCA4 = input('TCA4:  ')
    print(f'TCA4은 {TCA4} 입니다.')
    tca = [TCA1, TCA2, TCA3, TCA4]
    
elif num2 == '5':
    print(f'TCA는 총 {num2}명 입니다.')
    print('TCA 이름을 입력해주세요.')
    TCA1 = input('TCA1:  ')
    print(f'TCA1은 {TCA1} 입니다.')
    TCA2 = input('TCA2:  ')
    print(f'TCA2은 {TCA2} 입니다.')
    TCA3 = input('TCA3:  ')
    print(f'TCA3은 {TCA3} 입니다.')
    TCA4 = input('TCA4:  ')
    print(f'TCA4은 {TCA4} 입니다.')
    TCA5 = input('TCA5:  ')
    print(f'TCA5은 {TCA5} 입니다.')
    tca = [TCA1, TCA2, TCA3, TCA4, TCA5]
    
elif num2 == '6':
    print(f'TCA는 총 {num2}명 입니다.')
    print('TCA 이름을 입력해주세요.')
    TCA1 = input('TCA1:  ')
    print(f'TCA1은 {TCA1} 입니다.')
    TCA2 = input('TCA2:  ')
    print(f'TCA2은 {TCA2} 입니다.')
    TCA3 = input('TCA3:  ')
    print(f'TCA3은 {TCA3} 입니다.')
    TCA4 = input('TCA4:  ')
    print(f'TCA4은 {TCA4} 입니다.')
    TCA5 = input('TCA5:  ')
    print(f'TCA5은 {TCA5} 입니다.')
    TCA6 = input('TCA6:  ')
    print(f'TCA6은 {TCA6} 입니다.')
    tca = [TCA1, TCA2, TCA3, TCA4, TCA5, TCA6]
    
elif num2 == '7':
    print(f'TCA는 총 {num2}명 입니다.')
    print('TCA 이름을 입력해주세요.')
    TCA1 = input('TCA1:  ')
    print(f'TCA1은 {TCA1} 입니다.')
    TCA2 = input('TCA2:  ')
    print(f'TCA2은 {TCA2} 입니다.')
    TCA3 = input('TCA3:  ')
    print(f'TCA3은 {TCA3} 입니다.')
    TCA4 = input('TCA4:  ')
    print(f'TCA4은 {TCA4} 입니다.')
    TCA5 = input('TCA5:  ')
    print(f'TCA5은 {TCA5} 입니다.')
    TCA6 = input('TCA6:  ')
    print(f'TCA6은 {TCA6} 입니다.')
    TCA7 = input('TCA7:  ')
    print(f'TCA7은 {TCA7} 입니다.')
    tca = [TCA1, TCA2, TCA3, TCA4, TCA5, TCA6, TCA7]
    
elif num2 == '8':
    print(f'TCA는 총 {num2}명 입니다.')
    print('TCA 이름을 입력해주세요.')
    TCA1 = input('TCA1:  ')
    print(f'TCA1은 {TCA1} 입니다.')
    TCA2 = input('TCA2:  ')
    print(f'TCA2은 {TCA2} 입니다.')
    TCA3 = input('TCA3:  ')
    print(f'TCA3은 {TCA3} 입니다.')
    TCA4 = input('TCA4:  ')
    print(f'TCA4은 {TCA4} 입니다.')
    TCA5 = input('TCA5:  ')
    print(f'TCA5은 {TCA5} 입니다.')
    TCA6 = input('TCA6:  ')
    print(f'TCA6은 {TCA6} 입니다.')
    TCA7 = input('TCA7:  ')
    print(f'TCA7은 {TCA7} 입니다.')
    TCA8 = input('TCA8:  ')
    print(f'TCA8은 {TCA8} 입니다.')
    tca = [TCA1, TCA2, TCA3, TCA4, TCA5, TCA6, TCA7, TCA8]
     
else:
    print('입력 값 범위를 초과했습니다.')
    
num3 = input('COMMO는 총 몇 명입니까?(입력 값 범위: 3 ~ 8):  ')

if '1' <= num3 <= '2':
    print(f'COMMO는 총 {num3}명 입니다, {num3}명으론 무리입니다.')
    print('다시 입력해주세요.')
    
elif num3 == '3':
    print(f'COMMO는 총 {num3}명 입니다.')
    print('COMMO 이름을 입력해주세요.')
    COM1 = input('COM1:  ')
    print(f'COM1은 {COM1} 입니다.')
    COM2 = input('TCA2:  ')
    print(f'COM2은 {COM2} 입니다.')
    COM3 = input('TCA3:  ')
    print(f'COM3은 {COM3} 입니다.')
    com = [COM1, COM2, COM3]
    
elif num3 == '4':
    print(f'COMMO는 총 {num3}명 입니다.')
    print('COMMO 이름을 입력해주세요.')
    COM1 = input('COM1:  ')
    print(f'COM1은 {COM1} 입니다.')
    COM2 = input('TCA2:  ')
    print(f'COM2은 {COM2} 입니다.')
    COM3 = input('TCA3:  ')
    print(f'COM3은 {COM3} 입니다.')
    COM4 = input('TCA4:  ')
    print(f'COM4은 {COM4} 입니다.')
    com = [COM1, COM2, COM3, COM4]
    
elif num3 == '5':
    print(f'COMMO는 총 {num3}명 입니다.')
    print('COMMO 이름을 입력해주세요.')
    COM1 = input('COM1:  ')
    print(f'COM1은 {COM1} 입니다.')
    COM2 = input('TCA2:  ')
    print(f'COM2은 {COM2} 입니다.')
    COM3 = input('TCA3:  ')
    print(f'COM3은 {COM3} 입니다.')
    COM4 = input('TCA4:  ')
    print(f'COM4은 {COM4} 입니다.')
    COM5 = input('TCA5:  ')
    print(f'COM5은 {COM5} 입니다.')
    com = [COM1, COM2, COM3, COM4, COM5]
    
elif num3 == '6':
    print(f'COMMO는 총 {num3}명 입니다.')
    print('COMMO 이름을 입력해주세요.')
    COM1 = input('COM1:  ')
    print(f'COM1은 {COM1} 입니다.')
    COM2 = input('TCA2:  ')
    print(f'COM2은 {COM2} 입니다.')
    COM3 = input('TCA3:  ')
    print(f'COM3은 {COM3} 입니다.')
    COM4 = input('TCA4:  ')
    print(f'COM4은 {COM4} 입니다.')
    COM5 = input('TCA5:  ')
    print(f'COM5은 {COM5} 입니다.')
    COM6 = input('TCA6:  ')
    print(f'COM6은 {COM6} 입니다.')
    com = [COM1, COM2, COM3, COM4, COM5, COM6]
    
elif num3 == '7':
    print(f'COMMO는 총 {num3}명 입니다.')
    print('COMMO 이름을 입력해주세요.')
    COM1 = input('COM1:  ')
    print(f'COM1은 {COM1} 입니다.')
    COM2 = input('TCA2:  ')
    print(f'COM2은 {COM2} 입니다.')
    COM3 = input('TCA3:  ')
    print(f'COM3은 {COM3} 입니다.')
    COM4 = input('TCA4:  ')
    print(f'COM4은 {COM4} 입니다.')
    COM5 = input('TCA5:  ')
    print(f'COM5은 {COM5} 입니다.')
    COM6 = input('TCA6:  ')
    print(f'COM6은 {COM6} 입니다.')
    COM7 = input('TCA7:  ')
    print(f'COM7은 {COM7} 입니다.')
    com = [COM1, COM2, COM3, COM4, COM5, COM6, COM7]
    
elif num3 == '8':
    print(f'COMMO는 총 {num3}명 입니다.')
    print('COMMO 이름을 입력해주세요.')
    COM1 = input('COM1:  ')
    print(f'COM1은 {COM1} 입니다.')
    COM2 = input('TCA2:  ')
    print(f'COM2은 {COM2} 입니다.')
    COM3 = input('TCA3:  ')
    print(f'COM3은 {COM3} 입니다.')
    COM4 = input('TCA4:  ')
    print(f'COM4은 {COM4} 입니다.')
    COM5 = input('TCA5:  ')
    print(f'COM5은 {COM5} 입니다.')
    COM6 = input('TCA6:  ')
    print(f'COM6은 {COM6} 입니다.')
    COM7 = input('TCA7:  ')
    print(f'COM7은 {COM7} 입니다.')
    COM8 = input('TCA8:  ')
    print(f'COM8은 {COM8} 입니다.')
    com = [COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8]
     
else:
    print('입력 값 범위를 초과했습니다.')
    
tca_com = [tca, com]

n = input("해당 월을 입력해주세요\t:") # 해당 월 입력
if n == '1':
    def team(r_tco, r_tc, leave, off):
        print('-' * 23, ' 1월 ', '-' * 23)  # 1을 입력하면 1월 출력
        day = 1
        while day < 32: # 1월, 1 ~ 31일까지
            r_tco = random.choice(tco)  # TCO 1명 랜덤 추출
            r_tc = random.sample(tca_com, 2)    # TCA, COM 2명 중복 제외 랜덤 추출
            print(f'{day}일 : TCO = {r_tco}, TCA/COMMO = {r_tc}')
            print(f'근무퇴근 : {leave}')
            print(f'근무OFF  : {off}')
            day += 1
        print('-' * 53)
    team('tco', 'tca/commo', 'leave', 'off')
    
elif n == '2':
    def team(r_tco, r_tc, leave, off):
        print('-' * 23, ' 2월 ', '-' * 23)
        day = 1
        while day < 28: # 2월, 1 ~ 28일까지(또는 29일), 평년 윤년 구분 필요
            r_tco = random.choice(tco)
            r_tc = random.sample(tca_com, 2)
            print(f'{day}일 : TCO = {r_tco}, TCA/COMMO = {r_tc}')
            print(f'근무퇴근 : {leave}')
            print(f'근무OFF  : {off}')
            day += 1
        print('-' * 53)
    team('tco', 'tca/commo', 'leave', 'off')
    
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