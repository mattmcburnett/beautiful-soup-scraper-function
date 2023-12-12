from bs4 import BeautifulSoup

with open('challenge.html', 'r') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

body_content = soup.body

def find_hidden_html(body):
    hidden_html = ''
    for code_div in body.find_all('code'):
        # print(code_div["data-class"])
        if code_div['data-class'].startswith('23', 0, 2):
            divs = code_div.find_all('div')
            # print(divs)
            for div in divs:
                if div['data-tag'].endswith('93'):
                    spans = div.find_all('span')
                    # print(spans)
                    for span in spans:
                        if '21' in span['data-id']:
                            eyes = span.find_all('i')
                            # print(eyes)
                            for i in eyes:
                                hidden_html = hidden_html + i['value']
    return hidden_html

print(find_hidden_html(body_content))
