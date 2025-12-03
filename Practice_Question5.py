usage = int(input("Enter the usage amount in units: "))
bill_amount = 0

if usage < 100:
    if usage >= 100 and usage <= 300:
        temp = usage - 100
        bill_amount += temp * 8
        bill_amount += 500
    else:
        temp = usage - 300
        bill_amount += temp * 10
        bill_amount += 500
        bill_amount += 200 * 8
else:
    bill_amount += usage * 5