import csv


csv_file = open('sntc.csv', 'r')
csv_reader = csv.DictReader(csv_file)

products = {}
products_list = []


for row in csv_reader:
    # if '3.6.6E' in row['SW Version']:
    # if 'FOC1912X1BV' in row['Serial Number']:
    #print(row['Product ID'])
    product = row['Product ID']
    # if product not in products_list:
    #     products_list.append(product)
    
    
    if product in products:
        products[product] = products[product] + 1
    else:
        products[product] = 1
        #products['WS-C3750X-24T-S'] = 1

#print(products_list)
print(products)


