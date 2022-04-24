from requests import post


__author__ = 'Чусовитин А.Р.'

data = {
    'url': 'https://www.google.com/'
}
print(post('http://37.139.42.4:8888/', data=data).text)
