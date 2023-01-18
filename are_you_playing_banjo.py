## Create a function that takes in a string ("name") as an argument. If the name starts with R or r, they play banjo, else they do not play banjo.

def are_you_playing_banjo(name:str):
    first_letter = name[0]
    if first_letter == 'R':
        print(f"{name} is playing banjo")
        return "{name} is playing banjo"
    elif first_letter == 'r':
        print(f"{name} is playing banjo")
        return "{name} is playing banjo"
    else:
        print(f"{name} is not playing banjo")
        return f"{name} is not playing banjo"
    
    
    
    
are_you_playing_banjo('Martin')
are_you_playing_banjo('ricky')
are_you_playing_banjo('Eloise')
are_you_playing_banjo('Robin')
