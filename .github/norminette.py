import imp
import os

class Norminette:
    def __init__(self) -> None:
        self.major = 0
        self.minor = 0
        self.info = 0
        self.trace = ""
        self.current_file = ""
        self.file_trace = ""
        self.count_line = -1
        self.folder_explorer(".")

    def folder_explorer(self, path) -> None:
        for element in os.listdir(path):
            if os.path.isdir(path + "/" + element) and element[0] != ".":
                self.folder_explorer(path + "/" + element)
            else:
                if (element.startswith(".")):
                    continue
                if (element.endswith(".c") or element.endswith(".h") or \
                    element.startswith("Makefile")):
                    self.file_explorer(path + "/" + element)
                else:
                    self.current_file = path + "/" + element
                    self.error_creator("Wrong file", 0)

    def file_explorer(self, path):
        self.file_trace = ""
        self.current_file = path
        file = open(path)
        self.count_line = 1
        for line in file:
            self.trailing_spaces(line)
            self.count_line += 1

        # End of file
        self.count_line = -1
        if (self.file_trace != ""):
            self.trace += "\n# In file " + path + "\n"
            self.trace += self.file_trace

    def error_creator(self, desc: str, type : int):
        error = ["[MAJOR]", "[MINOR]", "[INFO]"]
        if (type == 0):
            self.major += 1
        elif (type == 1):
            self.minor += 1
        else:
            self.info += 1

        if (self.count_line == -1):
            self.file_trace += f"{error[type]}: File at {self.current_file} : {desc}\n"
        else:
            self.file_trace += f"{error[type]}: At line {self.count_line} : {desc}\n"

    # Here import coding style function
    from ardorax import trailing_spaces
