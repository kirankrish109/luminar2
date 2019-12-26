ClothType = int(input("Enter the cloth type \n 1.silk \n 2.linen \n 3.cotton \n"))
ClothPrice = float(input("Enter the cloth price:"))

if(ClothType == 1):
    if(ClothPrice > 5000):
        price = ClothPrice-ClothPrice*0/100
        print("The price after 0% discount is ",price)
    elif(ClothPrice > 4000 and ClothPrice < 5000):
        price = ClothPrice - ClothPrice * 10 / 100
        print("The price after 10% discount is ",price)
    elif (ClothPrice > 3000 and ClothPrice < 4000):
        price = ClothPrice - ClothPrice * 8 / 100
        print("The price after 8% discount is ", price)
    elif (ClothPrice > 2000 and ClothPrice < 3000):
        price = ClothPrice - ClothPrice * 7 / 100
        print("The price after 7% discount is ", price)
    elif (ClothPrice < 2000):
        price = ClothPrice - ClothPrice * 5 / 100
        print("The price after 7% discount is ", price)
else:
      print("invalid entry")


if(ClothType == 2):
    if(ClothPrice > 5000):
        price = ClothPrice-ClothPrice*0/100
        print("The price after 0% discount is ",price)
    elif(ClothPrice > 4000 and ClothPrice < 5000):
        price = ClothPrice - ClothPrice * 10 / 100
        print("The price after 10% discount is ",price)
    elif (ClothPrice > 3000 and ClothPrice < 4000):
        price = ClothPrice - ClothPrice * 8 / 100
        print("The price after 8% discount is ", price)
    elif (ClothPrice > 2000 and ClothPrice < 3000):
        price = ClothPrice - ClothPrice * 7 / 100
        print("The price after 7% discount is ", price)
    elif (ClothPrice < 2000):
        price = ClothPrice - ClothPrice * 5 / 100
        print("The price after 7% discount is ", price)
else:
      print("invalid entry")

if(ClothType == 3):
    if(ClothPrice > 5000):
        price = ClothPrice-ClothPrice*0/100
        print("The price after 0% discount is ",price)
    elif(ClothPrice > 4000 and ClothPrice < 5000):
        price = ClothPrice - ClothPrice * 10 / 100
        print("The price after 10% discount is ",price)
    elif (ClothPrice > 3000 and ClothPrice < 4000):
        price = ClothPrice - ClothPrice * 8 / 100
        print("The price after 8% discount is ", price)
    elif (ClothPrice > 2000 and ClothPrice < 3000):
        price = ClothPrice - ClothPrice * 7 / 100
        print("The price after 7% discount is ", price)
    elif (ClothPrice < 2000):
        price = ClothPrice - ClothPrice * 5 / 100
        print("The price after 7% discount is ", price)
else:
      print("invalid entry")
