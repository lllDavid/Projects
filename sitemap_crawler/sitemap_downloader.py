from requests import get

def download(url):
    try:
        response = get(url)

        if response.status_code == 200:
            with open("sitemap.xml", 'wb') as file:
                file.write(response.content)
            print(f"Sitemap downloaded successfully and saved.")
            return True
        else:
            print(f"Failed to retrieve the sitemap. HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")


