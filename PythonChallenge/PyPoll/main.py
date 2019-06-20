import csv

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
electionDataRows = getCvsFile("election_data.csv")

# Total votes
totalVotes = len(electionDataRows)

# Votes per candidate
votesPerCandidate = {}
for row in electionDataRows:
	candidate = row["Candidate"]
	if candidate in votesPerCandidate:
		votesPerCandidate[candidate] = votesPerCandidate[candidate] + 1
	else:
		votesPerCandidate[candidate] = 1


# Print to both the Console and a File
with open("electionDataResults.txt", "w") as file:
	printAndFile("Election Results", file)
	printAndFile("-----------------------------", file)
	printAndFile(f"Total votes: {totalVotes}", file)
	printAndFile("-----------------------------", file)
	m = max(votesPerCandidate.values())
	for candidate in votesPerCandidate:
		if(votesPerCandidate[candidate] == m):
			winner = candidate
		percent = round((votesPerCandidate[candidate]*100)/totalVotes, 3)
		printAndFile(f"{candidate}: {percent}% ({votesPerCandidate[candidate]})", file)
	printAndFile("-----------------------------", file)
	printAndFile(f"Winner: {winner}", file)
	printAndFile("-----------------------------", file)

print()