tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def display(table):
    '''
    Displays data table
    :param table: a data
    :return: None
    '''
    colWidths = [0] * len(table)


    setColWidths(colWidths, table)

    rs = setupLocation(colWidths, table)

    print(rs)


def setupLocation(colWidths, table):
    rs = ''
    for i in range(len(table[0])):
        for j in range(len(table)):
            rs += table[j][i].rjust(colWidths[j] + 10)
        rs += '\n'
    return rs


def setColWidths(colWidths, table):
    col = 0;
    for row in table:
        maxWidth = 0
        for field in row:
            if len(field) > maxWidth:
                maxWidth = len(field)
        colWidths[col] = maxWidth
        col += 1


display(tableData)
