from mail import Message, Mailbox

running = True


def user_interface(mail) -> None:
    '''
    main running of ui
    '''

    while running:
        print_menu()

        selection = int(input('Enter a number between 1 and 7: '))

        if selection == 1:
            compose(mail)
        elif selection == 2:
            display(mail)
        elif selection == 3:
            delete(mail)
        elif selection == 4:
            filter(mail)
        elif selection == 5:
            view_selection(mail)
        elif selection == 6:
            print_selection(mail)
        elif selection == 7:
            quit()


def setup() -> None:
    '''
    enters initial values frome expected output
    '''

    print('\nWe need to set up your mailbox!')
    owner = input('Enter your email address: ')

    initial_in = [
        Message('me@xyz.com', 'f@xyz.com'),
        Message('me@xyz.com', 'd@xyz.com'),
        Message('me@xyz.com', 'c@xyz.com'),
        Message('me@xyz.com', 'i@xyz.com'),
        Message('me@xyz.com', 'i@xyz.com'),
    ]

    initial_out = [
        Message('h@xyz.com', 'me@xyz.com'),
        Message('k@xyz.com', 'me@xyz.com'),
        Message('d@xyz.com', 'me@xyz.com'),
        Message('g@xyz.com', 'me@xyz.com'),
        Message('d@xyz.com', 'me@xyz.com'),
    ]

    for msg in initial_in:
        msg.add_line('Line0')

    for msg in initial_out:
        msg.add_line('Line0')

    return Mailbox(owner, initial_in, initial_out)


def print_menu() -> None:
    '''
    prints menu choices
    '''
    print(
        '\n\n'
        '1. COMPOSE\n'
        '2. DISPLAY\n'
        '3. DELETE\n'
        '4. FILTER\n'
        '5. VIEW\n'
        '6. PRINT\n'
        '7. QUIT\n'
    )


def compose(mail) -> None:
    '''
    lets user make a new message
    '''

    recipient = input("Enter recipient's email address: ")
    print('Begin entering the message')
    print('Enter two blank lines in a row to stop composing')

    message = Message(mail.address, recipient)
    blank_line_count = 0

    while blank_line_count < 2:
        line = input()
        message.add_line(line)

        if line.strip() == '':
            blank_line_count += 1
        else:
            blank_line_count = 0

    mail.add_message(message)


def display(mail) -> None:
    '''
    calls mailbox display(), showing mailbox summary
    '''
    mail.display()


def delete(mail) -> None:
    '''
    deletes message based on user input
    '''

    incoming = input('Delete (I)ncoming or (O)utgoing message? ').lower()
    idx = 0

    if incoming == 'i':
        while idx < 1 or idx > mail.get_incoming_len():
            idx = input(
                f'Enter a number between 1 and {mail.get_incoming_len()}: ')
            idx = int(idx)

        incoming = True
    elif incoming == 'o':
        while idx < 1 or idx > mail.get_outgoing_len():
            idx = input(
                f'Enter a number between 1 and {mail.get_outgoing_len()}: ')
            idx = int(idx)

        incoming = False

    mail.delete(idx, incoming)


def filter(mail) -> None:
    '''
    filters emails by sender/receiver
    '''

    recipient = input(
        'Enter the recipient’s address to filter on, or enter to skip: '
        )
    sender = input(
        'Enter the sender’s address to filter on, or enter to skip: '
        )

    if sender.strip() == '':
        sender = mail.address

    print('Messages matching your query:')

    filtered = mail.filter(sender, recipient)

    for msg in filtered:
        print(msg)


def view_selection(mail) -> None:
    '''
    show individual message
    '''

    incoming = input('View (I)ncoming or (O)utgoing message? ').lower()
    idx = 0

    if incoming == 'i':
        incoming = True

        while idx < 1 or idx > mail.get_incoming_len():
            idx = input(
                f'Enter a number between 1 and {mail.get_incoming_len()}: ')
            idx = int(idx)
    elif incoming == 'o':
        incoming = False

        while idx < 1 or idx > mail.get_outgoing_len():
            idx = input(
                f'Enter a number between 1 and {mail.get_outgoing_len()}: ')
            idx = int(idx)

    print(mail.get_message(idx, incoming).show())


def print_selection(mail) -> None:
    '''
    print selection of the user
    '''

    file_name = input('Enter the name of the file to print to: ')
    incoming = input('Print (I)ncoming or (O)utgoing message? ').lower()
    idx = 0

    if incoming == 'i':
        incoming = True

        while idx < 1 or idx > mail.get_incoming_len():
            idx = input(
                f'Enter a number between 1 and {mail.get_incoming_len()}: ')
            idx = int(idx)
    elif incoming == 'o':
        incoming = False

        while idx < 1 or idx > mail.get_outgoing_len():
            idx = input(
                f'Enter a number between 1 and {mail.get_outgoing_len()}: ')
            idx = int(idx)

    mail.get_message(idx, incoming).write(file_name)


def quit_selection() -> None:
    '''
    ends UI loop
    '''
    running = False
    print('Bye!')


if __name__ == '__main__':
    mail = setup()
    user_interface(mail)
