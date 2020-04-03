def is_valid(msg):
    if list(msg)[0] == '!':
        msg = msg.replace(msg[:1], '')

        if list(msg)[-1] == '!':
            msg = msg.replace(msg[-1], '')
            return msg, 'long'
        else:
            return msg, 'short'

    else:
        return False
