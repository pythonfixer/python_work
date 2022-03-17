filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    results = contents.replace("Python", "C")
    print(results)
print("\n")

with open(filename) as file_object:
    for line in file_object:        
        result = line.replace('Python', 'C')
        print(result.rstrip())
print("\n")


with open(filename) as file_object:
    lines = file_object.readlines() 
    
for line in lines:   
    result = line.replace('Python', 'C')
    print(result.rstrip())
