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
            "TO:", self.recipient, "\n",
            "FROM:", self.sender, "\n",
            self.message
        )
        file.close()

    def __str__(self) -> str:
        '''
        returns a string formatted like show() with contents of message
        '''
        summary = "TO: " + self.recipient + "\n" + "FROM:" + self.sender + "\n"
        summary += self.message[:min(len(self.message), 25)]
        return summary

    def get_sender(self) -> str:
        '''returns sender address'''
        return self.sender

    def get_recipient(self) -> str:
        '''returns recipient address'''
        return self.recipient



def Mailbox():

    def __init__(self, address, incoming = [], outgoing = []) -> None:
        self.address = address
        self.incoming = incoming
        self.outgoing = outgoing