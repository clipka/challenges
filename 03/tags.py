from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    list_of_tags = []
    file = open(RSS_FEED,'r')
    text = file.read().lower().replace('\n', '')

    pattern = "<category>([^<]+)</category>"
    for match in re.findall(pattern, text):
        match = match.replace('-', ' ')
        list_of_tags.append(match)

    file.close()

    return list_of_tags


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""

    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    similar_pairs = []
    pairs = list(product(tags, tags))

    for item in pairs:
        sorted_item = sorted(item, key=len)
        seq = SequenceMatcher(None, sorted_item[0], sorted_item[1])
        if SIMILAR <= seq.ratio() < 1:
            if sorted_item not in similar_pairs:
                similar_pairs.append(sorted_item)

    return similar_pairs


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
