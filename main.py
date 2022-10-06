from time import localtime, strftime



horaActual = {"diaSemana":strftime("%a", localtime()),
              "hora":int(strftime("%H", localtime()))-5,
              "minutos":int(strftime("%M", localtime())),
              "segundos":int(strftime("%S", localtime()))}


def horaDeIrACasa(horaActual):

  if horaActual['diaSemana'] == 'Sun' or horaActual['diaSemana'] == 'Sat':
    print("Hora de volver a casa")
    return
  elif horaActual['hora'] < 19 and horaActual['hora'] > 8:
    salidaEnSegundos=18*60*60
    restanteEnSegundos=salidaEnSegundos-(horaActual['hora']*60*60+horaActual['minutos']*60+horaActual['segundos'])
    restanteHoras=restanteEnSegundos//3600
    restanteMinutos=(restanteEnSegundos%3600)//60
    restanteSegundos=(restanteEnSegundos%3600)%60
    
    print("Faltan", restanteHoras, "horas", restanteMinutos,"minutos y",restanteSegundos,"segundos")

horaDeIrACasa(horaActual)