import messaging as msging


def testTextMessage(sender, recipient, message) -> None:
    '''
    runs a variety of tests to make sure TextMessage is running properly
    '''
    msg = msging.TextMessage(sender, recipient)
    assert msg.add_line(message)
    assert msg.sender == sender == msg.get_sender()
    assert msg.recipient == recipient == msg.get_recipient()
    assert msg.message == message
    big = 'e' * 140
    assert msg.add_line(big) == False
    msg.grandmafy()
    assert 'you' and 'to' not in msg.message
    msg.show()
    print(msg.__str__())
    print("All tests pass!")


if __name__ == "__main__":
    testTextMessage('me', 'you', 'hello you are here to?')
