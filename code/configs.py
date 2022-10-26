from pathlib import Path

## Changer par votre chemin d'accès
PROJECT_PATH = Path("...")
RAW_FILEPATH = PROJECT_PATH / "data" / "raw" / "posts.json"
PROCESSED_FILEPATH = PROJECT_PATH / "data" / "processed" / "posts.txt"

# TOP Gabon facebook pages
# "https://www.gabonreview.com/tribune-facebook-le-top-10-des-pages-gabonaises-en-mai-2020/"
DEFAULT_PAGES = [
    "GabonCelebritesCom",
    "231189310723035",
    "493097327851191",
    "Covid19GOUVGA",
    "tvgabon24",
]
