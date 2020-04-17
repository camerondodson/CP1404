"""Program to get user input and display the corresponding hexadecimal colour code"""

hex_colours_dict = {"turquoise1": "#00f5ff", "yellow1": "#ffff00", "VioletRed1": "#ff3e96",
                    "SpringGreen1": "#00ff7f", "SlateBlue1": "#836fff", "red1": "#ff0000",
                    "NavyBlue": "#000080", "magenta": "#ff00ff", "light": "#eedd82",
                    "black": "#000000"}

input_colour = input("Enter colour you wish to find hexadecimal for: ")
while input_colour != "":
    if input_colour in hex_colours_dict:
        print("The hexadecimal for", input_colour, "is", hex_colours_dict[input_colour])
    else:
        print("Invalid colour name")
    input_colour = input("Enter colour you wish to find hexadecimal for: ")
