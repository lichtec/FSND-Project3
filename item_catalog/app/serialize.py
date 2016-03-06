#quick function to help serialize results from a list (generally from a query)

def serialize(keys, values):
    if(len(keys) == len(values)):
        serial = {}
        x=0
        for key in keys:
            serial[key]=values[x]
            x=x+1
        return serial
    else:
        return('Error: lists are not the same length')