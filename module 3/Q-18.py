message = "Hello Everyone Bye Everyone"
hello_message, bye_message = [msg + ' Everyone' for msg in message.split(' Everyone') if msg]
print(hello_message)