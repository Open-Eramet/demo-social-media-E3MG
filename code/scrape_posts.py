import json
import warnings
from pathlib import Path

import facebook_scraper as fs
from configs import *
from tqdm import tqdm

warnings.simplefilter("ignore")


def scrape(output_filepath: Path, pages=DEFAULT_PAGES):
    """
    Effectue un web "scraping" sur une liste de pages Facebook
    """
    results = {}
    cookies_path = PROJECT_PATH / "assets" / "cookies.json"
    for page in tqdm(pages):
        results[page] = []
        try:
            for post in tqdm(fs.get_posts(page, pages=100, cookies=str(cookies_path))):
                results[page].append(post["text"])
        except KeyboardInterrupt as e:
            print(e)
            print(f"Stopping scrapping for {page}!")
        finally:
            print("# of scraped posts", len(results[page]))
    output_filepath.write_text(json.dumps(results))


if __name__ == "__main__":
    scrape(output_filepath=RAW_FILEPATH)
