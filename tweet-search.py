from twitter import *
from pprint import pprint
import os
import json
import sys
from fabric.colors import *
import textwrap

COUNT = 20
STOP_NUM = 3


def tweet_search(query):
    """Query search on twitter

    Parameters
    ----------
    query : str
        Search query.

    Return
    ------
    str
    """

    token = os.environ["ACCESS_TOKEN"]
    token_secret = os.environ["ACCESS_TOKEN_SECRET"]
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]

    t = Twitter(
        auth=OAuth(token, token_secret, consumer_key, consumer_secret))

    return t.search.tweets(q=query, count=COUNT)


def show(result):
    """Print result.

    Parameters
    ----------
    result : str
    """
    for i, v in enumerate(result["statuses"]):
        i += 1

        print(red(i), end='')
        print(" : " + green("@") + green(v["user"]["screen_name"]))
        print("    " + cyan("favorite : ") + str(v["favorite_count"]), end='')
        print(" " + cyan("retweet : ") + str(v["retweet_count"]))
        print("")

        dedented_text = textwrap.dedent(v["text"])
        print(textwrap.fill(dedented_text,
                            initial_indent='    ', subsequent_indent='    '))

        # print(v["text"])
        print("")

        if i % STOP_NUM == 0:
            input_res = input("Enter to next : ")

            if input_res == 'q':
                sys.exit()


if __name__ == '__main__':

    # Check args.
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

    result = tweet_search(query)
    show(result)
