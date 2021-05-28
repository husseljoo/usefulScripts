#Search in YOutube from the terminal
from sys import argv
import webbrowser


def handle():
    url='https://www.youtube.com/results?search_query='
    str=""
    for x in argv[1:]:
        str+=x+'+'
    str= str[:len(str)-1]
    url+=str
    return url

if __name__=='__main__':
    if len(argv)==1:
        webbrowser.get("firefox").open('https://www.youtube.com/')
    else:
        url=handle()
        webbrowser.get("firefox").open(url)
