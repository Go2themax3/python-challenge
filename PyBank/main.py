import csv

with open('budget_data.csv', 'r') as file:

    budget_data = csv.reader(file)
    next(budget_data)

    # Set variables
   
    total_months = 0
    net_profit_loss = 0
    monthly_changes = []
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]

    # Loop through each row 
    for row in budget_data:
        total_months += 1
        net_profit_loss += int(row[1])

        
        if total_months > 1:
            monthly_change = int(row[1]) - previous_profit_loss
            monthly_changes.append(monthly_change)

            if monthly_change > greatest_increase[1]:
                greatest_increase = [row[0], monthly_change]
            elif monthly_change < greatest_decrease[1]:
                greatest_decrease = [row[0], monthly_change]

        
        previous_profit_loss = int(row[1])

    
    average_change = sum(monthly_changes) / len(monthly_changes)

  
    print(f'Total number of months: {total_months}')
    print(f'Net profit/loss: {net_profit_loss}')
    print(f'Average change in profit/loss: {average_change}')
    print(f'Greatest increase in profit/loss: {greatest_increase[0]} ({greatest_increase[1]})')
    print(f'Greatest decrease in profit/loss: {greatest_decrease[0]} ({greatest_decrease[1]})')


   
    
