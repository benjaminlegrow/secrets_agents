def title():
    print("Welcome to the Secret Agent Database \n")


agents = {"ShadowWolf" : "Avery Black", "GhostFalcon" : "Ben LeGrow", "NightTiger" : "Scott Adams"}

def menu():
    print("1. Add Agent")
    print("2. Reveal real name")
    print("3. Delete agent")
    print("4. List agents")
    print("5. Exit\n")
    try:
        choice = int(input("Please put the number of the operation you would like to carry out: "))
        return choice
    
    except ValueError:
        print("Invalid input, please enter a number from 1-5")
        return None

def add_agent():
    new_agent_code = input("Please choose a code name for the agent: ")
    new_agent_real = input("Please enter the real name for the agent: ")
    agents[new_agent_code] = new_agent_real
    print("Agent has been added")


def reveal_real_name():
    name_code = input("Please enter agent code name: ")
    real = agents.get(name_code)
    if real:
        print(f"The real name of agent {name_code} is {real}")
    
    else:
        print("This is an invalid code name.")
    

def delete_agent():
    users_choice = input("Please choose an agent to get rid of (enter codename): ")
    if users_choice in agents:
        del agents [users_choice]
        print("Agent has been removed")
        
    
    else:
        print("This is an invalid code name.")


def listing_agents():
    print("Listing Agents...")
    if agents:
        for code, real in agents.items():
            print(f"Code name: {code}. Real Name: {real}")
        
    else:
        print("No agents available.")


def keep_going():
    keep_going_choice = input("Preform another operation (Y/N)?: ").upper()
    return keep_going_choice


def choice_undertaker(choice):
    if choice == 1:
        add_agent() #Adds agents
    
    elif choice == 2:
        reveal_real_name() #Reveals agents names

    elif choice == 3:
        delete_agent() #Gets rid of agents

    elif choice == 4:
        listing_agents() #Lists off all the agents

    elif choice == 5:
        print("Okay, goodbye.") #exits the program
        
    else:
        print("Invalid input")


def main():
    while True:
        title() #Gives title
        choice = menu() #Gives choice of what operaion user wants to carry out
        choice_undertaker(choice)   #puts all the functions for every operation a user could choose into one
        keep_going_choice = keep_going() #Asks if the user wants to continue

        if choice is None: #If the user enters an invalid input
            continue

        if keep_going_choice == "Y":
            continue

        elif keep_going_choice == "N":
            print("Ok, thank you for using Secret Agent Database.")
            break

        else:
            print("Invalid input")

    
if __name__ == "__main__":
    main()