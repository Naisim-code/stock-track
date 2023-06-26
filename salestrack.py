print('WELCOME TO STOCK TRACKING SYSTEM \n')
initial_stock = int(input("Please enter an initial stock level: "))
num_months = int(input("Please enter the number of months to plan: "))

stock_level = initial_stock
production_quantities = []

for month in range(1, num_months+1):
    sales_quantity = int(input(f"Please enter the planned sales quantity for month {month}: "))
    
    if sales_quantity <= stock_level:
        production_quantity = 0
    else:
        production_quantity = sales_quantity - stock_level
    
    production_quantities.append(production_quantity)
    stock_level += production_quantity - sales_quantity

print("The resulting production quantities are:")
for month, production_quantity in enumerate(production_quantities):
    print(f"Production quantity month {month+1} - {production_quantity}")
