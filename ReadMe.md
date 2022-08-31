# For Local SMTP server:
1. Change the Mail argument local to True
2. Run the following in the terminal:

        $ python -m smtpd -c DebuggingServer -n localhost:1025
# Testing

Mongo DB testing should be handled with care for the reasons below:

1. a new round is inserted autumaticaly with the current date.
2. tests work on the deployed db