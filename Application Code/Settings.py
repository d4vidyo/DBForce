
class settings():
    def __init__(self):
        self.Name = "DBForce"

    def load(self):
        self.host = "host"
        self.DB = "db"
        self.user= "user"
        self.pw="pw"
        self.Schema = "'FireForce'"
        self.fps = 144
        self.frametime = 1/self.fps