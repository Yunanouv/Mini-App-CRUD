import emoji
from tabulate import tabulate
import datetime

# Greeting
print(emoji.emojize("\n         Welcome To the Cake Shop :smiling_face_with_smiling_eyes: \n") )

# Record current date and time
current_time = datetime.datetime.now()
print("Date and Time: ", current_time.strftime("%Y-%m-%d %H:%M:%S"))

# Data
data = {'Item Name': ['Apple Pie', 'Strawberry Shortcake', 'Fruit Tartlets', 'Blueberry Cheesecake', 'Brownies'],
        'Stock': [8, 15, 20, 5, 10],
        'Price (Rp)': [90000, 35000, 10000, 180000, 60000]}

def display_cake(data):
    print("======================================================")
    print("          \N{BIRTHDAY CAKE} List of Cakes \N{BIRTHDAY CAKE}")
    print(tabulate(data, headers="keys",tablefmt="fancy_grid", showindex="always"))
    print("======================================================")

def addnew_cake():
    print("\n \N{SHORTCAKE} ADD NEW CAKE \N{SHORTCAKE} \n")
    while True:
        newcake_input = input("Input the Item Name = ").strip().title()
        if newcake_input.replace(" ", "").isalpha():  # Check if the input contains only alphabetic characters and spaces
            break
        else:
            print("Invalid input! Please enter only alphabetic characters!\n")

    if newcake_input in data['Item Name']:
        print("The {} already exists.".format(newcake_input))
        while True:
            add_stock = input("Do you want to add stock for this item? (Y/N) : ").strip().upper()
            if add_stock == 'Y':
                index = data['Item Name'].index(newcake_input)
                while True:
                    try:
                        cakestock_input = int(input("Input additional stock for '{}' : ".format(newcake_input)))
                        if cakestock_input > 0:
                            data['Stock'][index] += cakestock_input
                            print("Stock has been UPDATED succesfully! \N{WHITE HEAVY CHECK MARK} \n")
                            return
                        else:
                            print("Invalid input! Quantity must be greater than 0\n")
                    except ValueError:
                        print("Invalid input! Please enter a valid integer\n")
            elif add_stock == 'N':
                print("No changes have been made.")
                break
            else:
                print("Please input only Y or N!")
    else: # If the item is new
        while True:
            try:
                cakestock_input = int(input("Input the cake stock = "))
                if cakestock_input > 0:
                    break
                else:
                    print("Invalid input! Quantity must be greater than 0\n")
            except ValueError:
                print("Invalid input! Please enter a valid integer\n")

        while True:
            try:
                cakeprice_input = int(input("Input the price = Rp. "))
                if cakeprice_input > 0:
                    break
                else:
                    print("Invalid input! Price must be greater than 0\n")
            except ValueError:
                print("Invalid input! Please enter a valid integer\n")

            # Add new item w user input
        data['Item Name'].append(newcake_input)
        data['Stock'].append(cakestock_input)
        data['Price (Rp)'].append(cakeprice_input)
        print("\nNew cake has been ADDED successfully! \N{WHITE HEAVY CHECK MARK} \n")

def edit_cake():
    print("\n \N{DOUGHNUT} EDIT CAKE DETAILS\n")

    while True:
        display_cake(data)
        try:
            edit_cake_index = int(input("Enter the index of the cake you want to edit: "))
            if 0 <= edit_cake_index < len(data['Item Name']):
                edit_cake_name = data['Item Name'][edit_cake_index]  # Retrieve the item name
                break
            else:
                print("Invalid index! Please enter a valid index.\n")
        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")

    # Check if the cake exists in the list
    found = False
    for index, name in enumerate(data['Item Name']):
        if name == edit_cake_name:
            found = True
            print("\nThe detail of {} :".format(edit_cake_name))
            print("1. Item : {}".format(name))
            print("2. Stock : {}".format(data['Stock'][index]))
            print("3. Price : {}".format(data['Price (Rp)'][index]))
            print("4. Cancel")
                
            while True:
                edit_choice = input("\nEnter the number you want to edit: ").strip()
                if edit_choice == '1':
                    while True:
                        edit_name = input("\nEnter the new name: ").title()
                        if edit_name == data['Item Name'][index]:
                            print("\nThe new name is the same as the current name. No changes made.")
                            break
                        elif any(edit_name == name for name in data['Item Name'] if name != data['Item Name'][index]):
                            print("\nThe new name matches another existing name. Please choose a different name.")
                        elif all(char.isalpha() or char.isspace() for char in edit_name):
                            data['Item Name'][index] = edit_name
                            print("\nItem Name UPDATED successfully! \N{WHITE HEAVY CHECK MARK} \n")
                            display_cake(data)
                            return
                        else:
                            print("\nInvalid input! Please enter alphabetic characters only.")

                elif edit_choice == '2':
                    while True:
                        try:
                            edit_stock = int(input("\nEnter the new stock: "))
                            if edit_stock == data['Stock'][index]:  # Check if the edited stock is the same as before
                                print("\nThe new stock quantity is the same as before. No changes made.")
                                return
                            elif edit_stock >= 0:
                                data['Stock'][index] = edit_stock
                                print("\nStock quantity UPDATED successfully! \N{WHITE HEAVY CHECK MARK} \n")
                                display_cake(data)
                                break
                            else:
                                print("\nInvalid input! Please enter a non-negative integer.")
                        except ValueError:
                            print("\nInvalid input! Please enter a valid integer.")
                elif edit_choice == '3':
                    while True:
                        try:
                            edit_price = int(input("\nEnter the new price: Rp. "))
                            if edit_price == data['Price (Rp)'][index]:  # Check if the edited price is the same as before
                                print("\nThe new price is the same as before. No changes made.")
                                return
                            elif edit_price > 0:
                                data['Price (Rp)'][index] = edit_price
                                print("\nPrice UPDATED successfully! \N{WHITE HEAVY CHECK MARK} \n")
                                display_cake(data)
                                break
                            else:
                                print("\nInvalid input! Please enter price more than 0.")
                        except ValueError:
                            print("\nInvalid input! Please enter a valid integer.")
                    break
                elif edit_choice == '4':
                    print("\nNo changes have been made.")
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
    if not found:
        print("{} is not found in the list.".format(edit_cake_name))

def delete_cake():
    display_cake(data)
    while True:
        try:
            del_index = int(input("Please enter the index of the cake you want to remove : "))
            if del_index <0 or del_index >= len(data["Item Name"]):
                print("Invalid Index! Please try again! \n")
            else:
                break
        except ValueError:
            print("Invalid Input! Please enter an integer!\n")

    while True: 
        confirmation = input(f" \N{WARNING SIGN}\N{VARIATION SELECTOR-16}  Are you sure you want to delete {data['Item Name'][del_index]} (Y/N)?: ").strip().upper()
        if confirmation == 'Y':
            for i in data.values():
                i.pop(del_index)
            print("\n The cake has been REMOVED successfully! \N{WASTEBASKET}\N{VARIATION SELECTOR-16} \n")
            display_cake(data)
            break
        elif confirmation == 'N':
            print("Deletion aborted.\n")
            display_cake(data)
            break
        else:
            print("Please input only Y or N!")

def trx_menu():
    while True:
        print('''\n
        \N{MONEY WITH WINGS} TRANSACTION MENU\n
        1. Add Item to the Cart
        2. View Cart
        3. Payment      
        4. Exit\n
              ''')

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transaction()
        elif choice == "3":
            payment()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

trx = []
total_amount = 0
change = 0

def view_transaction():
    if trx:
        print("\nShopping Cart \N{PANCAKES}")
        rows = [[item['Item Name'], item['Qty'], item['Price (Rp)'], item['Subtotal (Rp)']] for item in trx]
        print(tabulate(rows, headers="keys", tablefmt="grid", showindex="always"))
    else:
        print("The cart is empty.")

def add_transaction():
    shopping_run = True
    original_stock = data["Stock"][:]
    
    while shopping_run == True:
        display_cake(data)

        while True: # Checking index
            try:
                cart_index = int(input("Enter the index number of cake = "))
                if cart_index < 0 or cart_index >= len(data['Item Name']):
                    print("Invalid Index! Please try again \n")
                elif data["Stock"][cart_index] == 0:
                    print("Sorry, this cake is out of stock. Please select another one.\n")
                else:
                    break
            except ValueError:
                print("Invalid Index! Please try again \n")

        while True:
            try:
                inputcart_qty = int(input("Enter the quantity = "))
                if inputcart_qty > 0:
                    if inputcart_qty <= data["Stock"][cart_index]:
                        subtotal = data["Price (Rp)"][cart_index] * inputcart_qty
                        data["Stock"][cart_index] -= inputcart_qty

                        found = False # Check if the cake already exist in shopping cart
                        for item in trx:
                            if item['Item Name'] == data['Item Name'][cart_index]:
                                item['Qty'] += inputcart_qty
                                item['Subtotal (Rp)'] += subtotal
                                found = True
                                break
                        if not found:
                            trx.append({'Item Name':data['Item Name'][cart_index],
                                        'Qty' : inputcart_qty, 
                                        'Price (Rp)':data['Price (Rp)'][cart_index],
                                        'Subtotal (Rp)' : subtotal})
                        print("Item added to the cart successfully \N{WHITE HEAVY CHECK MARK} \n")
                        break
                    else:
                        print("We dont have enough stock. The remaining stock is {}".format(data["Stock"][cart_index]))
                else:
                    print("Invalid Input! Quantity must be greater than 0\n")
            except ValueError:
                print("Invalid input! Please enter a valid quantity\n")
        
        while True:
            next_item = input("Continue shopping (Y/N)? : ").strip().upper()
            if next_item == "N":
                try :
                    while True:
                        try:
                            stop_shopping = input('''
                                \N{SHOPPING TROLLEY} What would you like to do ? 

                                1. Cancel the transaction 
                                2. Remove Item from the Cart
                                3. Proceed the Payment 
                                4. Back to Transaction Menu

                                Your choice = ''').strip()
                            if stop_shopping == "1":
                                shopping_run = False
                                trx.clear()
                                print("Transaction CANCELED. The cart is empty.")
                                data["Stock"] = original_stock
                                return
                            elif stop_shopping == "2":
                                remove_transaction()
                                shopping_run = False
                                return
                            elif stop_shopping == "3":
                                payment()
                                return
                            elif stop_shopping == "4":
                                print("\nExiting Program \N{WAVING HAND SIGN} \n")
                                return
                            else:
                                print("Invalid choice. Please choose the correct menu!")
                        except ValueError:
                            print("Invalid input! Please try again!\n")
                except ValueError:
                    print("Invalid input! Please try again!\n")
            elif next_item == "Y":
                break
            else:
                print("Please input only Y or N!\n")

def remove_transaction():
    if not trx:
        print("The cart is empty.")
        return

    view_transaction()
    while True:
        try:
            remove_item_index = int(input("Enter the index of the item you want to remove from the cart: "))
            if remove_item_index >= 0 and remove_item_index < len(trx):
                removed_item = trx.pop(remove_item_index)  
                removed_item_name = removed_item['Item Name'] 
                print(f"Removing {removed_item_name} from the cart...\n")

                for index, item in enumerate(data['Item Name']):
                    if item == removed_item_name:
                        data['Stock'][index] += removed_item['Qty']
                        print(f"Stock of {removed_item_name} reverted to {data['Stock'][index]}\n")
                print("\nItem REMOVED from the cart and stock REVERTED successfully!")
                break
            else:
                print("Invalid item index.")
        except ValueError:
            print("Invalid input! Please enter a valid integer!")

def payment():
    if trx: 
        while True:
            view_transaction()
            next_step = input("\nProceed the payment (Y/N) ? : ").strip().upper()
            total_cart_amount = sum(item['Subtotal (Rp)'] for item in trx)

            if next_step == "Y":
                print(f"Total Amount: Rp. {total_cart_amount}")
                while True:
                    try:
                        money = int(input("\nCash = Rp. "))
                        if money < 0:
                            print("Invalid input! Please enter a positive integer.")
                        elif money == 0:
                            print("Please input money more than 0.")
                        else:
                            if money >= total_cart_amount:
                                change = money - total_cart_amount
                                print(f"Change: Rp. {change}\n")
                                print_receipt(total_cart_amount, change)
                                trx.clear()
                                return
                            else:
                                print(f"You need to pay Rp. {total_cart_amount-money} more")
                    except ValueError:
                        print("Invalid input! Please enter a valid integer!\n")
            elif next_step == "N":
                print("Payment CANCELED. The cart is empty.")
                for item in trx:
                    for index, fruit in enumerate(data['Item Name']):
                        if fruit == item["Item Name"]:
                            data["Stock"][index] += item["Qty"]
                trx.clear()
                break
            else:
                print("Please input only Y/N!")
    else:
        print("The cart is empty.")

def print_receipt(total_amount, change):
    current_time = datetime.datetime.now()
    receipt_data = [["Item Name", "Qty", "Subtotal (Rp)"]]
    for item in trx:
        receipt_data.append([item['Item Name'], item['Qty'], item['Subtotal (Rp)']])
    
    print("\n================== RECEIPT ==================")
    print("Date and Time:", current_time.strftime("%Y-%m-%d %H:%M:%S\n"))
    print(tabulate(receipt_data, headers="firstrow", tablefmt="simple"))
    print(f"\nTotal Amount : Rp. {total_amount}")
    print(f"Change       : Rp. {change}\n")
    print("                     THANK YOU!")
    print("==============================================")

def main(): 
    while True:
        print(""" 
        \N{SPARKLES} MAIN MENU \N{SPARKLES}
            
        1. Display List of Cake
        2. Add New Cake
        3. Edit Cake      
        4. Delete Cake 
        5. Transaction
        6. Exit Program
        """)

        options = input("Input the Number of Menu Options : ").strip()
        if options == "1": 
            display_cake(data)
        elif options == "2":
            addnew_cake()
            display_cake(data)
        elif options == "3":
            edit_cake()
        elif options == "4" :
            delete_cake()
        elif options == "5":
            trx_menu()
        elif options == "6":
            print("\nExiting Program \N{WAVING HAND SIGN} \n")
            break
        else:
            print("Invalid choice. Please choose the correct menu!")

if __name__ == "__main__":
    main()
