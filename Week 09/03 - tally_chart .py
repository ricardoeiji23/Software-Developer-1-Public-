candidates = ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4", "Candidate 5"]

votes = {candidate: 0 for candidate in candidates} 
    # First define the 0 to X for each X in the list
    # The order of the Y's is (Candidate name) and (Vote count)  

print("Welcome to the Talent Content Voting Program!")

while True:
    print("\nList of the candidates:")
    for index, candidate in enumerate(candidates, start=1): #Getting the index and X in the list (That the index will start with 1)
        print(f"{index}. {candidate}")

    vote = input("Enter the number of the candidade you want to vote for (or -1 to finish): ")

    if vote == "-1": #Since the input is a string, we need to use " " for the -1 (Value that the input will add)
        break

    try:
        vote = int(vote) # Transform the input into a integer, since only can use it for the if(<, >, =)

        if 1 <= vote <= len(candidates): # Lower than the quanntity of X's in the list
            selected_candidate = candidates[vote-1] # The "selected_candidate" is the X of the list (Use the index "voto - 1" to see the correspondent X - Since the index 4 is the 5 in the voting)

            votes[selected_candidate] += 1 #The selected candidate is the X of the list (Now add +1)

            print(f"Vote registered for {selected_candidate}!") 
        
        else:
            print("Invalid candidate number. Please, try again.")

    except ValueError:
        print("Invalid input. Please enter a valid candidate number")

    
    
print ("\nVoting results")

sorted_cadidates = sorted(votes.items(), key=lambda x: x[1], reverse=True) 
    # We are sorting based on the dictionary of "votes" that have 2 values: Name and Votes
    # "key=lambda x: x[1]" -> It's based on the number of votes (index 0 = candidate / index 1 = votes)
    # "reverse=True" -> The order of the sorting will be from Higher to lower 

for candidate, vote_count in sorted_cadidates:
    print(f"{candidate}: {vote_count} votes")  
        # Take the 2 values of the dictionary sorted (sorted_cadidates) 
        # The order of the X's is (Candidate + Vote count)  

print("Thank you!") 
