from azure.storage.fileshare import ShareFileClient, ShareDirectoryClient
import pandas as pd
import os


def download_file(connection_string, share_name, download_path, local_path):
    file_client = ShareFileClient.from_connection_string(conn_str=connection_string, share_name=share_name, file_path=download_path)
    with open(local_path, "wb") as file_handle:
        data = file_client.download_file()
        data.readinto(file_handle)


def download_directory(connection_string, share_name, dir_path, local_dir_path):
    directory_client = ShareDirectoryClient.from_connection_string(conn_str=connection_string, share_name=share_name, directory_path=dir_path)
    
    # make sure local dir exists
    os.makedirs(local_dir_path, exist_ok=True)

    # list out all files and sub-dirs in the given dir
    my_files = list(directory_client.list_directories_and_files())
    for file_item in my_files: 
        if file_item['is_directory']:
            # skip if is a sub-dir
            print(f"Skipping directory: {file_item['name']}", flush=True)
        else:
            # download files
            file_client = ShareFileClient.from_connection_string(conn_str=connection_string, share_name=share_name, file_path=os.path.join(dir_path, file_item['name']))
            local_file_path = os.path.join(local_dir_path, file_item['name'])
            with open(local_file_path, "wb") as file_handle:
                data = file_client.download_file()
                data.readinto(file_handle)
            print(f"Downloaded {file_item['name']} to {local_file_path}", flush=True)


def list_dirs_and_files(connection_string, share_name, parent_dir, local_path):
    parent_dir = ShareDirectoryClient.from_connection_string(conn_str=connection_string, share_name=share_name, directory_path=parent_dir)
    my_list = list(parent_dir.list_directories_and_files())
    
    formatted_data_list = []
    for data in my_list:
        data_dict = {item[0]: item[1] for item in data.items()}
        formatted_data_list.append(data_dict)

    data_df = pd.DataFrame(formatted_data_list)
    for column in data_df.columns:
        data_df[column] = data_df[column].apply(lambda x: str(x) if not pd.isnull(x) else x)

    excel_path = local_path
    data_df.to_excel(excel_path, index=False)