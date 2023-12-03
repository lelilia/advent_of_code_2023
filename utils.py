def get_input_lines(filename):
    with open(filename, "r") as f:
        return f.readlines()

def get_input(filename):
    with open(filename, "r") as f:
        return f.read()