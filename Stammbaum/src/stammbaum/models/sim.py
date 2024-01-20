from statuses import SimStatus

class Sim:
    def __init__(self, name : str, gender : str, status=SimStatus.ALIVE):
        self.name = name
        self.gender = gender
        self.status = status
    

