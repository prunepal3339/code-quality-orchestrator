def square_Sum(n):
تنظیم متغیر مجموع به صفر
    total = 0
    # حلقه تکرار برای پیدا کردن اعداد فردی و جمع دوباره آن‌ها
    for i in range(1, 2*n, 2):
        total += i**2
    return total
