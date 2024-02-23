#This is specifically built to interface with Gmail API - other Google services are not yet supported

#---Import Dependencies---#
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import regex
import base64
import pandas as pd

#   GLOSSARY
#   get - returns list of items that meet specifications
#   show - returns list of all available items
#   store - saves results to directory



#authenticate
def authenticate(token_fpath = './resources/token.json', api_scope = 'https://mail.google.com/'):
    '''
    Returns Service Object used in every other function in this package.  This should be run before any other
    functions in this package.  Store the results of this function in a variable to pass to all other
    functions as the auth_var
    
    Before using any of these functions, you must first register your application in Google's Developer suite.
    See the following website for more instructions:
        https://cloud.google.com/apis/docs/getting-started
    Also see this youtube video, which helps visualize the process detailed in the previous URL
        https://www.youtube.com/watch?v=PKLG5pfs4nY

    token_fpath points this function to the file containing your individual Google API token, 
    which can be found in the google developer suite > project > APIs & Services > Credentials.
    I recommend keeping this in the same directory as the package code in a folder called resources.
    
    Available Scopes: https://developers.google.com/identity/protocols/oauth2/scopes
    
    Todo: 
    - Test multiple scopes
    - Change arguments of build function
    '''
    SCOPES = [api_scope]
    creds = None

    if os.path.exists(token_fpath):
        creds = Credentials.from_authorized_user_file(token_fpath, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(token_fpath, SCOPES)
            creds = flow.run_local_server(port = 0)
        with open('./resources/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials = creds)
    return service;

#show_label_ids
def show_label_ids(user_email, auth_var):
    '''
    Returns Pandas DataFrame of all labels associated with the email account
    
    auth_var is the return object from the authenticate() function
    '''
    results = auth_var.users().labels().list(userId=user_email).execute()
    labels = results.get("labels", [])

    if not labels:
        raise ValueError('No labels found')
    else:
        return pd.DataFrame(labels)

#get_messages
def get_messages(user_email, auth_var, label_id = None, include_spam_trash=False):
    '''
    Returns the ID for all emails in specified group of labels.
    label_id will accept lists, and leaving it blank will return all messages accross all mailboxes
    '''
    nextPageToken = None
    id_list = []
    
    if type(include_spam_trash) != bool:
        raise TypeError('include_spam_trash must be boolean');

    results = auth_var.users().messages().list(userId=user_email, labelIds=label_id, includeSpamTrash=include_spam_trash).execute()
    messages = results.get('messages', [])
    nextPageToken = results.get('nextPageToken', [])
    for message in messages:
        id_list.append(message['id'])

    while nextPageToken:
        results = auth_var.users().messages().list(userId=user_email, labelIds=label_id, includeSpamTrash=include_spam_trash, pageToken=nextPageToken).execute()
        messages = results.get('messages', [])
        nextPageToken = results.get('nextPageToken', [])
        for message in messages:
            id_list.append(message['id'])

    return(id_list)

#get_message_links
def get_message_links(user_email, email_id, auth_var, format='full'):
    '''
    Returns all links from single specified message using REGEX
    
    Todo:
    - change email_id to accept list of IDs
    '''
    try:
        result = auth_var.users().messages().get(userId=user_email, id=email_id, format=format).execute()
        snippet = result.get('snippet')
        urls = regex.findall(r"https?://[^\s]+", snippet)
    except Exception as e:
        print(f"Error processing message {email_id}: {e}")
    return(urls)

#get_message_body
def get_messge_body(user_email, email_id, auth_var, format='full'):
    '''
    Returns the entire body/snippet of an email.
    More data on the message is available through different elements in results
    
    Todo:
    - create function to store all message data in a DataFrame
    '''
    results = auth_var.users().messages().get(userId=user_email, id=email_id, format=format).execute()
    snippet = results.get('snippet')
    return(snippet);

#store_message_attachments
def store_message_attachments(user_email, email_id, auth_var, fpath = './outputs'):
    '''
    Stores attachments from single message in specified directory
    
    Todo:
    - Check if file path exists, and, if it does not, create it 
    '''
    message = auth_var.users().messages().get(userId=user_email, id=email_id).execute()

    for part in message['payload']['parts']:
        if part['filename']:
            if 'data' in part['body']:
                data = part['body']['data']
            else:
                att_id = part['body']['attachmentId']
                att = auth_var.users().messages().attachments().get(userId=user_email, messageId='msg_id',id=att_id).execute()
                data = att['data']
            file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
            path = part['filename']
            with open(f'{fpath}/{path}', 'wb') as f:
                f.write(file_data)
    return None;
