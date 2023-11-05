
def takeUserPreference():
    preference = input("Describe the meal you would like:")
    return preference

def additionalPreference():
    preference = input("Would you like the meal modified, else type 'NO'")
    if(preference[0]=='N'and preference[1]=='O'):
        return -1
    return preference