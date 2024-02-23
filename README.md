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
Create a folder in active directory (I called mine /resources) containing a json folder with the API toke from Google's API suite

Always start any applicaiton with the authenticate function.  This will 
