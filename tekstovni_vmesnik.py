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
    return 'Več sreče prihodnjič.'.format(igra)