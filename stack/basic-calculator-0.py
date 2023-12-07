# string contains only + , - and digits
def calculate(s):
    result = 0
    num = 0
    sign = 1
    for ch in s:
        if ch.isdigit():
            num = num*10 + int(ch)
        else:
            result += num*sign
            sign = 1 if ch == '+' else -1
            num = 0
    return result+ sign*num

result = calculate("+123432+352-54235-1+0-12")    
print(result)