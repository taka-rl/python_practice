'''
Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
Expected output:Math
'''

# sample answer
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict, key = sample_dict.get))