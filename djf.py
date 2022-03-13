

def Member(AVAILABLE_set, SELECTED_set) :
    if AVAILABLE_set.intersection(SELECTED_set):
        return True
    else:
        return False

AVAILABLE = [0, -1, -2, -3, 1,44,4,4,2,2,2,23,4,4,5,4,2,24,4] #can add more numbers to make it 100

SELECTED = [2]
AVAILABLE_set=set(AVAILABLE)
SELECTED_set=set(SELECTED)
if (Member(AVAILABLE_set,SELECTED_set)):
    print ("There is a match")
else:
    print ("There is no match")
 