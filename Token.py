from ipaddress import ip_address as ip

class Token:
    # state shared by each instance
    __shared_state = dict()

    # constructor method
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.IP_source = None
        self.IP_target = None
        self.sent_message = None
        self.finish_line = bool()
        self.is_free = True
        self.history = []

    def __str__(self):
        return "Token({0},{1},{2},{3},{4},{5})".format\
        (
                self.IP_source,
                self.IP_target,
                self.sent_message,
                'DA' if self.finish_line == True else "NU",
                'DA' if self.is_free == True else "NU",
                self.history
        )

    def free(self):
        self.__init__()