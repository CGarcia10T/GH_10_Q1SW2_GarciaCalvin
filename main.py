from pyscript import display

# string data type
resturant_name = "The Cornerstore"
owner_name = "Calvin Garcia"

# integer data type
year_established = 2009

# float data type
popular_item_price = 15.99
tax_rate = 0.085

# boolean data type
has_delivery = True

# list data type
product_names = ["Four Cheese Pizza", "Pepperoni Pizza", "Margherita Pizza", "Spinach Pizza", "Hawaiian Pizza", "Meat Lover's Pizza"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
common_allergens = ["Dairy", "Soy", "Eggs", "Wheat", "Tomato"]

# dictionary data type
business_hours = {"Monday": "7:00AM-9:00PM", "Tuesday": "7:00AM-9:00PM", "Wednesday": "7:00AM-9:00PM", "Thursday": "7:00AM-9:00PM", "Friday": "7:00AM-7:00PM", "Saturday": "7:00AM-7:00PM", "Sunday": "7:00AM-7:00PM"}
menu_prices = {"Four Cheese Pizza": 499.99, "Pepperoni Pizza": 399.99, "Margherita Pizza": 399.99, "Spinach Pizza": 399.99, "Hawaiian Pizza": 350.99, "Meat Lover's Pizza": 499.99,}

display(f'{resturant_name}', target='header')
display(f'Owner: {owner_name}', target='header')
display(f'Since {year_established}', target='header')

display(f'{product_names[0]}', target='product1')
display(f'{product_names[1]}', target='product2')
display(f'{product_names[2]}', target='product3')
display(f'{product_names[3]}', target='product4')
display(f'{product_names[4]}', target='product5')
display(f'{product_names[5]}', target='product6')

display(f'{menu_prices[product_names[0]]}', target='price1')
display(f'{menu_prices[product_names[1]]}', target='price2')
display(f'{menu_prices[product_names[2]]}', target='price3')
display(f'{menu_prices[product_names[3]]}', target='price4')
display(f'{menu_prices[product_names[4]]}', target='price5')
display(f'{menu_prices[product_names[5]]}', target='price6')

display(f'Opens: {business_hours[days[0]]}', target='schedule')

