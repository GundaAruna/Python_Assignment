b1=int(input("Enter the no.of books of type1: "))
b2=int(input("Enter the no.of books of type2: "))
b3=int(input("Enter the no.of books of type3: "))
cb1=499.00
cb2=855.00
cb3=645.00
dcharges=250.00
Amount=(b1*cb1)+(b2*cb2)+(b3*cb3)+dcharges
gst=0.12*Amount
Total_Invoice_Amount=Amount+gst
print("Total invoice Amount is: ",Total_Invoice_Amount)
