import json
import re

import nltk
from configs import *
from nltk.corpus import stopwords


def process_post(post: str) -> str:
    """
    Traite le texte d'un post facebook
    """

    # Supprimer tous les espaces
    processed_post = re.sub(pattern="\s", repl=" ", string=post)
    # Supprimer tous les caractères non alaphabétiques
    processed_post = re.sub(pattern="\W", repl=" ", string=processed_post)
    # supprime tous les numéros
    processed_post = re.sub(pattern="[0-9]+", repl=" ", string=processed_post)

    # Transformer en miniscule et séparer en mots
    tokens = processed_post.lower().split()
    # Supprimer tous les mots fréquents
    stops = stopwords.words("french")
    tokens = [token for token in tokens if not token in stops]
    processed_post = " ".join(tokens)

    return processed_post


def save_processed_posts(processed_filepath, pages=DEFAULT_PAGES):
    """
    Sauvegarde les posts traités dans un fichier texte
    """
    nltk.download("stopwords")
    with open(RAW_FILEPATH, "rt") as file:
        posts = json.loads(file.read())

    corpus = ""
    for page in pages:
        for p in posts[page]:
            corpus = corpus + process_post(p)

    processed_filepath.write_text(data=corpus)


if __name__ == "__main__":

    save_processed_posts(processed_filepath=PROCESSED_FILEPATH)
