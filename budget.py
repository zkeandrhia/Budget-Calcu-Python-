''' enter amount budgeted in a month
write expenses
wriote over/ under'''

def budget_month():
    
    user = float(input('Budget for a month: '))
    expenses = 'y'
    totalexpenses = 0
    
    while expenses == 'y':
        
        userexpenses = float(input('Expenses: '))
        totalexpenses += userexpenses
        expenses = input('More expenses? (y/n): ')
        total= totalexpenses - user
    if totalexpenses > user:
        print(f'Over budget of {user}, by {total}.')
    if user > totalexpenses:
        print(f'Under budget of {user}, by {total}.') 
    if user == totalexpenses or totalexpenses == user:
        print('Great you were on budget!')   
    
budget_month()