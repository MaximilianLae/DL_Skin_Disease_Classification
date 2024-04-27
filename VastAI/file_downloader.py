from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
import io

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'credentials.json'
# FILE_ID = '1j1jFq0K_3GoSO9RWQHgRw2P3ftKVUxDh'
FILE_ID = '1_rlFVX4PuHndfT8WmbCvCqeOQqYFuFrX'

def auth():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)

def download_file(service, file_id):
    request = service.files().get_media(fileId=file_id)
    fh = open('test.ipynb', 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    fh.close()

def main():
    service = auth()
    download_file(service, FILE_ID)

if __name__ == '__main__':
    main()