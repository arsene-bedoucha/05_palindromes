""" Ce module renvoie si des mots dans une liste sont des palindromes ou non"""

#### Fonction secondaire ###

def ispalindrome(p):
    """La fonction regarde si un mot est un palindrome ou pas"""

    a = p.lower()
    a = a.replace("é", "e")
    a = a.replace("è", "e")
    a = a.replace("à", "a")
    a = a.replace("ê", "e")
    a = a.replace("ë", "e")
    a = a.replace("ô", "o")
    a = a.replace(",", "")
    a = a.replace("'", "")
    a = a.replace(" ", "")
    a = a.replace("-", "")
    a = a.replace(".", "")
    a = a.replace("?", "")
    a = a.replace("!", "")
    a = a.replace(":", "")
    a = a.replace("ç", "c")
    i = a[::-1]
    t = 0
    while t < len(a)-1:
        if a[t] != i[t] :
            t = t+1
            print('False')
            break
    return True

#### Fonction principale ###

def main():
    """La fonction contient la liste des mots à tester"""

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
