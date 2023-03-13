import csv

with open('election_data.csv', 'r') as file:
    election_data = csv.reader(file)
    next(election_data)

    total_votes = 0
    candidate_votes = {}
    candidate_percentages = {}

    
    for row in election_data:
        total_votes += 1
        candidate = row[2]
        
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

   
    for candidate in candidate_votes:
        percentage = candidate_votes[candidate] / total_votes * 100
        candidate_percentages[candidate] = percentage

   
    winner = max(candidate_votes, key=candidate_votes.get)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidate_votes:
        print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    
