# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')
answer = 0

for i in range(len(data)):
    num = int(data[i])
    
    if i == 0:
        print(f'{num}', end='')
        answer += num
    elif answer == 1 or num == 1 or answer == 0 or num == 0:
        answer += num
        print(f' + {num}', end='')
    else:
        answer *= num
        print(f' x {num}', end='')
'''
    else :
        answer += num
        print(f' + {num}', end='')
'''
print(f' = {answer}')
