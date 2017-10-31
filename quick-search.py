from google import search
import requests
import urllib.request
import bs4
from readability.readability import Document
import html2text
import os
import sys
import traceback
from pprint import pprint
import re
import pydoc
from fabric.colors import green
from fabric.colors import red
from fabric.colors import cyan
import yaml


SEARCH_ENGINE_ID = os.environ["SEARCH_ENGINE_ID"]
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]


def search(query, start=1, num=10):
    """Get title, link list.

    Execute google search api format results to specified number of list.

    Ex: 
    search("Hello")

    Parameter
    ---------
    query : str
        Search query.

    start : int
        Number of page to start.

    num : int
        Number of resutls to get.

    Return
    ------
    list : 
        Title and link list.

    """

    title_links = []
    for start_num in range(3):
        start_num += 1
        api_path = "https://www.googleapis.com/customsearch/v1"
        params = {
            "cx": SEARCH_ENGINE_ID,
            "key": GOOGLE_API_KEY,
            "q": query,
            "start": start_num,
            "num": 10
        }

        try:
            result_json = requests.get(api_path, params).json()
            items_json = result_json["items"]

            for v in items_json:
                title_link = [v["title"], v["link"]]
                title_links.append(title_link)

        except:
            pprint(result_json)
            traceback.print_exc()

    return title_links[:num]


def contents_scraping(link, remove_space=True, remove_lb=True):
    """Scraping contents.

    Parameter
    ---------
    url : str
      Scraping target url.

    Return
    ------
    list : 
        title and contents.
    """

    try:
        html = urllib.request.urlopen(link).read()
    except:
        print("ERROR : failed to get contents.")
        return (False, "")

    title = Document(html).short_title()
    contents = Document(html).summary()
    contents = html2text.html2text(contents)

    p = re.compile(r"<[^>]*?>")
    c = p.sub("", contents)

    if remove_space is True:
        c = c.replace(" ", "")

    if remove_lb is True:
        c = c.replace("\r", "")
        c = c.replace("\n", "")

    return title, c


def open_browser(browser, link):
    """Open link on browser.
    Available Google Chrome or Firefox.

    Parameters
    ----------
    browser : str
      Browser application.
      Ex) Firefox.app

    link : str
      Open link.
    """
    com = 'open -a "/Applications/{0}" {1}'.format(browser, link)
    res_open = os.system(com)
    if res_open != 0:
        sys.stderr.write(
            red("ERROR : {0} Not Found\n".format(browser)))

    input_browse = input("Enter to next or 'q' is Quit : ")
    if input_browse == 'q':
        sys.exit()


if __name__ == '__main__':

    # Check args.
    args = sys.argv
    if len(args) == 1:
        print("Arg is not defined")
        sys.exit()

    # Load params.yaml.
    dir_path = os.path.abspath(os.path.dirname(__file__))
    param_path = dir_path + "/params.yaml"

    with open(param_path, mode="r") as f:
        yaml_data = yaml.load(f)

    RESULT_NUM = yaml_data["result_num"]
    STOP_NUM = yaml_data["stop_num"]
    SUMMARY_NUM = yaml_data["summary_num"]

    # Set query string.
    query = ""
    for q in sys.argv[1:]:
        if len(query) == 0:
            query += q
        else:
            query += " " + q

    # Execute google search.
    title_links = search(query, num=RESULT_NUM)

    for i, title_link in enumerate(title_links):

        # Print stdout.
        i += 1
        print(red(str(i)) + " ", end='')
        print(green(title_link[0]))
        print("  " + cyan(title_link[1]))

        title, contents = contents_scraping(title_link[1])
        if title is False:
            next

        for q in sys.argv[1:]:
            contents = contents.replace(q, green(q))

        print(contents[:SUMMARY_NUM])
        print("")

        # Temporaly stop.
        if i % STOP_NUM == 0:
            page_num = input("Enter or input number of page : ")

            # Browser (MacOS only)
            if page_num[-1] == 'c':
                open_browser('Google Chrome.app', title_link[1])

            elif page_num[-1] == 'b':
                open_browser('Firefox.app', title_link[1])

            # Show in terminal.
            elif page_num.isdigit() is True:
                link = title_links[int(page_num)][1]
                title, contents = contents_scraping(link, False, False)
                if title is False:
                    print("ERROR : failed to scrape contents.")
                    next

                pydoc.pager(contents)

                input_after_contents = input("Enter to next or 'q' is Quit : ")

                if input_after_contents == 'q':
                    sys.exit()

            # Quit.
            elif page_num == "q":
                sys.exit()
