import requests
from bs4 import BeautifulSoup


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def menu():
    x = """
    Author : RadenGozal
    
    Available Domain : {
    SE,ORG,NET,INFO,IN,DE,COM,WWW,KZ,CA,AU,PL,BE,IT,IP,CH,ES,TECH,AT,FR,TR,JP,UA,UK,
    }
    """
    print(x)
    new_list()


def new_list():
    domain = input("Choose Your Domain ? : ")
    jml = input("How Many Page ? : ")
    mullah = int(jml)
    hit_page = 0
    for page in range(1, mullah):
        hit_page += 1
        print("> Grabbing Page : ", domain, page)
        url = 'https://{}.all-url.info/{}/0/'.format(domain, page)

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 '
                          'Safari/537.36 '
        }
        req = requests.get(url, headers=header)
        sop = BeautifulSoup(req.text, 'html.parser')

        item = sop.find('div', {'align': 'center'})
        link = item.find_all('font', {'style': 'line-height:2;'})
        for li in link:
            uri = li.find('a').text
            text = open("result-by-date.txt", "a")
            text.write(uri + '\n')
            text.close
        print("Done Grabbing page \n")
    file = open("result-by-date.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    print('You Got ' + str(line_count) + ' domain in your list :D ')


def abjad():
    pass


def grab_url(url):
    print(url)


if __name__ == '__main__':
    menu()
