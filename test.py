class basic():
    def __init__(self):
        self.stf = "This is stuff"
class advanced(basic):
    def __init__(self):
        basic.__init__(self)
        print (self.stf)
ruby = advanced()


