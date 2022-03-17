def read_file(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Can't find the file " + filename + ".")
    else:
        print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_file(filename)