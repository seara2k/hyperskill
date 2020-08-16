class Plant:

    def __init__(self, spec):
        self.spec = spec


class Cactus(Plant):
    pass

basil = Plant("Ocimum basilicum")

opuntia = Cactus("Opuntia vulgaris")

lst = [type(opuntia) == Cactus,

       type(basil) == Cactus,

       isinstance(opuntia, Plant),

       type(basil) == object,

       isinstance(basil, Plant),

       isinstance(opuntia, object),

       type(opuntia) == Plant]

print(lst)
