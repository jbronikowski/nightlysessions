
# brenda = 10
# mike = 'tina'
# jacob = [1,2,3,4,5,6,7]



# def add_values(name, age = "nothing is here", sex='male'):
#     print(age)
#     print(name)
#     print(sex)
#     print("hello world!")

# add_values('josh', 12, "female")
# add_values(12, 15)
# add_values(brenda, mike)
# add_values(mike, brenda)
# add_values(jacob, "josh", 12)
# add_values(jacob)
# add_values(age=12, sex = "female", name='josh')

import requests


def multiple(value):
    return value * 1000

def get_websites(url):
    response = requests.get(url)

    length = len(response.text)
    multiplier = multiple(length)
    return multiplier



val1 = get_websites('https://cisco.com')
val2 = get_websites('https://yahoo.com')

print(val1)
print(val2)

val3 = multiple(val2)
val4 = multiple(val3)

print(val3)
print(val4)