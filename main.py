import msvcrt

#frase de prueba = me gusta dormir mucho
def main():
    #Pedir frase para extraer las iniciales de las palabras

    while True:
        phrase: str = input('Ingrese una frase (mínimo 3 palabras): ')
        phrase = phrase.lower().strip()
        listPhrase: list[str] = phrase.split( )

        if len(listPhrase)  < 3:
            print('La frase es muy corta')
        else:
            break

    initialOfWords:list = []
    iterator:int = 0

    #Transformar letras por medio en mayuscula
    for letter in listPhrase:
        initialOfWords.append(letter[0][0])
        if iterator % 2 != 0:
            initialOfWords[iterator]= initialOfWords[iterator].upper()
        iterator+=1



    #Pedir números para mezclar con las iniciales
    numbers:str = ''
    while len(numbers) != len(initialOfWords) :
        numbers = input('Ingrese ' + str(len(initialOfWords)) + ' números: ')

    #Mezclar iniciales con números
    initialOfWordsAndNumbers:str = ''

    for i in range(len(initialOfWords)):
        initialOfWordsAndNumbers += initialOfWords[i] + numbers[i]

    #Pedir palabra de referencia para asociarla a la contraseña
    while True:
        reference: str = input('Ingrese palabra de referencia o recordatorio: ')\
            .lower()\
            .strip()\
            .capitalize()
        if len(reference.split( )) == 1:
            break

    password:str = initialOfWordsAndNumbers + reference

    #Entregar contraseña
    print('La contraseña generada es: ',password)

    msvcrt.getch()
main()