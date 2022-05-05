




def selection(list, question):
    for item in list:
        print("")
        print(list.index(item), item)
    
    while True:
        result = input(question)
        try:
                result = int(result)
                break
        except:
            print("Selection must be a whole number between 0-9:")

    return result