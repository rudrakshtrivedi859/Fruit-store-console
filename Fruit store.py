d={}

while True:
    menu = """
        WELCOME TO FRUIT MARKET

        1) Manager
        2) Customer
        """
    print(menu)
    Role=int(input("Select your Role: "))

    if Role==1:
        while True:
            print("""

            Fruit Market Manager

            1) Add Fruit Stock
            2) View Fruit Stock
            3) Update Fruit stock
            """)
            choice=int(input("Enter your choice: "))

            if choice==1:
                print("\n ADD FRUIT STOCK")
                n=int(input("How many fruits you want to buy: "))
                total=""
                for i in range(1,n+1):
                  
                    fruit = input("Enter Fruit Name: ")
                    qty = input("Enter qty (in kg): ")
                    price = input("Enter price (for kg): ")

                    d[fruit]={
                    "qty" : qty,
                    "price" : price
                }
            cont = input("\nDo you want to perform more operations : press y for yes and n for no : ")

            if cont.lower() != "y":
                break
                

            elif choice==2:
                print("ALL FRUIT STOCKS")
                if len(d)==0:
                    print("No stock added yet!")
                else:
                    print(d)

            elif choice==3:
                fruit=input("Enter fruit name to update: ")
                if fruit in d:
                 new_qty = input("Enter qty (in kg): ")
                 new_price = input("Enter price (for kg): ")

                 d[fruit]["qty"]=new_qty
                 d[fruit]["price"]=new_price
                 print("Stock Updated Successfully!!")
                else:
                    print("Fruit not Found in stock!!")

                

    elif Role==2:
        print("Customer Module coming soon!!")

    else:
        print("Invalid Role Selected")
        break






            





        

      
          