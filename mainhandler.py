import tornado.websocket
from tornado import httputil
from audio.audiogenerate import AudioGenerate


class EchoWebSocket(tornado.websocket.WebSocketHandler, AudioGenerate):

    def __init__(
            self,
            application: tornado.web.Application,
            request: httputil.HTTPServerRequest,
            **kwargs
    ):
        super().__init__(application, request, **kwargs)
        self.audio_wav = None
        self.has_seen_media = None

    def open(self):
        self.create_audio()
        print("WebSocket opened")

    def on_message(self, message):
        print(message)
        self.write_audio(message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, _origin):
        return True

