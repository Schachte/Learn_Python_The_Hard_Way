################################
######### Excercise 08##########
# Learning Python The Hard Way#
####### Ryan Schachte ##########
################################

'''
ONLY INTS AND BOOLEANS DON'T CONTAIN SINGLE QUOTES
'''

#Initial string with re-formatted string format of representations in body of string
formatter = "%r %r %r %r"

#Replacing each %r in the formatter string with integers
print formatter % (1, 2, 3, 4)

#Single quotes show around %r string formatting
print formatter % ("one", "two", "three", "four")

#Replace %r with booleans (no single quotes)
print formatter % (True, False, False, True)

#Replace formatter with the original formatter 4 different times w/ single quotes around each block
print formatter % (formatter, formatter, formatter, formatter)

#Single quotes around each %r representation and the commas combine everything onto one line
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)