from os import listdir
from job_searcher import search
from sitemap_finder import find
from sitemap_downloader import download

if __name__ == "__main__":
    while True:
        check = input("Choose an option:\n1. Search for sitemap\n2. Look for job (Requires downloaded Sitemap)\nEnter 1 or 2: ").strip()

        if check == "2":
            files_in_directory = listdir()  
            sitemap_files = [f for f in files_in_directory if "sitemap." in f]

            if sitemap_files:
                print(f"Found sitemap file(s): {', '.join(sitemap_files)}")
                search()  
                break  
            else:
                print("No sitemap found. Proceeding with sitemap search and download.")
                result = find()  
                if download(result[1]):  
                    search() 
                break  

        elif check == "1":
            print("Proceeding with sitemap search and download.")
            result = find()  
            if download(result[1]):  
                search()  
            break  

        else:
            print("Invalid input. Please enter '1' or '2'.")
