import re            
            
def hodorify(word):
    hodor = ""
    length = len(word)
    
    if length == 1:
        return capify("h", word)
    elif length == 2:
        return capify("ho", word)
    elif length == 3:
        return capify("hod", word)
    elif length == 4:
        return capify("hodo", word)
    elif length == 5:
        return capify("hodor", word)
        
    # For longer words, use a GMT for the length 
    extraohs = length - len("hodor")
    hodor = "ho" + ("o" * extraohs) + "dor"
    return capify(hodor, word)
    
def capify(word, reference):
    new_word = ""
    for i, c in enumerate(reference):
        if c.isupper():
            new_word += word[i].upper()
        else:
            new_word += word[i]
    
    return new_word

with open('book.txt') as f:
    lines = f.readlines()
    
for line in lines:
    newtext = []
    things = re.findall(r"\w+|[^\w]", line, re.UNICODE)
    
    for thing in things:
        if re.match(r"\w+", thing, re.UNICODE):
            newtext.append(hodorify(thing))
        else:
            newtext.append(thing)
    
    print "".join(newtext)
