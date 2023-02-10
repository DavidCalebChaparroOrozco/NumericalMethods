def sign_of_a(a):
    if a < 0.0:
        sign = 'negative'
    elif a > 0.0:
        sign = 'positive'
    else:
        sign = 'zero'
    return sign

a = int(input('Enter a number: '))
print('a is: '+ sign_of_a(a))

print("-".center(50,'-'))

