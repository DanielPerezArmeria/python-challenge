import csv
from statistics import mean

# Function to get a list of the data rows as dictionaries
def getCvsFile(fileName):
	rows = list()
	with open(fileName, "r") as file:
		reader = csv.DictReader(file)
		for row in reader:
			rows.append(row)
	return rows

# Function to write to both Console and File
def printAndFile(message, f):
	print(message)
	print(message, file = f)


# The Data
bankDataRows = getCvsFile("PyBank_budget_data.csv")

# Here, we calculate both the number of months and the total of the profit/losses
numberOfMonths = len(bankDataRows)
total = 0
for row in bankDataRows:
	total += int(row["Profit/Losses"])

# In this block, we calculate the rest of the data.
# We are gonna store the month-by-month difference in a list, and work from there
differences = list()
greatestProfit = 0
greatestLoss = 0
for i in range(len(bankDataRows) - 1):
	data1 = int(bankDataRows[i]["Profit/Losses"])
	data2 = int(bankDataRows[i+1]["Profit/Losses"])
	diff = data2 - data1
	if diff > greatestProfit:
		greatestProfit = diff
		greatestProfitDate = bankDataRows[i+1]["Date"]
	if diff < greatestLoss:
		greatestLoss = diff
		greatestLossDate = bankDataRows[i+1]["Date"]
	differences.append(diff)

average = round( mean(differences), 2 )


# Print to both the Console and a File
with open("PyBankResults.txt", "w") as file:
	printAndFile("Financial Analysis", file)
	printAndFile("-----------------------------", file)

	printAndFile(f"Total number of months: {numberOfMonths}", file)
	printAndFile(f"Total: {total}", file)
	printAndFile(f"Average Change: {average}", file)
	printAndFile(f"Greatest increase in Profits: {greatestProfitDate} (${greatestProfit})", file)
	printAndFile(f"Greatest decrease in Profits: {greatestLossDate} (${greatestLoss})", file)

print()