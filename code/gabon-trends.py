import json

import matplotlib.pyplot as plt
import streamlit as st
from configs import *
from visualize import create_wordcloud_fig
from process_data import *
from scrape_posts import *

if not RAW_FILEPATH.exists():
    scrape(output_filepath=PROCESSED_FILEPATH, pages=DEFAULT_PAGES)


st.title("Gabon Trends ")

with st.sidebar:
    st.write("# Gabon Trends ")
    col_2, col_1 = st.columns(2)
    file_path = PROJECT_PATH / "assets" / "drapeau-gabon.jpg"
    col_1.image(file_path.__str__(), width=100)
    file_path = PROJECT_PATH / "assets" / "logo-facebook.png"
    col_2.image(file_path.__str__(), width=100)

    with st.expander("Affiner le choix"):

        with st.form("pages"):
            pages = st.multiselect(
                "Selectionner les pages FB",
                options=DEFAULT_PAGES,
                default=DEFAULT_PAGES,
            )
            st.form_submit_button("Afficher")

if len(pages) > 0:
    save_processed_posts(PROCESSED_FILEPATH, pages)
    fig = create_wordcloud_fig()
    st.write(fig)

    with st.expander("Afficher les détails"):

        with open(RAW_FILEPATH, "rt") as file:
            posts = json.loads(file.read())
        post_sources = {s: len(posts[s]) for s in posts}
        cols = st.columns(5)
        cols[2].metric("# Posts", sum(post_sources.values()))
        fig = plt.figure()
        plt.barh(y=list(post_sources.keys()), width=post_sources.values())
        plt.title("Répartition des posts")
        plt.xlabel("Source")
        plt.ylabel("# Posts")
        st.pyplot(fig)
else:
    st.error("Selectinner au moins une page SVP !")
