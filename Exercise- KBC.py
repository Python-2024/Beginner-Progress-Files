que = [
       ["National bird?\nA) Peacock\nB) Pegion\nC) Humming Bird"], 
       ["National Animal?\nA) Lion\nB) Penguin\nC) Tiger"], 
       ["Which one is simpler; Python vs C++?\nA) Python\nB) C++"]
       ]
ans = ["A", "C", "A"]
prize = 0
print("\n--__-- WELCOME TO THE KBC --__--\n")
for ques in range(0, len(que)):
    print(que[ques][0])
    us_val = input("\nYour ans: \n").upper()
    if us_val == ans[ques]:
        print("Your Answer is Correct! \n")
        prize += 100
    else:
        print("Your Answer is Wrong! \n")
        break

print(f"Ammount won: {prize}")