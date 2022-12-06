def read_file(path):

    items = []
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            item = line[:-1]
            items.append(item)  
        return items