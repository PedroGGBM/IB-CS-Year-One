def average_order_cost(cost_list): # this func calculates the average order cost by adding each total cost in list cost_list (for loop) and then divideding by the length
    total_client_costs = 0
    for i in cost_list:
        total_client_costs += i
    print(f"\nThe total average meal cost is ${total_client_costs/len(cost_list):.2f}")

def total_food_items(cost_list): # this func 
    for i in range(0, len(cost_list)):
        print(f"\nThe total order cost for customer #{i+1} was ${cost_list[i]}\n")

def total_num_items(menu_item_quantity, menu):
    for i in range(0, len(menu)):
        print(f"\nTotal number of {menu[i]}s: {menu_item_quantity[i]}")

def main():
    menu = ["Cheeseburger", "Veganburger", "Salad", "Fried", "Soda", "Water"]
    cost = [2.50, 3.75, 2.25, 1.75, 0.75, 0.80]
    cost_per_order = 0 # sum up all item costs per customer
    cost_list = [] # for average meal cost
    customer = 1 # explicitly for formatting
    menu_item_quantity = [0, 0, 0, 0, 0, 0]
    line_split = "░▒▓█ ░▒▓█▓▒░▒▓█▓▒░▒▓░▒▓█ ░▒▓█▓▒░▒▓█▓▒░▒▓"

    while True: # infinite customers unless first x input is "q"
        print(f"\nWelcome customer #{customer}! Here is the menu:\n{line_split}")
        for i in range(0, len(menu)):
            print(f"{i+1}. {menu[i]:15} ${cost[i]:.2f}") # prints the menu for each individual customer to see (beginning of each order)
        try:   
            x = input(f"What item do you wish for? Please input the number of the order (i.e. 1-6): ")
            if x == "q": # checks only for the first item query per order! 
                return average_order_cost(cost_list), total_food_items(cost_list), total_num_items(menu_item_quantity, menu) # once there are no more consumers, avergae_order_cost is returned (inheriting the cost_list as a parameter)
            else:
                x = int(x) # simply converts the x input into an int, if it were a str, it would go through the except ValueError and print the total cost ($0.00)
            while x == int(x): # checks if the x input is a digit (not int, otherwise it would never run due to the first x input): the except loop already excepts ValueErrors
                while x not in range(1, 7):
                    x = int(input(f"Invalid input, Please input the number of the order (i.e. 1-6): ")) # validation for input data
                y = int(input("How many of the item do you wish for? Please input the number (i.e. 1, 5, 7): "))
                if x == 1: 
                    menu_item_quantity[0] += y
                if x == 2:
                    menu_item_quantity[1] += y
                if x == 3:
                    menu_item_quantity[2] += y
                if x == 4:
                    menu_item_quantity[3] += y
                if x == 5:
                    menu_item_quantity[4] += y
                if x == 6:
                    menu_item_quantity[5] += y
                cost_per_order += (cost[x-1]*int(y))
                x = int(input(f"What item do you wish for? Please input the number of the order (i.e. 1-6): "))
        except ValueError: # excepts ValueError (if you input a string as an int value) and instead terminates the order and prints the total order cost
            cost_list.append(cost_per_order) # adds all of the total costs for different consumers for average 
            print(f"Your order cost is: ${cost_per_order:.2f}! Thank you for your purchase!")
            cost_per_order = 0 # sets the cost for the next consumer at 0
            customer += 1
            
main()
