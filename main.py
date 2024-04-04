from utils import list_dirs_and_files, download_file, download_directory


AZURE_CONN_STR = ""
AZURE_FILE_SHARE_NAME = "videos"
AZURE_FILE_UPLOAD_DIR = "clipped_videos/"
LOCAL_OUTPUT_DIR = "output/"

LOCAL_INFO_PATH = "list_items.xlsx"
VIDEO_NAME = "00d7995a-9c02-4ae6-a40d-fcdaab12b08d.mp4"


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

    download_directory() params:
        param1 - connection_string: Azure connection string
        param2 - share_name: Azure File Share name
        param3 - download_path: The path where a given folder stores on Azure File Share
        param4 - local_path: Save the video to a local path

    '''
    # list_dirs_and_files(AZURE_CONN_STR, AZURE_FILE_SHARE_NAME, AZURE_FILE_UPLOAD_DIR, LOCAL_INFO_PATH)
    # download_file(AZURE_CONN_STR, AZURE_FILE_SHARE_NAME, AZURE_FILE_UPLOAD_DIR+VIDEO_NAME, VIDEO_NAME)
    download_directory(AZURE_CONN_STR, AZURE_FILE_SHARE_NAME, AZURE_FILE_UPLOAD_DIR, LOCAL_OUTPUT_DIR)


if __name__ == "__main__":
    main()
