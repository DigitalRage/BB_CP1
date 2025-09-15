# BB 1st Crew Shares Project
while True: 
    print("This is a file that runs how much shares each crew member has if there is enough cash to spread out, each crewmate already has 500 dollars given to them. ")
    cash = input("How much cash do you want the pirate crew to have in all? \n").strip()
    crew = input("How much people do you want in the crew? \n").strip()

    if crew.isdigit and cash.replace(".","",1).isdigit() or cash.isdigit:
        cash = int(cash)
        crew = int(crew+8)
        cap = (cash/crew)*7
        f_mate = (cash/crew)*3
        crew_mem = (cash/crew-500)
        if cash/crew <= 500:
            print(f"How much was earned: {cash:.2f}\n\nHow many crew members are there (not including the captain and first mate): {crew}\n\nThe captain gets: {cap}\n\nThe first mate gets: {f_mate}\n\n Crew still needs: {crew_mem}" )
        else: 
            print("Don't be a dingus, make sure each crewmate gets at least 500$")
    else:
        print("Don't be a dingus, Try again (with real numbers)\n")