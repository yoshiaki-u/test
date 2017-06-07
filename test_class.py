#### class
class self:
    hoge = "class test"
    honto = "hono"

    class hoge:
        class xhoge:
            def __init__(self, string):
                self.init = string
            def usr(self, str):
                return str

    def test(self, str):
        return str + " desu"

class polling:
    def __init__(self):
        self.value1 = "polling"
        self.value2 = "polling test"
        self.value3 = self.plusone(5)

    def valu(self,sel):
        if (sel < 0):
            return self.value1
        else:
            return self.value2

    def plusone(self, x):
        return x+1

    def plustwo(self, x):
        return self.plusone(x)+1

    class device:
        self.value0 = "polling.device"
        def __init__(self, string):
            self.init = string
        def usr(self, str):
                return str


class sensor(polling):
    def hoge(self):
        print self.valu(0)

a = self.hoge.xhoge("test")

print a.usr("hogehoge")
b = self()
print b.test("hogehoge")
print self.honto

c = sensor()
c.hoge()
print
print c.value1
d = polling.device("test")

print d.usr("test string")
e = polling()
print e.plusone(6)
print e.plustwo(10)

#print d.value1
#print d.value2
