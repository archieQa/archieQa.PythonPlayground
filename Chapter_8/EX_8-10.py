def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)  # Removes the first message from the list
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)  # Adds it to the sent_messages list

# Example lists
messages = ["Hello, world!", "Python is great!", "Keep learning!"]
sent_messages = []

send_messages(messages[:], sent_messages)

print("Final messages list:", messages)  # Should be empty
print("Sent messages list:", sent_messages)  # Should contain all messages
