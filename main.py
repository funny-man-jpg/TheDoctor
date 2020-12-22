def readData(filename):
    data = []
    try:
        # Opening the file
        with open(filename) as file:
            # Loop through line by line
            for line in file:
                # split line using separator, store it in variable s
                s = line.split("-->")
                # if s is size 2
                if len(s) == 2:
                    # set first element stripped to symptom
                    symptom = s[0].strip()
                    # set second element  stripped to diagnosis
                    diagnosis = s[1].strip()
                    # add to data a list of symptom, diagnosis
                    data.append([symptom, diagnosis])
    except Exception as e:
        print(f"Unexpected error: {e}")
    return data


def findDiagnosis(data, userInput):
    found = False
    # Loop through each element of data
    for item in data:
        symptom = item[0]
        diagnosis = item[1]
        # if symptom is in userInput
        if symptom in userInput:
            # print "You have {diagnosis}"
            print(f"You have {diagnosis}")
            # set found = true
            found = True

    return found


def main():
    data = readData('data.txt')
    userInput = input(
        "Hello! My name is The Doctor. What seems to be the problem?\n")
    

    found = findDiagnosis(data, userInput)
    if not found:
        print("I'm sorry, we couldn't match your condition.")


if __name__ == "__main__":
    main()