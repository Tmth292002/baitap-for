# a = float(input("Enter any number: "))
# b = float(input("Enter any number: ")) 
# if a < b or a==b:
#     print("a is True  ")
# elif a!=b:
#     if a>b: 
#         print("a>b")
#     elif a<b:
#         print("a<b")
# elif a>b and a==b:
#     print("a is  True")  
# else:
#     print("nothing")


# age = 16

# if age < 10:
# 	print("con nit")
# elif age < 18:
# 	print("thanh thieu nien")
# 	if age >= 15 and age <= 17:
# 		print("tre day thi")
# else:
# 	print("nguoi lon")


def chuoiif():
    i = int(input("Enter any number: "))
    if (i == 10): 
        # print(" i == 10 ")
        if i<15:
            print("i < 15")
        if 10 < i < 15:
            print("i la 1 so nao do 10 < i < 15") 
        else:
            print("not thing")
if __name__ == "__main__":
    
    chuoiif()