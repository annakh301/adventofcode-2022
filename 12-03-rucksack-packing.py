import read_function

rucksack_items = read_function.read_file('input-puzzle/rucksack-content.csv')

with open() as f:
    lines = f.readlines()
    for line in lines:
        item = line[:-1]
        rucksack_items.append(item)   

def assign_points(rucksack_item):
    if rucksack_item.isupper():
        letter_point = ord(rucksack_item) - 64+26
    else: 
        letter_point = ord(rucksack_item) - 96
    return letter_point

get_points = []
# for rucksack in rucksack_items:
#     compartment_size = int(len(rucksack)/2)
#     a, b = rucksack[:-compartment_size], rucksack[-compartment_size:]
#     print(rucksack)
#     print(list(a),list(b))
#     common_item = set(list(a)).intersection(set(list(b)))
#     common_item_string = ''.join(common_item)
#     get_points.append(assign_points(common_item_string))

counter = 0
rucksack_group = []
elf_group_of_three = []
for rucksack in rucksack_items:
    counter = counter +1
    rucksack_group.append(rucksack)   
    if counter % 3 == 0:
        elf_group_of_three.append(rucksack_group)
        print(counter, rucksack_group)
        common_item = set(list(rucksack_group[0])).intersection(set(list(rucksack_group[1])), set(list(rucksack_group[2])))
        common_item_string = ''.join(common_item)
        print(common_item_string)
        get_points.append(assign_points(common_item_string))
        rucksack_group = []
        
print(elf_group_of_three)
print(sum(get_points))


