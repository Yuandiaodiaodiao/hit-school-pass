import tornado.web
import tornado.ioloop
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
    application.listen(10277)
    tornado.ioloop.IOLoop.current().start()