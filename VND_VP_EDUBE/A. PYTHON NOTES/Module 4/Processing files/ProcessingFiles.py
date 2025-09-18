# import errno

# try:
#     s = open("C:\Users\Tyler\OneDrive - NewBridge Graduate Institute\Desktop\file.txt", "rt")
#     # Actual processing goes here.
#     s.close()
# except Exception as exc:
#     if exc.errno == errno.ENOENT:
#         print("The file doesn't exist.")
#     elif exc.errno == errno.EMFILE:
#         print("You've opened too many files.")
#     else:
#         print("The error number is:", exc.errno)

# try:
#     stream = open("C:\Users\User\Desktop\\file.txt", "rt")
#     # Processing goes here.
#     stream.close()
# except Exception as exc:
#     print("Cannot open the file:", exc)

# Opening tzop.txt in read mode, returning it as a file object:
# stream = open("tzop.txt", "rt", encoding = "utf-8")

# print(stream.read()) # printing the content of the file




#WORKING PROCESSING COMPLETE
from os import strerror

try:
    ccnt = lcnt = 0
    with open(r"C:\Users\Tyler\OneDrive - NewBridge Graduate Institute\Desktop\file.txt", 'rt') as s:
        for line in s:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))