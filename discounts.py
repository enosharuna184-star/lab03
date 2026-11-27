amount = int(input("Enter the purchased amount:"))

if amount < 2000:
    discount = amount * 5 / 100
elif amount <= 5000:
    discount = amount * 10 / 100
else:
    discount = amount * 15 / 100

discount_amount = amount - discount

gst = discount_amount * 5 /100

final_amount = discount_amount + gst  

print("----Discount calculate----")
print("Amount", amount)
print("Discount", discount)
print("Amount after discount", discount_amount)
print("gst_amount", gst)
print("Total_bill", final_amount)

