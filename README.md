# google_api_etl
This repo contains all the tools necessary to build ETL pipelines from your gmail, capturing data such as...
* hyperlinks in the body of email messages
* category of message, as seen by user

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

Initialize the application by saving the output from the _authenticate()_ function to a variable, which will be used as the _auth_var_ argument in all future functions.

![image](https://github.com/Joe-Seifert/google_api_etl/assets/111460270/157011e1-24f0-41e1-a82d-209271711754)



# todo
Set a default variable name for authenticate so that other functions will not require an explicitly defined _auth_var_
