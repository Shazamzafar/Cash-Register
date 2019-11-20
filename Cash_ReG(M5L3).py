# Name:      Shazam Zafar
# Class:     Python M5L4
# Date:      November 20, 2018

# Ratailitem class


class Ratailitem:

    # Function for self description unit in inventory and price
    def __init__(self, des, UI, price):
        self.__description = des
        self.__units_inventory = UI
        self.__price = price

        # function declaring the description
    def set_desc(self, desc):
        self.__description = des

        # Function declaring the Unit in Inventory
    def set_UI(self, UI):
        self.__units_inventory = UI

        # Function declaring the price
    def set_price(self, price):
        self.__price = price

        # Function for getting the description
    def get_desc(self):
        return self.__description

        # Function for getting Units in Inventory
    def get_UI(self):
        return self.__units_inventory

        # Function for getting the price in float
    def get_price(self):
        return float(self.__price)

# Cash register class


class CashRegister:

    # function for self list
    def __init__(self):
        self.__list_item = []

        # Function for appending the purchase items with list
    def purchase_item(self, r):
        self.__list_item.append(r)

        # Function for total price
    def get_total(self):
        price = 0.0
        for item in self.__list_item:
            price += item.get_price()
        return price

        # Function For showing user the description
    def show_items(self):
        for item in self.__list_item:
            print(item.get_desc())
        # Clearing the list

    def clear(self):
        for item in self.__list_item:
            self.__list_item.remove(item)

# Main function


def main():
        # items name units in inventory and prices
    r1 = Ratailitem("Pants", "12", "59")
    r2 = Ratailitem("Shirts", "40", "34.95")
    r3 = Ratailitem("Dress", "20", "24.95")
    r4 = Ratailitem("Socks", "10", "99.99")
    r5 = Ratailitem("Sweater", "20", "39.99")

# Printting the data
    crl = CashRegister()
    print("Menu")
    print("-------------------------")
    print(r1.get_desc())
    print(r2.get_desc())
    print(r3.get_desc())
    print(r4.get_desc())
    print(r5.get_desc())
    print("")
    ch = "y"

    # While loop for asking user over and over to purchase items
    while ch.upper() == "Y":
        item = input("Enter the  item you would like to purchase:")

        # If statement giving user different choices
        if item.upper() == r1.get_desc().upper():
            crl.purchase_item(r1)

        elif item.upper() == r2.get_desc().upper():
            crl.purchase_item(r2)

        elif item.upper() == r3.get_desc().upper():
            crl.purchase_item(r3)

        elif item.upper() == r4.get_desc().upper():
            crl.purchase_item(r4)

        elif item.upper() == r5.get_desc().upper():
            crl.purchase_item(r5)

            # If item user enter and its not available if goes to else
        else:
            print("Items not available")

            # Asking user if he wants keep going
        ch = input("Do you want to select anther items: Enter \"y\" for yes And any Key to exit:")
#printing the final bill for user
    print("The items in the cash register are:")
    print("")
    print("Description")
    print(crl.show_items())
    print("")
    print("Price")
    print(crl.get_total())


#Calling the main function
main()
