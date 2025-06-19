from re import findall

def search():
    jobtitle = input("Enter jobtitle (eg. developer): ")
    date = input("Enter date for jobs newer than (YYYY-MM-DD): ")

    with open('sitemap.xml', 'r') as file:
        content = file.read()
        loc_tags = findall(r'<loc>(.*?)</loc>', content)
        lastmod_tags = findall(r'<lastmod>(.*?)</lastmod>', content)

        matching_jobs = []
        for loc, lastmod in zip(loc_tags, lastmod_tags):
            if jobtitle in loc and lastmod > date:
                job_desc = loc.split('/job/')[-1].rsplit('-', 1)[0]  
                matching_jobs.append((lastmod, job_desc, loc))

        matching_jobs.sort()

        for lastmod, job_desc, loc in matching_jobs:
            print(f"{lastmod} - {job_desc} - {loc}")