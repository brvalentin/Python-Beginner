



#phone2 = Phone("iPhone 13 pro", 950, 10)

#print(Item.all)
#print(Phone.all)

#Item.instantiate_from_csv()
#print(Item.all)


#Using the __init__
#item1 = Item("Phone", 100, 1)
#item2 = Item("Laptop", 1000, 3)
#item3 = Item("Cable", 10, 5)
#item4 = Item("Mouse", 50, 5)
#item5 = Item("Keyboard", 75, 5)

#print(Item.all)


#this is the filter function
#for instance in Item.all:
  #print(instance.name)

#item1.apply_discount()
#print(item1.price)

#item2 = Item("Laptop", 1000, 3)
#item2.pay_rate = 0.75
#item2.apply_discount()
#print(item2.price)

#item3 = Item("Cable", 10, 100)
#item3.pay_rate = 0.95
#item3.apply_discount()
#print(item3.price)


#print(Item.__dict__)   All the atributes for Class level
#print(item1.__dict__)   All the atributes for instance level


#when I don't use the __init__ it looks like this:
#item1.name = "Phone"
#item1.price = 100
#item1.quantity = 5
#print(item1.calculate_total_price(item1.price, item1.quantity))

#when I don't use the __init__ it looks like this:
#item2.name = "Laptop"
#item2.price = 1000
#item2.quantity = 3
#print(item2.calculate_total_price(item2.price, item2.quantity))

#item3.name = "Cable"
#item3.price = 9.00
#item3.quantity = 100

#print(item1.name)
#print(item2.name)
#print(item3.name)
#print(item1.price)
#print(item2.price)
#print(item3.price)
#print(item1.quantity)
#print(item2.quantity)
#print(item3.quantity)

#print(type(item1))
#print(type(item1.name))
#print(type(item1.price))
#print(type(item1.quantity))

#print(item1.calculate_total_price())
#print(item2.calculate_total_price())
#print(item3.calculate_total_price())