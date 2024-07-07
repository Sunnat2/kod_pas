import random
password = input("Ведите пороль для проверки:")
num = ['1', '56', '89', '7', '@', '$', '!', 'пропись', 'имя', 'фомилия'];
if password.isdigit():
    for a in range(8):
        rnum = random.choice(num)
    if password == rnum:
        print("пароль веден правельно", password)
        
    else:
        print(a, rnum, "False")

else:
    print("пароль веден не вурно")