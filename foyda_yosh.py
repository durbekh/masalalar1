j = input("Jinsingizni kiriting (erkak yoki ayol): ").lower()
y = int(input("yoshingizni kiriting : "))
if 0 <= y <= 120 :
    if j == "erkak" and y >= 60:
        n_y = y - 60
        if n_y == 0 :
            print(f"Bobo siz nafaqa chiqgansiz . \nNafaqaga shu yili chiqgansiz")
        else:
            print(f"Bobo siz nafaqa yoshidasiz . \nNafaqaga cgiqganingizga {n_y} yil bo'ldi")
    elif j == "erkak" and y < 60 :
        n_ye = 60 - y
        print(f"Hurmatli foydalanuvchi siz hali nafaqaga chiqmagansiz . \nNafaqaga chiqishingizga {n_ye} yil bor .")
    elif j == "ayol" and y < 60 :
        n_yea = y - 60
        print(f"Hurmatli foydalanuvchi siz hali nafaqaga chiqmagansiz . \nNafaqaga chiqishingizga {n_yea} yil bor .")
    elif j == "ayol" and y >= 60 :
        n_yy = y - 60
        if n_yy == 0 :
            print(f"Buvi siz nafaqa yoshidasiz . \nNafaqaga yaqinda chiqdingiz")
        else:
            print(f"Buvi siz nafaqa yoshidasiz .\nNafaqaga cgiqganingizga {n_yy} yil bo'ldi")
    else:
        print("Hurmatli foydalanuvchi siz jinsingizni to'g'ri kiritishingiz kerak")
else:
    print("Yoshingizni to'g'ri kiriting ! ")




















