import sys
import os

ifile = None
ofile = None
txtFile = None
delimeter = None
columns = None
columnsTypes = []
hasHeader = None

types = {
    'bit' : 'numeric',
    'tinyint' : 'numeric',
    'bool' : 'numeric',
    'boolean' : 'numeric',
    'smallint' : 'numeric',
    'mediumint' : 'numeric',
    'int' : 'numeric',
    'integer' : 'numeric',
    'bigint' : 'numeric',
    'float' : 'numeric',
    'double' : 'numeric',
    'decimal' : 'numeric',
    'dec' : 'numeric',
    'money' : 'numeric',
    'char' : 'text',
    'nchar' : 'ntext',
    'varchar' : 'text',
    'nvarchar' : 'ntext',
    'binary' : 'text',
    'varbinary' : 'text',
    'tinyblob' : 'text',
    'tinytext' : 'text',
    'text' : 'text',
    'blob' : 'text',
    'mediumtext' : 'text',
    'mediumblob' : 'text',
    'longtext' : 'text',
    'longblob' : 'text',
    'date' : 'text',
    'datetime' : 'text',
    'timestamp' : 'text',
    'time' : 'text',
    'year' : 'text'
}

def checkType(input):
    global types
    for type in list(types.keys()):
        if(input==type):
            return True
    return False
     


def getArgs():
    global txtFile
    global delimeter
    global columns
    global columnsTypes
    global hasHeader
    txtFile = input('Nazwa pliku: ')
    while True:
        hasHeader = input('Czy plik zawiera wiersz nagłówkowy? (Y/N): ').lower()
        if(hasHeader == 'y' or hasHeader == 'n'):
            break
    delimeter = input('Znak rodzielający:')
    while True:
        try:
            while True:
                columns = int(input('Ilość kolumn: '))
                if columns>0:
                    break
                print('To musi być dodatnia liczba naturalna.')
            break
        except ValueError:
            print('Liczba kolumn musi być liczbą.')
    for x in range(0,int(columns)):
        while True:
            line = input('Typ ' + str(x+1) + ' kolumny: ').lower()
            if(checkType(line)):
                columnsTypes.append(line)
                break
            else:
                print("To nie jest prawidłowy typ danych.")

def createLine():
    pass
    string = None
    if(hasHeader == 'y'):
        next(ifile)
    for line in ifile:
        string = line.split(str(delimeter))
        while(len(string) > int(columns)):
            string.pop()
        string[len(string)-1] = string[len(string)-1].replace('\n','')
        for i in range(0,int(columns)):
            try:
                if(types.get(columnsTypes[i]) == 'numeric'):
                    pass
                if(types.get(columnsTypes[i]) == 'text'):
                    string[i] = '\'' + string[i] + '\''
                if(types.get(columnsTypes[i]) == 'ntext'):
                    string[i] = 'N\'' + string[i] + '\''
            except IndexError:
                print('Error: Nie można poprawnie odczytać pliku.')
                sys.exit()
        result = '(' + ",".join(string) + '),'
        print(result)
        ofile.write(result + "\n")
    ofile.seek(ofile.tell() - 3, os.SEEK_SET)
    ofile.truncate()

def main():
    try:
        while True:
            if(len(sys.argv)<2):
                getArgs()
            else:
                pass
            try:
                global ifile
                global ofile
                ifile = open(txtFile, "r")
                ofile = open('result_'+txtFile,"w")
            except IOError:
                print('Nie można otworzyć pliku.')
                sys.exit()
            createLine()
            ifile.close()
            ofile.close()
    except KeyboardInterrupt:
        print("\nAplikacja zamknięta przez użytkownika.")
    

if __name__ == '__main__':
    main()
