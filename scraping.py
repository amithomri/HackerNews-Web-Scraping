import requests
from bs4 import BeautifulSoup
import pprint
response = requests.get("https://news.ycombinator.com/")
response2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(response.text, "html.parser")
soup2 = BeautifulSoup(response2.text, "html.parser")
subtext = soup.select(".subtext")
links_titles = soup.select(".titleline > a")
subtext2 = soup2.select(".subtext")
links_titles2 = soup2.select(".titleline > a")
total_links_titles = links_titles2+links_titles
total_subtext = subtext + subtext2


def sort_article_by_points(news_list):
    return sorted(news_list, key=lambda k: k["votes"], reverse=True)#the key is expressed with lambda and it means sort by the votes


def create_popular_hackernews(links, my_subtext):
    """

    :param links: links of hackernews articles
    :param my_subtext: subtext of hackernews articles
    :return: a sorted list of hackernews articles
    """
    top_hackernews = []
    for index in range(len(links)):
        title = links[index].getText()
        href = links[index].get('href', None)
        points = my_subtext[index].select(".score")
        if points:
            points = (int(points[0].getText().split(' ')[0]))#strip the points out of the string
            if points > 99:
                top_article = {"title": title, "link": href, "votes": points}
                top_hackernews.append(top_article)
    return sort_article_by_points(top_hackernews)


pprint.pprint(create_popular_hackernews(total_links_titles, total_subtext))#pprint is a nice way to view the list

