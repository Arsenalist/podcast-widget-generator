import argparse
import requests

def main():
    p = argparse.ArgumentParser(description='Create a JSON feed based on an XML feed')
    p.add_argument('-x', '--xml-feed', required=True)
    p.add_argument('-o', '--output', required=True)
    args = vars(p.parse_args())
    feed = args['xml_feed']
    output = args['output']


    url = 'https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fassets.raptorsrepublic.com%2Frapcast-podcast.xml'
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        print ("Could not complete request " + url)
        print (e)
    output_file = open(output, 'w')
    output_file.write(r.text)
    output_file.close()

if __name__ == '__main__':
    main()

