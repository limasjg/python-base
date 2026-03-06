# Match-case statement (switch) an a alternative to use many elifs

def day_of_week(day):
    match day:
        case 1:
            return "It's Monday"
        case 2:
            return "It's Tuesday"
        case 3:
            return "It's Wednesday"
        case 4:
            return "It's Thursday"
        case 5:
            return "It's Friday"
        case 6:
            return "It's Saturday"
        case 7:
            return "It's Sunday"
        case _: # Using like else
            return "Invalid day"
        
print(day_of_week(616))