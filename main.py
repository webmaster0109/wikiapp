import wikipediaapi as wp
import streamlit as stl

# Create a Wikipedia API object
user_agent = 'MyWikipediaBot/1.0 (determinedvillani@freethecookies.com)'
wiki_wiki = wp.Wikipedia('en', headers={'User-Agent': user_agent})  # 'en' for English Wikipedia
# wiki_wiki.session.headers.update()

stl.title("WikiApp Search")
search_input = stl.text_input("Search anything you want to know...")

if search_input:
    # Search for the given query
    page_py = wiki_wiki.page(search_input)

    if page_py.exists():
        # Print the title and summary of the Wikipedia page
        stl.write("Title:", page_py.title)
        stl.write("Summary:", page_py.summary)
        print("Title:", page_py.title)
        print("Summary:", page_py.summary)
    else:
        print("Page not found.")
    