"""These are variables to contain the name of the candidate
    you can write as many variables of candidates names for as many candidates
"""
candidate1_name = input("Enter the name of the first candidate!!")
candidate2_name = input("Enter the name of the second candidiate!!")
"""
    This line of code below contains the no. of votes of people that voted to the
    candidates
"""
candidate1_vote = 0
candidate2_vote = 0
"""
    the below line of code is a list that contains all the voter id's
"""
voters_id = [101,102,103,104,105]
voted= []
while True:
    if voters_id == []:
        print("Voting is done!!")
        if candidate1_vote>candidate2_vote:
            print(f"{candidate1_name} won the voting , the votes for {candidate1_name} is {candidate1_vote} ")
        elif candidate2_vote>candidate1_vote:
            print(f"{candidate2_name} won the voting , the votes for {candidate2_name} is {candidate2_vote} ")
        else:
            print("The voting is tied!!")
        break
    else:
        voter = int(input("Enter your id no.!!"))
        if voter in voted:
            print("You already voted!!")
        else:
            if voter in voters_id:
                print(f"1.{candidate1_name}\n2.{candidate2_name}")
                choice = int(input("enter your choice!!"))
                if choice == 1:
                    candidate1_vote+=1
                    print(f"You voted {candidate1_name}")
                else:
                    candidate2_vote+=2
                    print(f"You voted {candidate2_name}")
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("You are not allowed vote!!")
