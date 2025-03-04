from requests import get
from urllib.parse import urlparse

def find():
    url = str(input("Enter a URL (eg. https://app.instaffo.com): "))
    parsed_url = urlparse(url)
    parsed_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    sitemaps = [
        f"{url}/sitemap.xml",
        f"{url}/sitemap.yml",
        f"{url}/sitemap.yaml",
        f"{url}/sitemap.json",
        f"{url}/sitemapindex.xml",
        f"{url}/sitemap_index.xml",
        f"{url}/sitemap1.xml",
        f"{url}/sitemap1.yml",
        f"{url}/sitemap1.yaml",
        f"{url}/sitemap1.json",
        f"{url}/sitemapindex1.xml",
        f"{url}/sitemap1_index.xml",
        f"{url}/robots.txt"
    ]
    
    found_sitemap = False  
    
    for sitemap in sitemaps:
        try:
            response = get(sitemap, timeout=10)

            if response.status_code == 200:
                if sitemap == sitemaps[-1]:
                    robots_text = response.text.split(" ")
                    for i in robots_text:
                        if "sitemap" in i:
                            print(f"Sitemap found in robots.txt: {i}")
                            found_sitemap = True  
                            return True, i
                else:
                    print(f"Sitemap found at: {sitemap}")
                    found_sitemap = True 
                    return True, sitemap
                
        except Exception as e:
            print(f"Error: {e}")

    if not found_sitemap:
        print("No sitemap found.")



