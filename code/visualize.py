import matplotlib.pyplot as plt
from configs import *
from wordcloud import WordCloud


def create_wordcloud_fig():

    # Read the whole text.
    text = PROCESSED_FILEPATH.read_text()
    if len(text) == 0:
        return None
    # Generate a word cloud image
    wordcloud = WordCloud(
        max_font_size=40, background_color="white", random_state=0
    ).generate(text)
    fig = plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")

    return fig
