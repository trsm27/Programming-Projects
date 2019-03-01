# bus ticket calculator

in this demonstration we can see of how to format certain inputs to be certain data types like interger, string and float

```
num_tickets = int(input("enter number of bus tickets required "))

```

in this line of code python stores the number of bus tickets required as an integer form due to the ```int()``` and stores is in a variable called ```num_tickets```

```
price = float(input("Enter price of bus tickets "))
```

in this line of code python stores the number of bus tickets required as a float form due to the ```float()``` and stores is in a variable called ```price```

```
total = num_tickets * price
```
this line of code stores the overall price of the ride by multiplying the number of tickets and the price per tickets in ```num_tickets * price``` and then storing the results in a variable called ``` total```


```
print("the total price is: $%.2f" % total)
```

this line outputs the total amount of the ride in 2 deciaml places

```
print("The change from £"+ str('%.2f' % offer)+ ' is £'+str('%.2f' % change))
```

this outputs the change calculated by ```change = offer - total``` in 2 decimal places in the format ```The change from £??.?? is £??.??```
