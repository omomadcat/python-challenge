import pandas as pd

# Load dataset
file_path = 'PyBank/Resources/budget_data.csv'
budget_data = pd.read_csv(file_path)

# Calculate total number of months included in the dataset
total_months = budget_data['Date'].nunique()

# Calculate total amount of profits and losses over the entire period
total_profit_losses = budget_data['Profit/Losses'].sum()

# Calculate changes in profits and losses over the entire period
budget_data['Profit/Losses Change'] = budget_data['Profit/Losses'].diff()

# Calculate average change in profits and losses
average_change = budget_data['Profit/Losses Change'].mean()

# Find greatest increase in profits (date and amount)
greatest_increase = budget_data.loc[budget_data['Profit/Losses Change'].idxmax()]

# Find greatest decrease in profits (date and amount)
greatest_decrease = budget_data.loc[budget_data['Profit/Losses Change'].idxmin()]

# Prepare final analysis summary
analysis_summary = (
    f"Financial Analysis\n"
    f"____________________\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Profit/Losses Change']:.0f})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Profit/Losses Change']:.0f})"
)

# Print analysis summary
print(analysis_summary)

# Save results to txt file
output_file_path = 'printed_financial_analysis.txt'
with open(output_file_path, 'w') as file:
    file.write(analysis_summary)