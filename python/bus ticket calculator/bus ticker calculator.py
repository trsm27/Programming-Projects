num_tickets = int(input("enter number of bus tickets required "))
price = float(input("Enter price of bus tickets "))
total = num_tickets * price
print("the total price is: $%.2f" % total)
offer = float(input("Enter the amount of money offerred "))
change = offer - total
print("The change from £"+ str('%.2f' % offer)+ ' is £'+str('%.2f' % change))
