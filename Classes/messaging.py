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


class TextMessage(Message):

    def __init__(self, sender, recipient) -> None:
        super().__init__(sender, recipient)

    def add_line(self, append: str) -> bool:
        '''
        appends  a  line  of  text  to  the  message  body
        '''
        if len(self.message) > 0:
            self.message += (' ' + append)
        else:
            self.message += append

        if len(self.message) >= 140:
            self.message = self.message[:140]
            return False

        return True

    def show(self) -> None:
        print("From:", self.sender)
        print(self.message)

    def grandmafy(self) -> None:
        '''
        replaces every “ you ” in the text with “u”
        replaces every “ to ” in the text with “2”
        '''
        self.message = self.message.replace(' to ', ' 2 ')
        self.message = self.message.replace('to ', '2 ')
        self.message = self.message.replace(' you ', ' u ')
        self.message = self.message.replace('you ', 'u ')


def testTextMessage(sender, recipient, message) -> None:
    '''
    runs a variety of tests to make sure TextMessage is running properly
    '''
    msg = TextMessage(sender, recipient)
    assert msg.add_line(message)
    assert len(msg.message) <= 140
    assert msg.sender == sender == msg.get_sender()
    assert msg.recipient == recipient == msg.get_recipient()
    assert msg.message == message
    big = 'e' * 140
    assert msg.add_line(big) == False
    assert len(msg.message) <= 140
    msg.grandmafy()
    assert ' you ' and ' to ' and 'you ' and 'to ' not in msg.message
    msg.show()
    print("All tests pass!")


if __name__ == "__main__":
    testTextMessage('me', 'you', 'hello you are here to?')
