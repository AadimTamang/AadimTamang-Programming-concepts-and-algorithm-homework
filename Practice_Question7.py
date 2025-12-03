class_a = int(input("Enter the number of student A: "))
class_b = int(input("Enter the number of student B: "))
class_c = int(input("Enter the number of student C: "))
tables = 0

if class_a % 2 == 0:
    tables += class_a // 2
else:
    tables += (class_a // 2) + 1
if class_b % 2 == 0:
    tables += class_b // 2
else:
    tables += (class_b // 2) + 1
if class_c % 2 == 0:     
    tables += class_c // 2
else:
    tables += (class_c // 2) + 1    

print("The total number of tables required is:", tables)