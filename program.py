from jinja2 import Environment, FileSystemLoader, Template
from wsgiref.simple_server import make_server

jenv = Environment(loader=FileSystemLoader('.'))

def app(env, start_resp):
  start_response   = '200 OK'
  response_headers = [('Content-type', 'text/html')]
    path = env['PATH_INFO']
    
    def template(link):
        return jenv.get_template(path).render(link=link)
    if 'index.html' in path:
        link = '<a href="https://github.com/Ovchinnickova2016/myproject/new/master/about/aboutme.html">aboutme</a>'
    if 'about/aboutme.html' in path:
        link = '<a href="https://github.com/Ovchinnickova2016/myproject/new/master/index.html">index</a>'
        
    return [template(link).encode('utf-8')]
    
app = start_wsgi()
serv = make_server(app, host='localhost', port=8000)
serv.serve_forever()
