bug_id_input = input("What is the bug id? ")
key_id_input = input("What is the column? ")
value_id_input = input("What is the " + key_id_input + " you are looking for? ")

def search_data(bug_id, key, value):
    print(key, value)
    f = open(bug_id + '.csv', 'a')
    with open('sntc.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            # if '3.6.6E' in row['SW Version']:
            # if 'FOC1912X1BV' in row['Serial Number']:
            if value in row[key]:
                f.write(bug_id + ',' + row['Hostname'] + ',' + row['IP Address'] + ',' + row['Serial Number'] + ',' + row['Product ID'] + ',' + row['SW Version'] + '\n')
                print(row['Hostname'], row['IP Address'], row['Serial Number'], row['Product ID'], row['SW Version'])
    print('######################')


# search_data('csv5678', 'Serial Number', 'FDO2143V0TC')
# search_data('csv0000', 'SW Version', '3.6.6E')
# search_data('csv1111', 'IP Address', '10.1.100.40')
# search_data('csv12', 'Product ID', 'AIR-CAP3702I-B-K9')

# return_value = send_data("Mike")

# print(return_value)
