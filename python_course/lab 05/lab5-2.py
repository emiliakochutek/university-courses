import requests
import sys

# url = 'https://python.org'
# r = requests.get(url)

# >>> r
# <Response [200]> 200 -> status code
# >>> r.content[:1000]


def get_page(url):
    ## Uzupelnienie protokolu w razie braku
    if not (url.startswith('https://') or url.startswith('http://')):
        url = 'https://' + url
        
    r = requests.get(url)
    return r

if __name__ == '__main__':
    for url in sys.argv[1:]:
        r = get_page(url)
        
        if r.status_code != 200:
            print(f'{url:.<20}{r.reason}')
            continue
        
        size = len(r.content) // 1000 ## rozmiar w kB
        print(f'{url:.<20}{size}kB')