from pprint import pprint
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
import colorama
from colorama import Fore, Back, Style
import pydoc
from fabric.colors import green

colorama.init(autoreset=True)


class GoogleSearch():

    def __init__(self, num=5, loop_num=3, tmp_stop=5):
        self.num = num
        self.loop_num = loop_num
        self.tmp_stop = tmp_stop
        self.GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

    def search(self, query, start=1, num=10):
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
                "cx": "001155821352449308988:0skw1nrswlm",
                "key": self.GOOGLE_API_KEY,
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

    def contents_scraping(self, link, remove_space=True, remove_lb=True):
        """
        Scraping contents.

        Parameter
        ---------
        url : str
          Scraping target url.

        Return
        ------
        list : 
            title and contents.
        """

        html = urllib.request.urlopen(link).read()

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

    def search_images(self, word, num=10):
        """
        Get Images from google search.

        Ex: 
          search_images("cat", 5)

        Parameter
        ---------
        word : str
          Search word.

        num : int
          Number of images to get.

        Return
        ------
        list : list
          Image urls.

        ["https://example.jpg", "https://example2.png"]
        """

        api_path = "https://www.googleapis.com/customsearch/v1"
        params = {
            "cx": "001155821352449308988:0skw1nrswlm",
            "key": "AIzaSyDXu5ftNYEHOiq8wwUnSBbB4lnshkn1Syw",
            "q": word,
            "searchType": "image",
            "start": 1,
            "num": 10
        }

        try:
            result_json = requests.get(api_path, params).json()
            items_json = result_json["items"]
        except:
            pprint(result_json)

        image_links = []
        for i, v in enumerate(items_json):
            if i < num:
                image_links.append(v["link"])

        return image_links


if __name__ == '__main__':

    # Get args.
    args = sys.argv

    if len(args) == 1:
        print("Arg is not defined")
        sys.exit()

    # Set query string.
    query = ""
    for q in sys.argv[1:]:
        if len(query) == 0:
            query += q
        else:
            query += " " + q

    # Execute google search.
    gs = GoogleSearch(20)
    title_links = gs.search(query, num=20)

    for i, title_link in enumerate(title_links):

        # Print stdout.
        i += 1
        pprint("Query : " + query)
        print(Fore.RED + str(i) + " ", end='')
        print(Fore.GREEN + title_link[0])
        print("  " + Fore.CYAN + title_link[1])

        try:
            title, contents = gs.contents_scraping(title_link[1])
        except:
            print("Contents scraping error : " + title_link[1])
            next

        # print(contents[:500])
        for q in sys.argv[1:]:
            contents = contents.replace(q, green(q))

        print(contents[:500])
        print("")

        # Temporaly stop.
        if i % 5 == 0:
            page_num = input("Enter number of page : ")

            # Specify index.
            if page_num.isdigit() is True:
                link = title_links[int(page_num)][1]
                title, contents = gs.contents_scraping(link, False, False)
                for q in sys.argv[1:]:
                    contents = contents.replace(q, green(q))

                pydoc.pager(contents)

                input_after_contents = input("Enter to next or 'q' is Quit : ")

                if input_after_contents == 'q':
                    sys.exit()

            # Quit.
            elif page_num == "q":
                sys.exit()
