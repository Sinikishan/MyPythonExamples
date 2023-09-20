n = int(input("Enter number of rows: "))
'''
The end parameter in the print function is used to add any string.
At the end of the output of the print statement in python. By defa
ult, the print function ends with a newline.
'''
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()
