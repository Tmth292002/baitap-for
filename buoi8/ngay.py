# def day(i):

#     switcher = {
#         0: 'Sunday',
#         1: 'Monday',
#         2: 'Tuesday',
#         3: 'Wednesday',
#         4: 'Thursday',
#         5: 'Friday',
#         6: 'Saturday'
#     }
#     return switcher.get(i, "Invalid day of week")


# def week(i):
#     switcher = {
#         0: 'Sunday',
#         1: 'Monday',
#         2: 'Tuesday',
#         3: 'Wednesday',
#         4: 'Thursday',
#         5: 'Friday',
#         6: 'Saturday'
#     }
#     return switcher.get(i, "Invalid day of week")


# if __name__ == "__main__":
#     try:
#         i = int(input("Nhap ngay: "))
#         print(week(i))

#     except:
#         print("Pleased, enter number 0-6 again. ")


def season(i):
    switcher = {
        1: "Summer",
        2: "Autunm",
        3: "Winter",
        4: "Spring"
    }
    return switcher.get(i, "Invalid day of week")


if __name__ == "__main__":
    a = input()
    print(season(a))

# import math
# n = int(input("Nhập số cần kiểm tra"))
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
#         print(i)
# print(count)
# if count == 2:
#     print("Số nguyên tố")
# else:
#     print("k phải số nguyên tố")
