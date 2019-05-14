def izpis_igre(igra):
    return  """===================================================================

{geslo}
Napacne crke : {napacne_crke}
Ugibaš še : {število} -krat.
==============================================""".format(
    geslo=igra.pravilni_del_gesla(),
    crke=igra.nepravilni_ugibi()
    stevilo=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak())


def izpis_zmaga(igra):
    return 'Čestitam, uganil/a si geslo {}.'.format(igra)

def izpis_poraza(igra):
    return 'Več sreče prihodnjič.'

def zahtevaj_vnost():
    return input('Ugibaj:')

def pozeni_vmesnik():
    igra = model.nova_igra() #poklicemo funkcijo iz datoteke model
    while True: #neskoncna zanka
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje =igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

pozeni_vmesnik()
