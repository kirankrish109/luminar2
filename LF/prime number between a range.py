low = int(input("Enter the lower range"))
up = int(input("Enter the upper number"))


while(low<up):

    if(low>1):
        while(low<up):
            if(up%low == 0):
                break
            else:

                print(low)
                break


            low=low+1


