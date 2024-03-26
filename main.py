from utils import list_dirs_and_files, download_file


AZURE_CONN_STR = ""
AZURE_FILE_SHARE_NAME = "videos"
AZURE_FILE_UPLOAD_DIR = "uploaded_videos/"

LOCAL_INFO_PATH = "list_items.xlsx"
VIDEO_NAME = "b3a532d8-0ac2-4a4f-8bd5-4918583a073f.mp4"


def main():
    '''
    list_dirs_and_files() params:
        param1 - connection_string: Azure connection string
        param2 - share_name: Azure File Share name
        param3 - parent_dir: Show all files' information in a given directory
        param4 - local_path: Save the info to a local Excel file
    
    download_file() params:
        param1 - connection_string: Azure connection string
        param2 - share_name: Azure File Share name
        param3 - download_path: The path where a given video stores on Azure File Share
        param4 - local_path: Save the video to a local path

    '''
    list_dirs_and_files(AZURE_CONN_STR, AZURE_FILE_SHARE_NAME, AZURE_FILE_UPLOAD_DIR, LOCAL_INFO_PATH)
    download_file(AZURE_CONN_STR, AZURE_FILE_SHARE_NAME, AZURE_FILE_UPLOAD_DIR+VIDEO_NAME, VIDEO_NAME)


if __name__ == "__main__":
    main()
