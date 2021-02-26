class Message():

    def __init__(self, sender, recipient) -> None:
        self.sender = sender
        self.recipient = recipient
        self.message = ''

    def add_line(self, append: str) -> None:
        '''
        appends  a  line  of  text  to  the  message  body
        takes  a  single  string  as  a parameter
        '''
        self.message += append + "\n"

    def show(self) -> None:
        '''
        prints contents of message in an email format
        '''
        print("TO:", self.recipient)
        print("FROM:", self.sender)
        print("\n" + self.message)

    def write(self, filename: str) -> None:
        '''
        writes the contents of the message to a file in show() format
        takes in the filename as a str parameter
        '''
        file = open(filename, 'w')
        file.write(
            "TO: " + self.recipient + "\n" + "FROM: " + self.sender + "\n" + 
            self.message
        )
        file.close()

    def __str__(self) -> str:
        '''
        returns a string formatted like show() with contents of message
        '''
        summary = "TO: " + self.recipient + "\n" + "FROM: " + self.sender + "\n"
        summary += self.message[:min(len(self.message), 25)]
        return summary

    def get_sender(self) -> str:
        '''returns sender address'''
        return self.sender

    def get_recipient(self) -> str:
        '''returns recipient address'''
        return self.recipient


class Mailbox():

    def __init__(self, address, incoming=[], outgoing=[]) -> None:
        self.address = address
        self.incoming = incoming
        self.outgoing = outgoing

    def add_message(self, msg: "Message"):
        '''
        adds message to corresponding mailbox
        '''
        if msg.recipient == self.address:
            self.incoming.append(msg)
        else:
            self.outgoing.append(msg)

    def display(self):
        '''
        print summary of all mail in the mailbox
        '''
        print('INBOX:\n')
        for idx, msg in enumerate(self.incoming):
            print(str(idx + 1) + '.', msg.__str__().replace("\n", ' '))
        print('\nSENT:\n')
        for idx, msg in enumerate(self.outgoing):
            print(str(idx + 1) + '.', msg.__str__().replace("\n", ' '))

    def get_message(self, idx: int, incoming: bool) -> "Message":
        '''
        returns message by index in corresponding list
        '''
        if incoming:
            return self.incoming[idx - 1]
        else:
            return self.outgoing[idx - 1]

    def delete(self, idx: int, incoming: bool) -> "Message":
        '''
        deletes message by index in corresponding list and returns it
        '''
        if incoming:
            removed = self.incoming[idx - 1]
            self.incoming.remove(removed)
            return removed
        else:
            removed = self.outgoing[idx - 1]
            self.outgoing.remove(removed)
            return removed

    def filter(self, sender='', recipient='') -> list:
        '''
        takes in sender and recipient str parameters and returns a list of
        Messages with matching data
        '''
        filtered = []
        for msg in self.incoming:
            if sender == msg.sender or recipient == msg.recipient:
                filtered.append(msg)
        for msg in self.outgoing:
            if sender == msg.sender or recipient == msg.recipient:
                filtered.append(msg)

        return filtered

    def __str__(self) -> str:
        '''
        returns summary string of this mailbox
        '''
        msgQty = str(len(self.incoming) + len(self.outgoing))
        return self.address + "'s Mailbox - contains " + msgQty + " messages."

    def get_incoming_len(self) -> int:
        return len(self.incoming)

    def get_outgoing_len(self) -> int:
        return len(self.outgoing)


def testMessage(sender: str, recipient: str, message: "Message") -> None:

    msg = Message(sender, recipient)
    msg.add_line(message)

    assert msg.sender == sender == msg.get_sender()
    assert msg.recipient == recipient == msg.get_recipient()
    print(msg.message)
    print(message)
    assert msg.message == (message + "\n")

    msg.show()
    msg.__str__()


def testMailbox():
    msg1 = Message('me@me.com', 'you@you.com')
    msg1.add_line('test1')
    msg2 = Message('me@me.com', 'you@you.com')
    msg2.add_line('test2')
    msg3 = Message('you@you.com', 'me@me.com')
    msg3.add_line('test3')
    msg4 = Message('you@you.com', 'me@me.com')
    msg4.add_line('test4')
    mail = Mailbox('me@me.com', [msg3, msg4], [msg1, msg2])

    mail.display()
    assert mail.get_message(1, True) == msg3
    assert mail.delete(1, True) == msg3
    assert mail.get_message(1, True) == msg4
    print(mail.filter(sender='you@you.com'))


if __name__ == "__main__":
    testMessage('me@me.com',
                'you@you.com',
                'This is a test message of over length 25 characters'
                )
    testMailbox()
