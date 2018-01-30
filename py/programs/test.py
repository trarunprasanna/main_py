name="happy_birthday"
print (name[:])
print (name[:name.index("_")])

# here is a very long word

word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"
# and store it in the answer variable....

answer = (word[word.index("antidis"):word.index("establishmen")])
print (answer)
#erase me and enter slice here...



word1 = "antidisestablishmentarianism"
# use a slice to take out the word "establishment"
answer1 = word1[7:20]
print (answer1)