STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=[]):
        self.geslo = geslo
        self.crke = crke

    def pravilne_crke(self):
        pravilne = []
        for crka in self.crke:
            if crka in self.geslo:
                pravilne.append(crka)
        return pravilne

    def napacne_crke(self):
        napacne =  []
        for crka in self.crke:
            if crka not in self.geslo:
                napacne.append(crka):
        return napacne

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True
    
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                niz += crka
            else:
                niz += '_'
        return niz

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        velika_crka = crka.upper(=)
        if velika_crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(velika_crka)
            if self.zmaga():
                return ZMAGA    
            elif self.poraz():
                return PORAZ
            else:
                if velika_crka in self.pravilne_crke():
                return PRAVILNA_CRKA
                elif velika_crka in self.napacne_crke():
                    return NAPACNA_CRKA