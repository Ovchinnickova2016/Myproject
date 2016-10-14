#подключаем пакет дополнение
from wsgiref.simple_server import make_server

#функция ответа сервера 
def app(environ, start_response):
    status = '200 OK' # статус 
    response_headers = [('Content-type', 'text/html')]  #заголовки
    start_response(status, response_headers) # создание ответа, со ссылкой на index.html
    path = environ['PATH_INFO'] 
    if path == '':
        path = 'index.html'
    file = open(path, 'r')  #открытие файла на чтение
    return [file.read()]

#класс Middleware
class Middleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        answer = self.app(environ, start_response)[0]
        # Если в html странице есть теги body, то
        if (answer.find('<body>') > 0 and answer.find('</body>') > 0): 
            #строка разбивается на части: сначала берется то, что до и после открывающего тега, затем то, что после тега снова делится, 
            a1, a2 = answer.split('<body>')
            # Далее, строка собирается заново, но в тело встраиваются новые строки.
            answer = a1 + '<body>\n' "\t\t<div class='top'>Middleware TOP</div>" + a2
            a1, a2 = answer.split('</body>')
            answer = a1 + "\t<div class='bottom'>Middleware BOTTOM</div>\n" + '\t</body>' + a2          
        return answer

#запуск сервера
myserver = make_server('localhost', 8000, Middleware(app))
myserver.serve_forever()
