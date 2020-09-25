import sys

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
    txtFile = input('File name: ')
    while True:
        hasHeader = input('Does the file have header line? (Y/N): ').lower()
        if(hasHeader == 'y' or hasHeader == 'n'):
            break
    delimeter = input('Delimeter:')
    while True:
        try:
            columns = int(input('Columns: '))
            break
        except ValueError:
            print('This must be a number.')
    for x in range(0,int(columns)):
        while True:
            line = input(str(x+1) + ' column type: ').lower()
            if(checkType(line)):
                columnsTypes.append(line)
                break
            else:
                print("This is not a valid data type.")

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
                print('Error: Could not properly read file, quitting.')
                sys.exit()
        result = '(' + ",".join(string) + ')'
        print(result)
        ofile.write(result + "\n")

def main():
    try:
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
            print('Could not open file.')
            sys.exit()
        createLine()
        ifile.close()
        ofile.close()
    except KeyboardInterrupt:
        print("\nApplication stopped by the user.")
    

if __name__ == '__main__':
    main()