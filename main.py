import linecache

def welcome():
    return str(input("\nHello! My name is The Doctor. What seems to be the problem?"))

def diagnosis():
    symptom = welcome()
    file = open('data.txt')
    result = file.readlines
    if symptom == "runny nose":
        print(linecache.getline('data.txt',2))
    elif symptom == "fever":
        print(result[1])
    elif symptom == "fever":
        print(result[2])
    elif symptom == "fever":
        print(result[3])
    else:
        print("I'm sorry, we couldn't match your condition.")
    file.close()

def exit():
    print("Thank you for using The Doctor")

def main():
    welcome()
    diagnosis()
    exit()

if __name__ == "__main__":
    main()