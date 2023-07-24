
"""
TODO
یک تابع بنویسید که لیستی از اعداد را به عنوان پارامتر بگیرد
و 
مجموع اعداد زوج موجود در آن را محاسبه کند و برگرداند
numbers = [102,109,2,55,67,88]
"""

# def my_func_1(numbers_list):
#     total = 0
#     for number in numbers_list:
#         if number % 2 == 0:
#             total += number

#     return total

# numbers = [102,109,2,55,67,88]
# print(my_func_1(numbers))


"""
یک تابع بنویسید که لیستی از اعداد را از ورودی دریافت نماید و 
در صورت صعودی بودن لیست 
True 
و در صورت نزولی بودن لیست
False
را برگرداند

صعودی بودن یعنی هر عدد موجود در لیست از عدد قبلی بزرگتر باشد
مثال
[1,2,3,4,8]   نمونه از لیست صعودی


نزولی:
هر عدد از بعدی کوچکتر باشد

[5,3,1,0]  نمونه یک لیست نزولی


در تابع از 
for   و   if
استفاده کنید
"""

# numbers = [1,2,3,4,8]
numbers = [3,2,1]
def my_func_2(n):
    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            if n[i] > n[j]:
                return False
            
    return True

print(my_func_2(numbers))