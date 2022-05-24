import tornado.ioloop
import tornado.web
from mainhandler import EchoWebSocket


def main():
    app = tornado.web.Application([
        (r"/", EchoWebSocket),
    ])
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    print("Starting app...")
    try:
        main()
    except KeyboardInterrupt:
        print("Stoping app...")
    finally:
        print("Application stoped")