def main():
    candidates = ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4", "Candidate 5"] 
        # Create a list with 5 names of the candidates

    votes = {candidate: 0 for candidate in candidates} 
        # Each candidate is initialized to 0 
        # (it will store the votes each candidate receives) 
        # (The dictionary is based on the list) 
        # It is defining that 0 is going to be for each candidade in the list "candidates"                                                                            

    print("Welcome to the Talent Contest Voting Program!")

    while True:
        print("\nList of Candidates:")
        for i, candidate in enumerate(candidates, start=1):
            print(f"{i}. {candidate}")
                # Enumarate: It'll count the index of each item in the list 
                # The enumaration (list of the candidates) will start with 1    
                # i = index (start the counting with 1 and follow)
                # candidate = name of the candidade
                # it'll print the number + name of the item in the list                                                                                                                                                

        vote = input("Enter the number of the candidate you want to vote for (or -1 to finish): ")
            # Ask for the vote of the user                                                                 

        if vote == "-1":
            break
                # If the vote is equal -1, it'll break and leave the program (loop)                                                               

        try:
            vote = int(vote)
                # Transform the vote into a integer

            if 1 <= vote <= len(candidates):
                selected_candidate = candidates[vote - 1]
                votes[selected_candidate] += 1
                print(f"Vote registered for {selected_candidate}!\n")
                    # If the vote is greater than 1 and smaller than the number of candidate (In the list)
                    # "selected_candidate" will be the specific item in the list based in the index 
                        # Using the input of the user - 1 (Since the number 5 is the index 4 in the list)  
                    # "votes[selected_candidate] += 1" -> will increment in the dictionary the vote count for the selected candiddate 
                    # "print(f"Vote registered for {selected_candidate}!\n")" -> This line prints a confirmation message for the registered vote.                          

            else:
                print("Invalid candidate number. Please try again.")
                    # if the value is not in the range, it'll give a warning
        except ValueError:
            print("Invalid input. Please enter a valid candidate number.")
                # It'll give a warning if the input is something that cannot become a integer

    print("\nVoting Results:")
    sorted_candidates = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    for candidate, vote_count in sorted_candidates:
        print(f"{candidate}: {vote_count} votes")
            #"sorted_candidates" -> variable in which sorted all the candidates based on the number of votes (Higher to lower - "reverse=True")
                # The base for the variable is the dictionary in which correspond with the candidate and votes  
            # Print the name of the candidate and the vote count    
            
    print("Thank you for participating in the Talent Contest!")

if __name__ == "__main__":

    main()