from collections import OrderedDict

program_language = OrderedDict()

program_language['P'] = 'Python'
program_language['C'] = 'C'
program_language['C++'] = 'C plus plus'
program_language['C#'] = 'C Sharp'

for key, value in program_language.items():
    print(key, ":" , value)
