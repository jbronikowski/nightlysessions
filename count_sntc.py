import csv
import operator
import json

csv_file = open('sntc.csv', 'r')
csv_reader = csv.DictReader(csv_file)

products = {}
# products_list = []
software_versions = {}


for row in csv_reader:
    # if '3.6.6E' in row['SW Version']:
    # if 'FOC1912X1BV' in row['Serial Number']:
    #print(row['Product ID'])
    product = row['Product ID']
    # if product not in products_list:
    #     products_list.append(product)
    software = row['SW Version']
    
    
    if product not in products:
        products[product] = {}
    
    if 'count' not in products[product]:
        products[product]['count'] = 1
    else:
        products[product]['count'] = products[product]['count'] + 1
    
    #print(row)
    if software:
        if software not in products[product]:
            products[product][software] = 1
        else:
            products[product][software] = products[product][software] + 1
    


    # if software in software_versions:
    #     software_versions[software] = software_versions[software] + 1
    # else:
    #     software_versions[software] = 1
        #products['WS-C3750X-24T-S'] = 1

#print(products_list)
print(json.dumps(products, indent=4))
#print(software_versions)
# sorted_d = sorted(products.items(), key=operator.itemgetter(1),reverse=True)

# for key, value in sorted_d:
#     print(key,value)

# { 
#     'AIR-CAP1602E-A-K9': {
#                             "13.3" : 2,
#                             "15.6" : 6
#                         },
#     'AIR-LAP1242AG-A-K9': {
#                             "12.16" : 5,
#                             "3.6" : 7
#                         }
# }

