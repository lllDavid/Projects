# Sitemap Crawler

**Currently only works with [instaffo.com](https://www.instaffo.com/en/talent).**

- **Workflow**:
1. Checks the provided URL for a sitemap.
2. Downloads the sitemap if found.
3. Filters sitemap URLs for job listings matching a specific title and published after a target date.
4. Outputs the filtered job posts.

## Usage 

### 1. Clone the Repository
```bash
git clone https://github.com/lllDavid/sitemap_crawler
```
### 2. Run the Application
```bash
cd sitemap_crawler
python main.py
```