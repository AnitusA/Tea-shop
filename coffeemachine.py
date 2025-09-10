import time


normal = 10
cold = 20
chocolate = 15

print("Your coffee machine is on")

def coffee():
    global normal, cold, chocolate
    choice = int(input("Please select an option:\n 1. Normal\n 2. Cold\n 3. Chocolate\n"))

    match choice:
        case 1:
            if(normal >= 1):
                print("Ingredients for your normal coffee is available")
                normal -= 1
            else:
                print("Ingredients for your normal coffee is not available")
                print("Please select another option")
        case 2:
            if(cold >= 1):
                print("Ingredients for your cold coffee is available")
                cold -= 1
            else:
                print("Ingredients for your cold coffee is not available")
                print("Please select another option")
        case 3:
            if(chocolate >= 1):
                print("Ingredients for your chocolate coffee is available")
                chocolate -= 1
            else:
                print("Ingredients for your chocolate coffee is not available")
                print("Please select another option")
        case _:
            print("Invalid option selected")

    print("Your coffee is ready in 5 minutes")
    time.sleep(5)
    print("Your coffee is ready")
    print("Thank you for using my coffee machine")
    print(f"remaining normal: {normal}\n remaining cold: {cold}\n remaining chocolate: {chocolate}")
    if(normal == 0 and cold == 0 and chocolate == 0):
        print("All ingredients are finished")
        print("Please refill the ingredients")
    else:
        coffee()

if __name__ == "__main__":
    coffee()
