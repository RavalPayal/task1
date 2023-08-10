 # create a product and price for 3 items
p1_name,p1_price = "apple",10.90
p2_name,p2_price = "banana" , 30
p3_name,p3_price = "mango" , 50

 # create a company name and information
company_name = "Alepa"
company_address = "salomonkatu 19"
company_city = "helsinki"
 # declare ending message
message = "Thank you for shopping with us today!"
 # create a top border
print("*"*50)
 # print company information first using format
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))

print("\t\t{}".format(company_city))
 # print a line between sections
print("*"*50)

 # print out header for section of items
print("\t product name \t product price")

 # creat a print statement for each product
print("\t{}\t\tε{}".format(p1_name.title(),p1_price))
print("\t{}\t\tε{}".format(p2_name.title(),p2_price))
print("\t{}\t\tε{}".format(p3_name.title(),p3_price))

#print a line between section
print("="*50)

# print out header for section for  total
print("\t\t\t  total")

# calculate total price and print it
total=p1_price+p2_price+p3_price
print("\t\t\tε{}".format(total))

# print a line between sections
print("="*50)

# output thank you message
print("\n\t{}\n".format(message))

# creat a bottom border
print("*"*50)


