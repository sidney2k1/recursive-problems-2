totalamount=int(input("Enter the amount of money:"))
listofnotes=[1000,500,100,50,20,10,5]
for i in listofnotes:
    numberofnotes=totalamount//i
    totalamount%=i
    if numberofnotes!=0:
        print(f"The number of notes of {i} is {numberofnotes}")