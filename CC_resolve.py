conjunction_keywords = ["and", "but", "if", "then","so"]
verbs = ["has", "had"]
prep = ["in", "at", "on"]


def cc_resolve(sentence):
    sentSplit = sentence.split(" ")
    firstPart = []
    secondPart = []
    conjFound = 0

    for word in sentSplit:
        if word in conjunction_keywords:
            conjFound = 1
            continue
        if (conjFound == 0):
            firstPart.append(word)
        elif (conjFound == 1):
            secondPart.append(word)

    # we have two arrays which will hold  pre verb, after verb , perepositional phrase properties for each of the sentences
    # the default value of a index would be "empty"
    # [preverb,verb,afterverb,prepostion]

    firstProp = ["empty", "empty", "empty", "empty"]
    secondProp = ["empty", "empty", "empty", "empty"]

    tempSent = ""  # temp sentence that will hold everything before we encounter a keyword
    seenVerb = 0
    seenPrep = 0
    for word in firstPart:

        if word in verbs:
            seenVerb = 1
            firstProp[0] = tempSent
            firstProp[1] = word
            tempSent = ""

        if word in prep:
            seenPrep = 1
            if (seenVerb == 1):
                firstProp[2] = tempSent  # after verb
                tempSent = ""
            else:
                tempSent = word
                secondProp[2] = tempSent  # after verb
                continue

        tempSent = tempSent+" "+word
    if (seenPrep == 1):
        firstProp[3] = tempSent
        tempSent = ""
    if(seenVerb == 1 and seenPrep == 0):
        firstProp[2] = tempSent
        tempSent = ""

    tempSent = ""  # temp sentence that will hold everything before we encounter a keyword
    seenVerb = 0
    seenPrep = 0
    for word in secondPart:
        if word in verbs:
            seenVerb = 1
            secondProp[0] = tempSent
            secondProp[1] = word
            tempSent = ""

        if word in prep:
            seenPrep = 1
            if (seenVerb == 1):
                secondProp[1] = tempSent
                tempSent = ""
            else:
                secondProp[2] = tempSent
                tempSent = word
                continue

        tempSent = tempSent+" "+word
        print(tempSent)

    if (seenPrep == 1):
        secondProp[3] = tempSent
        tempSent = ""
    if(seenVerb == 1 and seenPrep == 0):
        secondProp[2] = tempSent  # after verb
        tempSent = ""
    print(firstProp)
    print(secondProp)
    finalSent1 = ""
    finalSent2 = ""

    for i in range(4):
        if (firstProp[i] != "empty"):
            finalSent1 = finalSent1+" " + firstProp[i]
        else:
            if (secondProp[i] != "empty"):
                finalSent1 = finalSent1+" "+secondProp[i]

    for i in range(4):
        if (secondProp[i] != "empty"):
            finalSent2 = finalSent2+" " + secondProp[i]
        else:
            if (firstProp[i] != "empty"):
                finalSent2 = finalSent2+" "+firstProp[i]

    print(finalSent1)
    print(finalSent2)
    answer=[finalSent1,finalSent2]
    return answer


cc_resolve("Sam had 49 pennies and 34 nickeles in his bank")
