from re import findall

def search():
    jobtitle = str(input("Enter jobtitle (eg. developer): "))
    date = str(input("Enter date for jobs newer than: "))

    with open('sitemap.xml', 'r') as file:
        content = file.read()

        loc_tags = findall(r'<loc>(.*?)</loc>', content)
        lastmod_tags = findall(r'<lastmod>(.*?)</lastmod>', content)

        for loc, lastmod in zip(loc_tags, lastmod_tags):
            if jobtitle in loc and lastmod > date:
                print(loc)
                

