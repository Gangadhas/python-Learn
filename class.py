class name:
    my_name='qwer'
    def __init__(self,fname,nname):
        self.fname=fname
        self.nname=nname
    def __str__(self):
        return f'my name is {self.my_name} my friend name is {self.fname}'
    def age(self,fage,nage):
        self.fage=self.fname
        self.nage = self.nname
        return f'my name is {self.fage} my friend name is {self.nage}'

nome=name('tamil','dgs')
print(nome)
A=nome.age('eng','fre')
print(A)
