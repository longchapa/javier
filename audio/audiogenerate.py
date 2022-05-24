import wave
from datetime import datetime
import json
import base64


class AudioGenerate:

    def __init__(self):
        self.audio_wav = None
        self.has_seen_media = None
        self.name = self.__get_audio_filename()

    def create_audio(self):
        self.audio_wav = wave.open(self.name, "wb")
        self.audio_wav.setsampwidth(2)
        self.audio_wav.setnchannels(1)
        self.audio_wav.setframerate(8000)

    def __get_audio_filename(self):
        return datetime.now().strftime("audio/%Y-%m-%d_%H-%M-%S_%f.wav")

    def write_audio(self, data):
        data = json.loads(data)
        try:
            if data['event'] == 'media':
                if not self.has_seen_media:
                    payload = data['media']['payload']
                    chunk = base64.b64decode(payload)
                    self.audio_wav.writeframesraw(chunk)
                elif data['event'] == 'stop':
                    self.audio_wav.close()
                    self.has_seen_media = True
                    self.write_message("Audio creado")
                    print("Algo salio mal")
        except Exception as e:
            self.write_message("Algo salio mal")
            print("Algo salio mal")
            pass
