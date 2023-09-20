# Python3 code to demonstrate
# each occurrence frequency using
# dict.get()

# initializing string
test_str = "SiniRajPulari"

# using dict.get() to get count
# of each element in string
result = {}

for keys in test_str:
	result[keys] = result.get(keys, 0) + 1

# printing result
print ("Count of all characters in SiniRajPulari is : \n"
											+ str(result))
