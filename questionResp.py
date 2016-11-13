remove = input('Would you like a cookie? (y/n): ')
print(remove)
if remove == 'y':  # or 'Y' or 'YES' or 'Yes':
    remove2 = input('Are you sure you would like a cookie? (y/n): ')
    print(remove2)
    if remove2 == 'y':  # or 'Y' or 'YES' or 'Yes':
        print('Well fine take your damn cookie!')
    else:
        print('You indicisive prick!')
else:
    print('What my cookies arent good enough for you?! Dick.')
