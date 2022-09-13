age = int(input("Enter your age: "))
if age >= 18:
    vote_id = input("Enter your voter id number: ")
    length = len(vote_id)
    up_case = vote_id.upper()
    if length ==10 and "IBO" in up_case:
        print("You are eligible for voting")
    else:
        print("invalid voter id ")
else:
    print("you are not eligible for voting")
    