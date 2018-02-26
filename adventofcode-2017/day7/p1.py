has_parent = set()
program_names = set()

with open('input.txt', 'r') as fp:
    for line in fp:
        if '->' in line:
            name, subtower = line.split('->')
            name = name.strip().split()[0]
            subtower = subtower.strip().split(', ')

            program_names.add(name)
            for subtower_name in subtower:
                has_parent.add(subtower_name)

print program_names - has_parent
