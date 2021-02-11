def countB(w):
    count = 0
    for i in range(0, len(w)):
        if w[i] == "b":
            count = count + 1
    
    return count 

print(countB("baseball"))

def removeLast(w):
    letter = w[-1]
    
    return letter

print(removeLast("winter"))

def firstLast(w):
    if w[0] == w[-1]:
        return True
    else:
        return False

print(firstLast("alph"))

def firstLast(w):
    if w[0] == w[-1]:
        return True
    else:
        return False 

print(firstLast("roar"))