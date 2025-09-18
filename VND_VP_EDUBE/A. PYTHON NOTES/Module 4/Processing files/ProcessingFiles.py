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
