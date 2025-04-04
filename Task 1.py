try:
    file1 = open("sample.txt","r")
    print("Reading file content:")
    reading_file = file1.readline()
    print("Line 1:", reading_file)
    reading_file2 = file1.readline()
    print("LIne 2:", reading_file2)
    file1.close()
except FileNotFoundError:
    print("Error: The file sample.txt was not found")
