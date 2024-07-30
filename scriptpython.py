import subprocess
class Scriptpython:
    def __init__(self,name,userid):
        self.name=name
        self.userid=userid
    def lancer(self):
        x=subprocess.check_output(["sh","./lancer_"+self.name+".sh",self.userid])
        return x

