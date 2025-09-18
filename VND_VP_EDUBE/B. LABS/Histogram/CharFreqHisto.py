from os import strerror

# Initialize 26 counters for each Latin letter.
# Note: we've used comprehension to do that.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    f = open(file_name, "rt")
    for line in f:
        for char in line:
            # If it is a letter...
            if char.isalpha():
                # ... we'll treat it as lower-case and update the appropriate counter.
                counters[char.lower()] += 1
    f.close()
    # Let's output the counters.
    for char in counters.keys():
        cnt = counters[char]
        if cnt > 0:
            print(char, '->',cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
##

## WHEN ENTERING SRCNAME AND DESTINATION NAME, BEST WAY TO MANUALLY INPUT DATA IS TO ADD DIRECT LOCATION
# from os import strerror

# srcname = input("Enter the source file name: ")
# dstname = input("Enter the destination file name: ")

# try:
#     with open(srcname, 'rb') as src, open(dstname, 'wb') as dst:
#         buffer = bytearray(65536)
#         total = 0
#         readin = src.readinto(buffer)
#         while readin > 0:
#             written = dst.write(buffer[:readin])
#             total += written
#             readin = src.readinto(buffer)
#     print(total, 'byte(s) successfully written')
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))