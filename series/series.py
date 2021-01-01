def slices(series, length):
    output = []
    if (length < 1) or (len(series) < length):
        raise ValueError(".+")
    for i in range( len(series) - length + 1 ):
        output.append(series[i:length+i])
    return output