for i in range(1, 5):  # Outer loop for rows (1 to 4)
    for j in range(i):  # Inner loop for characters in each row
        print('*', end='')
    print()  # Move to the next line after each row


# for i in range(1,10,1): 
#     for j in range(1,5,2): 
#         print(i,j)