book_dictionary = {
"Zindagi gulzar hai": 500,
"Mushaf": 450,
"Namal": 550,
"Umera ahmed collection": 800,
"La hasil": 400,
"Devta": 700,
"Mann mayal": 300,
"Alif": 550,
"Raja gidh": 500,
"Bano": 450,
"Mere humdum mere dost": 350,
"Maat": 480,
"Mera saeein": 700,
"Dastaan": 420,
"Bazigar": 550,
"Jannat kay pattay": 600,
"Mohabbat subha ka sitara hai": 480,
"Aks": 500,
"Kuch khwab hein adhurey": 450,
"Raat ka sheher": 480,
"Bin roye ansoo": 400,
"Abdullah": 550,
"Ishq ka qaaf": 420,
"Muqaddas": 500,
"Amar bail": 480,
"Tum akhri jazeera ho": 600,
"Mera ishq hai tu": 450,
"Jheel kinara kankar": 350,
"Khuda aur mohabbat": 700,
"Jannat do qadam": 420,
"Bheegi palkon par": 500,
"Sauda": 480,
"Koi lamha khwab nahi hota": 550,
"Tum meri ho": 600,
"Iblees": 480,
"Pahari ka qaidi": 350,
"Rang rez mere": 400,
"Meri zaat zarra-e-benishan": 550,
"Hasil": 420,
"Piyas": 480,
"Mai ne khawabon ka shajar dekha hai": 600,
"Ishq ka ain": 500,
"Jannat ke pattay": 550,
"Alif laila": 480,
"Dil se nikle hain jo lafz": 350,
"Dhoop kinare": 400,
"Roshan jugnu": 600,
"Mohabbat rog hai jaana": 550,
"Aaina": 480,
"Qayamat": 500,
"Kahin deep jale kahin dil": 420,
"Gumshuda jannat": 350,
"Kuch khwab hein adhurey": 480,
"Raat ka sheher": 550,
"Dil diya dehleez": 600,
"Chand gagan aur chandni": 480,
"Dil darya samandar": 420,
"Bandhan": 450,
"Ankhoon kay saagar": 550,
"Khawab gazeeda": 600,
"Shab deeda": 480,
"Khwab sheeshe ka": 500,
"Bichray lamhe": 420,
"Khamosh wafa": 350,
"Tere liye hai mera dil": 480,
"Raat bhar ka hai mehmaan andhera": 550,
"Main hari piya": 600,
"Meray dard ko jo zuban miley": 500,
"Aurat teri yehi kahani": 450,
"Nimra ahmed collection": 550,
"Rukhsat hai ik zawal": 600,
"Bheegi palkon par": 480,
"Zard patton ka shajar": 500,
"Pehli nazar": 420,
"Pir e kamil": 1500,
"Aab e hayat": 1350,
}

from datetime import date, timedelta

order_history = {}
cart = []

def cart_adding(cart, total):
    while True:
        book_selection = input('Enter the book you want to purchase (or "Done" to finish): ').capitalize()
        if book_selection in book_dictionary:
            quantity = int(input('Enter the quantity: '))
        elif book_selection == 'Done':
            break
        else:
            print("Invalid book selection. Please choose a book from the list.")
            continue

        for _ in range(quantity):
            cart.append(book_selection)
            totaui

        print(f'{quantity} copies of {book_selection} added to your cart')

    return cart, total


def payment(total):
    while True:
        payment_method = input('Please select a payment method (Cashondelivery / Visacard / Mastercard): ').capitalize()
        delivery_charges = 140

        if payment_method == 'Cashondelivery':
            COD_charge = 30
            total += delivery_charges + COD_charge
            break
        elif payment_method == 'Visacard' or payment_method == 'Mastercard':
            total += delivery_charges
            details = input('Add Bank ISOP: ')
            break
        else:
            print('Invalid payment method. Please select from the given options')
            continue

    return total, payment_method, details if payment_method in ['Visacard', 'Mastercard'] else None


def get_details():
    name = input('Name: ')
    phone = input('Contact: ')
    address = input("Please add an address: ")

    return name, phone, address


def invoice(cart, total, payment_method, details):
    current_date = date.today()
    delivery_date = current_date + timedelta(days=7)

    print("Invoice:")
    print("----------------------------")
    print("Item\t\t\tQuantity\tPrice")
    print("----------------------------")

    for book in cart:
        price = book_dictionary[book]
        print(f"{book}\t\t\t  1\t\tPKR {price}")

    print("----------------------------")
    print("Delivery charges\t\t\tPKR 140")
    if payment_method == 'Cashondelivery':
        print('COD charge \t\t\t\tPKR 30')
    print("----------------------------")
    print(f"Total Amount:           PKR {total}")
    print(f'Consumer Name:          {details[0]}')
    if payment_method in ['Visacard', 'Mastercard']:
        print(f'Bank Details:           {details}')
    print(f'Delivery Address:       {details[2]}')
    print(f'Contact no.:            {details[1]}')
    print(f'Expected Delivery Date: {delivery_date}')


def add_to_order_history(order_id, order_details):
    order_history[order_id] = order_details


def delete_order():
    display_order_history()

    delete_option = input("What would you like to do next?\n1. Delete an Order\n2. Place Another Order\n3. Exit\nEnter 1, 2, or 3: ").lower()

    if delete_option == '1':
        order_id_to_delete = input("Enter the Order ID you want to delete (or 'cancel' to go back): ")

        if order_id_to_delete.lower() == 'cancel':
            return

        try:
            order_id_to_delete = int(order_id_to_delete)
            if order_id_to_delete in order_history:
                del order_history[order_id_to_delete]
                print(f"Order {order_id_to_delete} has been deleted.")
            else:
                print(f"Order {order_id_to_delete} not found in the order history.")
        except ValueError:
            print("Invalid input. Please enter a valid Order ID.")
    elif delete_option == '2':
        return
    elif delete_option == '3':
        exit_program()
    else:
        print("Invalid input. Please enter 1, 2, or 3.")


def display_order_history():
    print("\nOrder History:")
    print("----------------------------")
    print("Order ID\tDate\t\tTotal Amount")
    print("----------------------------")
    for order_id, order_details in order_history.items():
        print(f"{order_id}\t\t{order_details['date']}\tPKR {order_details['total']}")
    print("----------------------------")


def exit_program():
    print("Exiting the program.")
    exit()


def main():
    global order_history

    while True:
        shopping_cart = []
        total_amount = 0

        shopping_cart, total_amount = cart_adding(shopping_cart, total_amount)
        total_amount, payment_method, details = payment(total_amount)
        consumer_details = get_details()

        current_date = date.today()
        order_id = len(order_history) + 1

        order_details = {
            'date': current_date,
            'cart': shopping_cart,
            'total': total_amount,
            'payment_method': payment_method,
            'details': details,
        }

        add_to_order_history(order_id, order_details)

        print("\nOrder Summary:")
        invoice(shopping_cart, total_amount, payment_method, consumer_details)

        action = input("\nWhat would you like to do next?\n1. View Order History\n2. Delete Order\n3. Place Another Order\n4. Exit\nEnter 1, 2, 3, or 4: ")

        if action == '1':
            display_order_history() 
            delete_order()
        elif action == '2':
            delete_order()
        elif action == '3':
            continue
        elif action == '4':
            exit_program()
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")

        another_order = input("Do you want to place another order? (yes/no): ").lower()
        if another_order != 'yes':
            exit_program()


if __name__ == "__main__":
    main()