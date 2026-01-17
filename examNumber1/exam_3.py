class FoodDelivery:
    def __init__(self,order_number,destination,price,delivery_term,order_status):
        self.order_number = order_number
        self.destination = destination
        self.price = price
        self.delivery_term = delivery_term
        self.order_status = order_status
    
    def order_info(self):
        return f"Order Number: {self.order_number}, Destination: {self.destination}, Price: ${self.price}, Delivery Term: {self.delivery_term}, Order Status: {self.order_status}"    

    def change_term(self):
        new_term = input("New term:")
        self.delivery_term = new_term
        return f"Delivery term updated to: {self.delivery_term}"

def status_info(order_list,num):
    for i in order_list:
        if  i.order_number == num:
            print("Found")
            i.order_info
            break
        print("not found")

def add_order(order_list,order):
    order_list.append(order)

order_list = []
n = input("Order count:")
for i in range(n):
    order_number = input()
    destination = input()
    price = input()
    delivery_term = input()
    order_status = input()
    order =  FoodDelivery(order_number,destination,price,delivery_term,order_status)
    add_order(order_list,order)

num = input("Enter order number to search:")
status_info(order_list,num)