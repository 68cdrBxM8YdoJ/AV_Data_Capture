from xml.etree.cElementTree import Element, SubElement, tostring
from bs4 import BeautifulSoup
import custom_html_parser


def generate(data: dict) -> Element:
    root = Element("movie")

    s_title = SubElement(root, "title")
    s_title.text = data["title"]

    s_set = SubElement(root, "set")
    s_set.text = ""

    s_year = SubElement(root, "year")
    s_year.text = "YEAR"

    s_outline = SubElement(root, "outline")
    s_outline.text = "OUTLINE"

    s_plot = SubElement(root, "plot")
    s_plot.text = "PLOT"

    s_runtime = SubElement(root, "runtime")
    s_runtime.text = "RUNTIME"

    s_director = SubElement(root, "director")
    s_director.text = "DIRECTOR"

    s_poster = SubElement(root, "poster")
    s_poster.text = "POSTER"

    s_thumb = SubElement(root, "thumb")
    s_thumb.text = "THUMB"

    s_fanart = SubElement(root, "fanart")
    s_fanart.text = "FANART"

    s_actor = SubElement(root, "actor")
    for name in ["a", "b", "c"]:
        ss_name = SubElement(s_actor, "name")
        ss_name.text = name

    s_maker = SubElement(root, "maker")
    s_maker.text = "MAKER"

    s_label = SubElement(root, "label")
    s_label.text = "LABEL"

    for tag in ["A", "B", "C"]:
        s_tag = SubElement(root, "tag")
        s_tag.text = tag

    for genre in ["A", "B", "C"]:
        s_genre = SubElement(root, "genre")
        s_genre.text = genre

    s_num = SubElement(root, "num")
    s_num.text = "NUM"

    s_premiered = SubElement(root, "premiered")
    s_premiered.text = "PRE"

    s_cover = SubElement(root, "cover")
    s_cover.text = "COVER"

    s_website = SubElement(root, "website")
    s_website.text = "WEB"

    return root


def prettify(el: Element) -> str:
    soup = BeautifulSoup(tostring(el), "xml")
    parser = custom_html_parser.CustomHTMLParser()
    parser.feed(str(soup))

    return parser.get_parsed_string()


def write(xml: str, filename: str):
    with open("output1.xml", "w") as file:
        file.write(xml)


if __name__ == "__main__":
    nfo = generate()
    print(prettify(nfo))
