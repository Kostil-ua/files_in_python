with open("quotes.txt", "r", encoding = "utf-8") as fille:
    for line in fille:
        print(line)

author = input("Введи автора вірша")

with open("quotes.txt", "a", encoding = "utf-8") as fille:
    fille.write("("+ str(author)+")\n")

while True:
    author = input("Введіть автора")
    if author == "ні":
        break
    quote = input("Введіть цитату:")

    with open("quotes.txt", "a", encoding = "utf-8") as fille:
       fille.write(str(author)+":"+ str(quote)+"\n")