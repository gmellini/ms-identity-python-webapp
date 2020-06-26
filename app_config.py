import os

CLIENT_SECRET = "Enter_the_Client_Secret_Here" # Our Quickstart uses this placeholder
# In your production app, we recommend you to use other ways to store your secret,
# such as KeyVault, or environment variable as described in Flask's documentation here
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

CLIENT_ID = "Enter_the_Application_Id_here"

REDIRECT_PATH = "/getAToken"  # It will be used to form an absolute URL
    # And that absolute URL must match your app's redirect_uri set in AAD

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
# BASIC READ SCOPE
SCOPE = ["User.ReadBasic.All"]
# COFENSE POST SCOPE
# https://cofense.com/mfa-bypass-phish-caught-oauth2-grants-access-user-data-without-password/
#SCOPE = ["Contacts.Read", "User.Read", "Mail.Read", "Notes.Read.All", "MailboxSettings.ReadWrite", "Files.ReadWrite.All"]
# GET SHARED FILES SCOPE
# https://docs.microsoft.com/en-us/graph/api/drive-sharedwithme?view=graph-rest-1.0&tabs=http
#SCOPE = ["Files.Read.All", "Files.ReadWrite.All", "Sites.Read.all", "Sites.ReadWrite.All"]

SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session

