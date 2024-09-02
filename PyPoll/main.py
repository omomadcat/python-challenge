import pandas as pd

# Load dataset
file_path = 'PyPoll/Resources/election_data.csv'
election_data = pd.read_csv(file_path)

# Calculate total number of votes cast
total_votes = election_data['Ballot ID'].nunique()

# Generate complete list of candidates who received votes
candidates = election_data['Candidate'].unique()

# Calculate total number of votes each candidate won
votes_per_candidate = election_data['Candidate'].value_counts()

# Calculate percentage of votes each candidate won
percentage_votes = (votes_per_candidate / total_votes) * 100

# Determine winner based on popular vote
winner = votes_per_candidate.idxmax()

# Prepare final analysis summary
analysis_summary = (
    f"Election Results\n"
    f"____________________\n"
    f"Total Votes: {total_votes}\n"
    f"____________________\n"
)

for candidate in candidates:
    analysis_summary += f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes_per_candidate[candidate]})\n"

analysis_summary += (
    f"____________________\n"
    f"Winner: {winner}\n"
    f"____________________"
)

# Print analysis summary
print(analysis_summary)

# Save results to a text file
output_file_path = 'printed_election_results.txt'
with open(output_file_path, 'w') as file:
    file.write(analysis_summary)
