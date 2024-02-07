import pprint, os, random




def initTicket(ticket):
    '''
    Initializing a ticket
    :param ticket: an empty ticket
    :return: None
    '''
    for row in range(len(ticket)):
        ticket[row][0] = round(random.random() * 9)
        for col in range(1, len(ticket[0])):
            ticket[row][col] = round(random.random() * 99)

def printTicket(ticket):
    for row in range(len(ticket)):
        for col in range(len(ticket[0])):
            print(str(ticket[row][col]).rjust(5), end=' ')
        print()



def createBunchTicket():
    print("How many do you want the ticket: ")
    numTicket = int(input())
    tickets = []
    for loop in range(numTicket):
        ticket = [[0 for i in range(5)] for j in range(15)]
        initTicket(ticket)
        tickets.append(ticket)
    return tickets

def checkBingoTicket(ticket):
    BINGO = ['O'] * 5
    for row in ticket:
        if row == BINGO:
            return True
    return False

def tickBingo(tickes, num):
    for ticket in tickes:
        for row in ticket:
            if num in row:
                row[row.index(num)] = 'O'
        if checkBingoTicket(ticket):
            print('BINGO'.center(50, '*'))
            printTicket(ticket)

def gamePlay():
    tickets = createBunchTicket()
    print("Enter the number to guess: ")
    guess = int(input())
    for i in range(guess):
        num = random.randint(0, 99)
        tickBingo(tickets, num)
        checkBingoTicket(tickets)


gamePlay()
