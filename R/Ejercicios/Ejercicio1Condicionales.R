numero <- readline()
numero <- as.numeric(numero)


if ((numero %% 2) == 0){
    print("Este numero es par")
} else if ((numero%%2) != 0){
    print("No es un numero par")
}
