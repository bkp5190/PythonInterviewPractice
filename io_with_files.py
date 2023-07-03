# Outline the different functionalities to interacting with files in Python.

def main():
    myfile = open('example.txt')
    print("FIRST READ\n", myfile.read())

    # Reset the pointer inside the file
    # myfile.seek(0)
    print("SECOND READ", myfile.read())
    myfile.seek(0)
    print(myfile.readlines())
    # Important to keep in mind that file paths are different between OS
    # Windows: 'C:\\Users..'
    # MacOS/Linux: 'Users/'
    myfile.close()

    with open('example.txt', 'r') as myfile:
        contents = myfile.read()
        print(contents)

    # Modes for files:
    # 'r': read only
    # 'w': write only
    # 'a': append only
    # 'r+': reading and writing
    # 'w+': writing and reading (Overwrites)
    with open('my_new_file.txt', 'r') as f:
        print(f.read())

    with open('my_new_file.txt', 'a') as f:
        print(f.write('\nFOUR ON FOURTH'))

    with open('my_new_file.txt', 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()