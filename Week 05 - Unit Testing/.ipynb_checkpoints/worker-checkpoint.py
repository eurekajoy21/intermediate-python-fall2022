
class NormalIncrease:
    raise_amt = 1.20

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


dorj = NormalIncrease("Dorj","Misha", 800000)
myagmar = NormalIncrease("Myagmar","Bold", 760000)

