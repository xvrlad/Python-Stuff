"""
Lab 4:
"""

def main():
    print(remove_spaces("1 5 67 88"))
    print()

    remove_spaces("programming  is such fun,  fun,   fun")
    print()

    remove_spaces("1 5 67 88    ")
    print()

    remove_spaces("    1 5    67 88")
    print()
    remove_spaces("156788")

def remove_spaces(phrase):
    space_finder = phrase.find(" ")
    last_character = phrase[-1]
    while space_finder > -1:
        string_part = phrase[:space_finder]
        phrase = phrase[space_finder + 1:]
        space_finder = phrase.find(" ")
        print(string_part, end= "")
    if space_finder == -1:
        string_part_end = phrase[:space_finder]
        print(string_part_end, end= "")
    return last_character
        


##    string_part = phrase[:space_finder]
##    print(space_finder, string_part, end= "")
##    phrase = phrase[space_finder + 1:]
##    space_finder = phrase.find(" ")
##    string_part = phrase[:space_finder]
##    print(space_finder, string_part, end= "")
##    phrase = phrase[space_finder + 1:]
##    space_finder = phrase.find(" ")
##    string_part = phrase[:space_finder]
##    print(space_finder, string_part, end= "")
##    phrase = phrase[space_finder + 1:]
##    space_finder = phrase.find(" ")
##    string_part = phrase[:space_finder]
##    print(space_finder, string_part, end= "")
##    phrase = phrase[space_finder + 1:]
##    space_finder = phrase.find(" ")
##    string_part = phrase[:space_finder]
##    print(space_finder, string_part, end= "")
##    return
    
    #this stores the index value for spaces
##    while len(str(space_finder)) == 1:
##        string_part = phrase[:space_finder]
##        phrase = phrase[space_finder + 1:]
##        space_finder = phrase.find(" ")
##        print(string_part, end= "")
##    return 
        
    
    
##    spaces = phrase.find(" ")
##    while spaces != None:
##        spaces = phrase.find(" ")
##        string_part = phrase[:spaces]
##        phrase = phrase[spaces + 1:]
##    return string_part
##    full_string = string_part 
##    return full_string


    
##        string = phrase[:spaces]
##        print(string, end="")
##    return

main()








