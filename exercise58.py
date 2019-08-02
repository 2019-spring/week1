names = ['john', 'sudhir', 'akmal', 'admin', 'alex']

for name in names:
    if name.lower() == 'admin':
        print(f"Hello {name.title()},\nwould you like to see a status report?")
    else:
        print(f"Hello {name.title()}, thank you for logging in again.")