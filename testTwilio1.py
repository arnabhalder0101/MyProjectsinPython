from twilio.rest import Client
import credentials


def MessageNotify(body, to):
    account_sid = credentials.account_sid
    auth_token = credentials.auth_token

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+12058905444',
        body=body,
        to=to
    )
    return message

