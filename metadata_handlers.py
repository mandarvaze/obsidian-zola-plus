"""
Any function in this file is treated as a metadata handler. The function name is the metadata key.
The function takes the value of the metadata key and returns the html to be inserted into the page.
You can use existing elements or create new ones, just make sure to also create css for them.
"""
from random import choice, seed


def modified(date: str) -> str:
    """Converts date into html format element"""
    return f"""
            <meta property="article:modified_time" content="{date}"/>
            """


def button(text):
    return f"""
            <button class="button">{text}</button>
            """


# [![Build Status](https://img.shields.io/website?url=https%3A%2F%2Fyarden-zamir.com)](https://yarden-zamir.com)
def chips(chips_dict: dict):
    chips_out = ""
    for key, value in chips_dict.items():
        front, link = "", ""
        if not value.startswith("http"):
            value = str(value).replace(" ", "--")
        if not key.startswith("http"):
            key = f"https://img.shields.io/badge/{_clean_url(key)}-{_clean_url(value)}-{_random_color(key)}"
        chips_out += f"""
        [![alt text]({key})]({value})
        """.strip() + "\n"
    return chips_out


def tags(tags_list: list) -> str:
    tags_out = ""
    for tag in tags_list:
        tags_out += f"https://img.shields.io/badge/{tag}-{_random_color(tag)}\n"
    return tags_out

def _clean_url(url: str) -> str:
    if "/" in url:
        return url.split("/")[-1].replace("-", "--").replace(" ", "--")
    else:
        return url.replace("-", "--").replace(" ", "--")


def _random_color(random_seed=0) -> str:
    seed(random_seed)
    return choice([
        "brightgreen",
        "green",
        "yellowgreen",
        "yellow",
        "orange",
        "red",
        "blue",
        "purple",
    ])