from requests import get

def find():
    url = str(input("Enter a URL (eg. https://app.instaffo.com): "))

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
        
    for sitemap in sitemaps:
        try:
            response = get(sitemap, timeout=10)

            if response.status_code == 200:
                if sitemap == sitemaps[-1]: 
                    robots_lines = response.text.splitlines()
                    for line in robots_lines:
                        if "sitemap" in line.lower():
                            parts = line.split(":")
                            if len(parts) > 1:
                                sitemap_url = parts[1].strip()
                                print(f"Sitemap found in robots.txt: {sitemap_url}")
                                return sitemap_url
                else:
                    print(f"Sitemap found at: {sitemap}")
                    return sitemap

        except Exception as e:
            print(f"Error: {e}")

    print("No sitemap found.")