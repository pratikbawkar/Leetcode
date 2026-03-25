# 2026 NQT test problem
"""1st question is Write a program to calculate the final payable amount after applying a discount based on total purchase amount.
 Amount < 1000  - 5% off,  1000-5000 10%off , Amount > 5000 discount 15% , negative / <0 input  - error. 
example amount - 1200 purchase  - pay 1080"""
amount = int(input())

if amount < 0:
    print("Error")
elif amount < 1000:
    print(amount * 0.95)
elif 1000 <= amount <= 5000:
    print(amount * 0.90)
else:
    print(amount * 0.85)
