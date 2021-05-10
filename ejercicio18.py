segundos  =  int ( input ( "Ingrese un tiempo en segundos:" ))
hora  =  segundos  /  3600
segundos  =  segundos  %  3600
minutos  =  segundos  /  60
segundos  =  segundos  %  60
print ( "la hora es:" , int ( hora ), int ( minutos ), segundos )