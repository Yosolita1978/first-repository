# encoding: utf-8

prices = {'Laptop': 1000, 'Iphone': 666, 'Kindle': 459, 'Ipad': 750, 'Iwatch': 1800}
stock = {'Laptop': 5, 'Iphone': 4, 'Kindle': 3, 'Ipad': 2, 'Iwatch': 1}
total = 0
shop_list = []

def show(stock):
    for element in stock:
        print "* " + element

def question():
    prompt = "What do you want to buy: "
    action = raw_input(prompt)
    return action
   

print "Hi, How I can help you "
show(prices)

while True: 
    item = question()

    if item == "":
        print "Your Total is", total
        show(shop_list) 
        break

    elif item in prices and stock[item] > 0:    
        total += prices[item]
        stock[item] -= 1 
        shop_list.append(item)

    else:
        print "We don't have that item" 
        
