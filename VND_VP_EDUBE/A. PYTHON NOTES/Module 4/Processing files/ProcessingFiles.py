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


###################################################

#WORKING PROCESSING COMPLETE
# from os import strerror

# try:
#     ccnt = lcnt = 0
#     with open(r"C:\Users\Tyler\OneDrive - NewBridge Graduate Institute\Desktop\file.txt", 'rt') as s:
#         for line in s:
#             lcnt += 1
#             for ch in line:
#                 print(ch, end='')
#                 ccnt += 1
#     print("\n\nCharacters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))

#####################################################
# DEALING WIH TEXT FILES: WRITE()
# from os import strerror

# try:
# 	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
# 	for i in range(10):
# 		s = "line #" + str(i+1) + "\n"
# 		for ch in s:
# 			fo.write(ch)
# 	fo.close()
# except IOError as e:
# 	print("I/O error occurred: ", strerror(e.errno))

########################################################
# BYTEARRAYS: CON
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
