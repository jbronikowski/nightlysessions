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
    if product not in products_list:
        products_list.append(product)

print(products_list)


