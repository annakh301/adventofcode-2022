from asyncore import read
import read_function

cleanup_sections = read_function.read_file('input-puzzle/cleanup-sections.csv')
contained_sections = []
noncontained = []

def get_overlapped_fully(cleanup_section):
    paira, pairb = cleanup_section.split(",")
    a, b = paira.split("-")
    c, d = pairb.split("-")
    if (int(a)>=int(c) and int(b)<=int(d)) or (int(a)<=int(c) and int(b)>=int(d)):
        return cleanup_section

def get_overlapped_partially(cleanup_section):
    paira, pairb = cleanup_section.split(",")
    a, b = paira.split("-")
    c, d = pairb.split("-")

    x = list(range( int(a), int(b)))
    y = list(range(int(c), int(d)))
    x.append(int(b))
    y.append(int(d))

    z = set(x).intersection(set(y))
    if len(z) > 0:
        return cleanup_section
        
        

for section in cleanup_sections:
     contained_sections.append(get_overlapped_partially(section))
res = [i for i in contained_sections if i is not None]
print(contained_sections)

print(len(res))
