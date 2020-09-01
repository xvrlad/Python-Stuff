"""
Xavier Ladores
xlad198
Program that uses a dictionary of colours and a pattern text file to draw
pixel art.
"""
from tkinter import *

#-------------------------------------------
#-------------------------------------------
# main() function
#-------------------------------------------
def main():
    prompt1 = "Enter a palette filename: "
    for_colours_dict = input(prompt1)
    prompt2 = "Enter a pattern filename: "
    for_pattern_list = input(prompt2)
    list1 = process_file(for_colours_dict)
    list2 = process_file(for_pattern_list)
    
    size = 50
    start_left = size * 2
    start_down = size * 2
    #replace these two lines in step 8
    pattern_list = create_pattern_list(list2)
    colours_dictionary = create_colours_dict(list1)
    
    number_of_rows = len(pattern_list)	
    number_of_columns = len(pattern_list[0])
    canvas_width = size * number_of_columns +size * 4
    canvas_height = number_of_rows * size + size * 4
    window = Tk() 
    window.title("A5 by xlad198") 
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill = BOTH, expand = True) #Canvas fills the whole window  
    draw_pattern(a_canvas, colours_dictionary, pattern_list, size, start_left, start_down)
    window.mainloop()

def split_digits(line):
    split_list = list(line)
    position = 0
    for iterations in range(len(split_list)):
        split_list[position] = int(split_list[position])
        position += 1
    return split_list

def process_file(filename):
    read_file = open(filename, "r")
    contents = read_file.read()
    read_file.close()

    strings_list = contents.split("\n")
    return strings_list
    
def create_colours_dict(lines):
    colours_dict = {}
    colon = ":"
    for strings in lines:
        colon_index = strings.find(colon)
        key = int(strings[: colon_index])
        value = strings[colon_index + 1 :]
        colours_dict[key] = value
    return colours_dict
    
def create_pattern_list(lines):
    position = 0
    position2 = 0
    for loops in range(len(lines)):
        if position <= len(lines):
            lines[position] = list(lines[position])
            new_list = lines[position]
            for elements in new_list:
                elements = int(elements)
                new_list[position2] = elements
                position2 += 1
            position2 = 0
            position += 1
    return lines
        

def draw_pattern(a_canvas, colours_dictionary, pattern_list, size, left, top):
    possible_digits = "0123456789"      
    down = top
    #complete this
    fixed_left = left
    for elements in pattern_list:
        for integers in elements:
            a_canvas.create_rectangle(left, top, left + size,
                                    top + size,
                                    fill= colours_dictionary[integers])
            left += size
        left = fixed_left
        top += size
    return
            
main()
