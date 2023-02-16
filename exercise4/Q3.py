
# implement a replace function that deletes then inserts
# the replace should keep the array sorted
def replace(array, newVal, oldVal):
    try:
        array.remove(oldVal)
    except:
        print("Value to be replaced was not found")
        return
    try:
        insertIndex = next(x for x,val in enumerate(array) if val > newVal)
        array.insert(insertIndex, newVal)
    except:
        array.append(newVal)

def main():
    array = [1,2,5,8,15,20,22]
    print(array)
    replace(array, 3, 5)
    print(array)

if __name__=="__main__":
    main()