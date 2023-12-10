"""
- 5 candidates 
- User will select the candidate adn vote for it 

- Should display the list of the cadidates in order of the votes 
"""

list_candidates = ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4", "Candidate 5"]

for x in list_candidates:
    vote_input = float(input(f"Enter the vote for {x}: "))