import yaml

def read_file(filename):
    ### this function reads a yaml file in and return a dictionary
    with open (filename) as fin:
        file = fin.read()
        param = yaml.load(file)
    return param