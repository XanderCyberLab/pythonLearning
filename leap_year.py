year = int(input("Enter the Year to determine if it is a Leap Year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a Leap Year")
# else:
#     print(f"{year} is not a Leap Year")
    
if year % 4 == 0 & year % 100 == 0 & year % 400 == 0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")