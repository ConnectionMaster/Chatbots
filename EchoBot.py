bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that responds to a user's message: respond
def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
    bot_message = "I can hear you! You said: " + message
    # Return the result
    return bot_message
# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(____.format(____))
    # Get the bot's response to the message
    response = ____(____)
    # Print the bot template including the bot's response.
    print(____.format(____)) 
# Test function
print(respond("hello!"))