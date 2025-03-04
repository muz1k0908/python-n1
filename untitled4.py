# xaqiqiy
# son = float(input("Juft son kiriting: ")
# if son % 2 == 0:
#    print("Bu son juft emas.")
# else:
#    print("Rahmat!"))

# togrisi
#son = float(input("Juft son kiriting: "))
#if son % 2 == 1:
 #   print("Bu son juft.")
#else:
  #  print("Rahmat!")

# xaqiqiy
# yosh = (input("Yoshingiz nechida?"))
# if yosh <= 4 or yosh >= 60:
#    narh = 0
# elif yosh < 18:
#    narh = 10000
# else:
#    narh = 20000
#    print(f"Chipta {narh} so'm")

#togrisi
#yosh = int(input("Yoshingiz nechida?"))
#if yosh <= 4 or yosh >= 60:
#    narh = 0
#elif yosh < 18:
 #   narh = 10000
#else:
 #   narh = 20000
#print(f"Chipta {narh} so'm")

# Original:
# x = float(input("Birinchi sonni kiriting: ")
# y = float(input("Ikkinchi sonni kiriting: ")
# if x == y:
#    print(f"{x}={y}")
# elif x < y:
#    print(f'{x}<{y}')
# else:
#    print(f"{x}>{y}")

# Correct:
#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x == y:
#    print(f"{x} = {y}")
#elif x < y:
#    print(f'{x} < {y}')
#else:
#    print(f"{x} > {y}")

# Original:
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               #'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#for n in range(5):
 ##   savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# Correct:
#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 
              #'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#p#rint("Savatda mavjud mahsulotlar:", savat)


# Original:
# users = ['alisher1983','aziza','yasina' 'umar']
# login = input("Yangi login tanlang:' )

# Correct:
#users = ['alisher1983', 'aziza', 'yasina', 'umar']  # Corrected the list
#login = input("Yangi login tanlang: ")

#if login in users:
   # print('Login band, yangi login tanlang!')
#else:
   # print("Xush kelibsiz!")





users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:" )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")