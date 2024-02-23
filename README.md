# google_api_etl
This repo contains tools necessary to build ETL pipelines from your gmail, capturing data such as...
* hyperlinks in the body of email messages
* category of message, as seen by user
* full email body
* message attachments

The style of tool seeks to emulate a user's search path through their personal mailbox, which primarily focuses on labels (important, starred, etc.)

#Registering an application with Google
Before using this code, you must register the appropriate application in Google's developer suite.  

The following resources detail the process of registering an application in google's developer suite:
* https://cloud.google.com/apis/docs/getting-started
* https://www.youtube.com/watch?v=PKLG5pfs4nY

The application's API token will live in the credentials section of your active project.  Remember the location of this token, becuase you will need to save it to use the authenticate function.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/566313d0-64d2-4efd-af50-1f1ec8d5f992)

# Sample Workflow
I am going to look through my email inbox to find all messages from my girlfriend containing links to instagram memes.  I deleted social media to enable my hermiting tendencies, so she has resorted to this primative method to share entertainment with me.  Once I have located the memes, I will open them all in my browser so that I can scroll through them efficently.

Create a folder in active directory (I called mine /resources) containing a json folder with the API token from Google's API suite.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/9390801b-4bd5-444e-b6b9-3958bfa28cf6)

The file should look like this:

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/a493e463-eb8c-4636-98f4-8a001ed4ddd2)

The _token_fpath_ argument of the _authenticate()_ function will reference this file path.  If you put your token in the same file path as I did (relative to the active directory) you will not have to specify this.  

Create a new jupyter notebook file in the active directory pictured above.  Import the necessary functions from the GmailApiPackage.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/9bd5a366-a9a4-48eb-96f2-f0ab74387137)

Initialize the application by saving the output from the _authenticate()_ function to a variable, which will be used as the _auth_var_ argument in all future functions.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/157011e1-24f0-41e1-a82d-209271711754)

Now, I want to search for all messages that I have labeled as "Michelle Memes."  To find these, I will first use the _show_label_ids()_ function to find the ID associated with the "Michelle Memes" folder.  This function returns a pandas DataFrame containing all of the label metadata.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/35acc50b-5027-4471-81af-c4d90a3d116e)

Now that I have pinpointed the appropriate label ID, I can use the _get_messages()_ function to get the list of all message IDs with this label.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/fe51f65d-63a2-4562-9f56-65e5d64a6b5d)

This list is too long to scroll through in one sitting, so I would like to shorten it a bit.  I have already seen most of the memes that she has sent me, so I am going to look for only emails that are unread, looking at only unread memes.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/7b76f670-e6df-4ee9-8fb2-5d1e7d8b7eda)


This list is much more managable.  Now I will use the _get_message_links()_ function to extract only the URLs from the email bodies listed.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/151e3029-fb06-4603-807e-87f573e9f5f5)


The URL list is a bit sloppy, so I will use itertools.chain to remove the list nesting.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/d2f4c6f2-fb79-45e1-8516-a3d69d337196)


Now the only thing left to do is open the links in a web browser.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/61816e34-888c-42bc-9d38-2214ee096eaa)


# todo
Set a default variable name for authenticate so that other functions will not require an explicitly defined _auth_var_
