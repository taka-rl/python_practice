'''
Exercise 8: Rename key of a dictionary
Write a program to rename a key city to 
a location in the following dictionary.

Given:
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

Expected output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
'''

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

keys = ["city"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)


# sample answer
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
