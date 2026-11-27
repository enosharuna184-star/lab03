amount = int(input("Enter the purchased amount:"))

if amount < 2000:
    discount = amount * 5 / 100
elif amount <= 5000:
    discount = amount * 10 / 100
else:
    discount = amount * 15 / 100

discount_amount = amount - discount

print("----Discount calculate----")
print("Amount", amount)
print("Discount", discount)
print("Amount after discount", discount_amount)

