wr = str(input("Enter text to write to the file:"))
file3 = open("output.txt","w")
writing_file = file3.write(wr)
print("Data successfully written to output.txt.")
file3.close()

file4 = open("output.txt","a")
ap = str(input("Enter additional text to append:"))
append_file = file4.write(ap)
print("Data successfully appended.")
file4.close()

print("Final content of output.txt:")
file5 = open("output.txt","r")
reading_file = file5.readline()
print(reading_file)


