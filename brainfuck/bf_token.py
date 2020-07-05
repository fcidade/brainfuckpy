class Token:
    def __init__(self, type_: str):
        self.type = type_

    def __str__(self):
        #return '%d:%s' % (0, self.type)
        return str(self.type)