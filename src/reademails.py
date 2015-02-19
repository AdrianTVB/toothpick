__author__ = 'Danrex'

# readyouremail.py

import imaplib
import email


def get_unread_emails():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('bassett199@gmail.com', 'password')
    mail.list()
    mail.select('inbox')
    typ, data = mail.search(None, 'ALL')
    ids = data[0]
    id_list = ids.split()

    # get the most recent email id
    latest_email_id = int( id_list[-1] )

    # iterate through 15 messages in descending order starting with latest_email_id
    # the '-1' dictates reverse looping order
    for i in range( latest_email_id, latest_email_id-15, -1 ):
        typ, data = mail.fetch( i, '(RFC822)' )

        for response_part in data:
          if isinstance(response_part, tuple):
              msg = email.message_from_string(response_part[1])
              varSubject = msg['subject']
              varFrom = msg['from']

        # remove the brackets around the sender email address
        varFrom = varFrom.replace('<', '')
        varFrom = varFrom.replace('>', '')

        # add ellipsis (...) if subject length is greater than 35 characters
        if len( varSubject ) > 35:
          varSubject = varSubject[0:32] + '...'

        print('[' + varFrom.split()[-1] + '] ' + varSubject)
    mail.close()



if __name__ == "__main__":
    raise NotImplementedError()