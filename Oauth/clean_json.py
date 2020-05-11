def beautify(d):
    line_items = [x for x in d['LineItems']]

    newd = {}

    for key, val in d.items():
        if val != "" and val != None:
            newd[key] = val
    newd['LineItems'] = [{} for _ in range(len(line_items))]

    for x in line_items:
        for key, val in x.items():
            if val == None:
                continue
            if val != "":
                print(line_items.index(x))
                newd['LineItems'][line_items.index(x)][key] = val

    return newd