from job_searcher import search
from sitemap_finder import find
from sitemap_downloader import download

if __name__ == "__main__":
    result = find()
    if download(result[1]):
        search()