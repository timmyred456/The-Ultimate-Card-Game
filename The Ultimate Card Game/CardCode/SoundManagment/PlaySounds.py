import simpleaudio as sa
import threading

class SoundObject():
    def __init__(self,FileLocation):
        self.FileLocation = FileLocation
        self.wave_obj = sa.WaveObject.from_wave_file(FileLocation)
        self.soundObject = None
        self.IsLooping = False

    def LoopThread(self):
        while self.IsLooping == True:
            if(self.soundObject.is_playing() == False):
                self.soundObject = self.wave_obj.play()

    def PlaySound(self,Loop=True):
        self.IsLooping = Loop
        self.soundObject = self.wave_obj.play()
        if(self.IsLooping == True):
            x = threading.Thread(target=self.LoopThread)
            x.start()

    def StopSound(self):
        if(self.soundObject != None):
            self.soundObject.stop()
            self.IsLooping = False
