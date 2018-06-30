from B import B
from C import C

class A:
    def setId(this,id):
        this.id=id

    def getId(this):
        return this.id

    def setName(this,name):
        this.name=name

    def getName(this):
        return this.name

    def getB(this):
        return this.b

    def setB(this,b):
        this.b=b

    def setC(this,c):
        this.c=c

    def getC(this):
        return C

    def __init__(this):
        return

    def __init__(this,id,name,price):
        this.id=id
        this.name
        this.price
        this.b=B()
        this.c=[]

    def  __repr__(this):
        return f"{this.name}"

class D(A):
    def __init__(this):
        return
    def __init__(this,id,name,price):
        super()(id,name,price)
