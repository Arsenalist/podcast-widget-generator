import argparse
from jinja2 import Template
import feedparser

def main():
    p = argparse.ArgumentParser(description='Create a HTML widget containing the last few podcasts')
    p.add_argument('-f', '--feed', required=True)
    args = vars(p.parse_args())
    feed = args['feed']

    d = feedparser.parse(feed)
    items = d.entries[:2]
    context = []
    for i in items:
        # some megaphone.fm customization
        context.append( {"title": i.title, "id": i.links[0].href.replace(".mp3", "?").replace("traffic", "player")} )

    info = {'items': context}
    with open('template.html', 'r') as content_file:
        content = content_file.read()
    template = Template(content)
    print(template.render(info))

if __name__ == '__main__':
    main()

