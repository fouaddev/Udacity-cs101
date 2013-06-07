def split_string(source,splitlist):
    token = ""
    tokenlist = []
    src_length = len(source)
    for i in range(0,src_length):
        if (source[i] in splitlist):
            # peek and advance until we find a char not in the splitlist
            if i < (src_length -1) and source[i + 1] in splitlist:
                continue
            tokenlist.append(token)
            token = ""
        else:
            token = token + source[i]
    if token != "":
        tokenlist.append(token)
    return tokenlist
               
out = split_string("State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']