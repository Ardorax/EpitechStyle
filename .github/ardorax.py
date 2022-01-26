#
# Create your own file like this one !
# Create a function with argument self and line
# The self argument is for the class
# The line argument is the current line
#
# Use self.error_creator("ERROR MESSAGE", error_type)
# error_types : 0 -> MAJOR
# error_types : 1 -> MINOR
# error_types : 2 -> INFO
#

def trailing_spaces(self, line:str):
    if (line.endswith(" \n")):
        self.error_creator("Trailing space", 1)