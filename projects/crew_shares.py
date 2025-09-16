# BB 1st Crew Shares Project
while True: 
    print("This is a file that runs how much shares each crew member has if there is enough cash to spread out, each crewmate already has 500 dollars given to them. ")
    cash = input("How much cash do you want the pirate crew to have in all? \n").strip()
    crew = input("How much people do you want in the crew (not including captain of first mate)? \n").strip()

    if  cash.replace(".","",1).isdigit() and crew.isdigit():
        cash = float(cash)
        crew = int(crew)
        shares = crew+10
        cap = (cash/shares)*7
        f_mate = (cash/shares)*3
        crew_mem = (cash/shares-500)
        if cash/shares >= 500:
            print(f"\nHow much was earned: {cash:.2f}\n\nHow many crew members are there (not including the captain and first mate): {crew}\n\nThe captain gets: {cap:.2f}\n\nThe first mate gets: {f_mate:.2f}\n\nCrew still needs: {crew_mem:.2f}\n" )
            break
        else: 
            print("Don't be a dingus! Make sure each crewmate gets at least $500 (at least $5000 + $500 per crew mate, since the captain and first mate together get 10× the amount)")
    else:
        print("Don't be a dingus! Try again with real numbers.\n")