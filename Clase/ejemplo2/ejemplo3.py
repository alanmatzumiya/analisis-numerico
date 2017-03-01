def str_product(str = '12.3, 12.0, 14.5'):
    '''
        strProduct(...)
            strProduct([str])

            Regresa el producto de los numeros contenidos en str separados por coma.

            Parameters
            ----------
            str : cadena
                str es una de caracteres que representa una lista de numeros separados por coma
            Returns
            -------
                prod : numero
                    prod es el producto de los numeros separados por coma de la lista
    '''

    prod, i , buffer = 1, 0, ''
    print 'str:=' , str
    for j in range(len(str)):
        if str[j] == ',':
            buffer = str[i:j]
            print buffer, i , j
            prod = prod * float(buffer)
            i = j + 1
            buffer = ''
    buffer = str[i:len(str)]
    print buffer, i , len(str)
    prod = prod * float(buffer)
    print prod
    return prod


str_product()
str_product('1.0,2.0,3.0,4.0')

