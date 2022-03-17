def count_cur_words(filename, word):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        count = contents.lower().count(word)
        print("The file " + filename + " has about " + str(count) + " '" + word + "'.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
    count_cur_words(filename, 'the')
