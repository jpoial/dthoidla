#!/usr/bin/env python3


class Loom(object):
    """
    Looma omadusi kirjeldav klass
    """
    __nimi = ''  # private
    
    def vota_nimi(self):
        return self.__nimi
    
    def pane_nimi(self, nimi):
        self.__nimi = nimi
    
    def __init__(self, nimi):
        self.pane_nimi(nimi)
        
    @classmethod
    def luua_nimeta(cls):
        return cls('nimetu')

    @classmethod
    def luua(cls, nimi):
        return cls(nimi)
        
    def __del__(self):
        print('Vabastati ' + self.vota_nimi())
        
    def __str__(self):
        return 'Olen loom ' + self.vota_nimi()


class Kass(Loom):
    """
    Kassi omadusi kirjeldav klass.
    """
    vurrupikkus = 0
    
    def __str__(self):
        return super().__str__() + ' ja sealjuures KASS'


class Koer(Loom):
    """
    Koera omadusi kirjeldav klass.
    """
    sabaga = True
    

def main():
    """
    Main method.
    """
    minu_kass = Kass.luua('Kiti')
    minu_koer = Koer.luua_nimeta()
    minu_loom = Loom.luua_nimeta()
    minu_loom.pane_nimi('Patu')
    print(minu_kass)
    print(minu_koer)
    print(minu_loom)
    minu_loom = minu_koer
    print(minu_loom)
    minu_loom = minu_kass
    print(minu_loom)
    minu_kass = minu_loom
    print(minu_kass)


if __name__ == '__main__':
    main()
