class Token:
    """
        Wraps code slices as objects
    """
    def __init__(self, type_: str):
        self.type = type_

    def __str__(self):
        return str(self.type)