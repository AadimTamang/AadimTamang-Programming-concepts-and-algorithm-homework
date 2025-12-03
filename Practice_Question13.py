total_amount = float(input("Enter total amount: "))
is_member = input("Is the customer a member? (True/False): ")

is_member = True if is_member == "True" else False

if total_amount > 1000 and is_member:
    discount = 0.20 * total_amount
elif total_amount > 1000 and not is_member:
    discount = 0.10 * total_amount
else:
    discount = 0

final_amount = total_amount - discount
print("Final amount to pay: Rs", final_amount)
