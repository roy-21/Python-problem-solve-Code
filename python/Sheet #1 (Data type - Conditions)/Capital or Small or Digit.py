X=input().strip()

#digit check

if X.isdigit():
    print("IS DIGIT")
#ck given input is alpha?
elif X.isalpha():
    print("ALPHA")
#output-yes!
    if X.isupper():
        print("IS CAPITAL") #ck capital letter!
    else:
        print("IS SMALL") #ck small letter!