def check():
    s1=str(input("Enter the first word:"))
    s2=str(input("Enter the second word:"))
    if(sorted(s1)==sorted(s2)):
        print("Entered text is an anagram")
    else:
        print("Entered text is not an anagram")
check()
