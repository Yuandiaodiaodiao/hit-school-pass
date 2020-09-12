import tornado.web
import tornado.ioloop
import tornado.httpserver
import os
path=os.path.join("dist",'static')
htmlpath=os.path.join("dist",'index.html')
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(htmlpath)


if __name__ == "__main__":
    setting = dict(
        static_path=path,
    )
    application = tornado.web.Application([
        (r"/", MainHandler),
    ],**setting)
    http_server=tornado.httpserver.HTTPServer(application,xheaders=True)
    http_server.bind(int(10277),"0.0.0.0")
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()