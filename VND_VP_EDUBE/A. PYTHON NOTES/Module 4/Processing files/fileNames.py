
# As you can see, systems derived from Unix/Linux don't use the disk drive letter (e.g., C:) and all the directories grow from one root directory called /, while Windows systems recognize the root directory as \.



# In addition, Unix/Linux system file names are case-sensitive. Windows systems store the case of letters used in the file name, but don't distinguish between their cases at all.

# This means that these two strings: ThisIsTheNameOfTheFile and thisisthenameofthefile describe two different files in Unix/Linux systems, but are the same name for just one file in Windows systems.

# The main and most striking difference is that you have to use two different separators for the directory names: \ in Windows, and / in Unix/Linux.

# This difference is not very important to the normal user, but is very important when writing programs in Python.

# To understand why, try to recall the very specific role played by the \ inside Python strings.



# Prev Next