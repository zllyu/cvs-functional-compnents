# CVS Functional Components

## Overview

Azure Video Manager is a Python script designed to facilitate the management of video files stored in an Azure File Share. It enables users to list directories and files within a specified directory of an Azure File Share and download selected video files to their local system. This tool simplifies the process of organizing and accessing video content in the cloud.

## Features

- **Directory and File Listing**: Generates a list of all directories and files within a specified Azure File Share directory, saving this information into a local Excel file for easy access and management.
- **Video File Downloading**: Allows for the downloading of specific video files from the Azure File Share to the local system, making it easy to access and use these files offline.

## Prerequisites

Ensure you have the following prerequisites installed and set up:

- Python 3.x environment
- Access to an Azure Storage account with the necessary permissions

## Installation

To set up Azure Video Manager, follow these steps:

1. **Clone the repository** to your local machine to get a copy of the script.
2. **Install required Python packages**. Create a `requirements.txt` file with the content provided below, and install the dependencies using pip:
    ```
    azure-storage==0.37.0
    pandas==1.5.2
    ```
    Run the pip install command like so:
    `pip install -r requirements.txt`
3. **Prepare your Azure Storage account details**. You will need a connection string to your Azure Storage account, as well as the name of the Azure File Share you'll be working with.

## Configuration

Before running the script, configure the following variables within the script to match your Azure Storage settings and local environment:

- `AZURE_CONN_STR`: The connection string to your Azure Storage account.
- `AZURE_FILE_SHARE_NAME`: The name of the Azure File Share where your videos are stored.
- `AZURE_FILE_UPLOAD_DIR`: The directory within the Azure File Share where the video files are located.
- `LOCAL_INFO_PATH`: The path where the Excel file containing the list of directories and files will be saved locally.
- `VIDEO_NAME`: The name of the video file you wish to download.

## Usage

After configuring the script with your Azure Storage details, run it to list directories and files and/or download a specific video file:
```
python main.py
```

This operation will create an Excel file at the specified `LOCAL_INFO_PATH`, containing a list of files and directories. Additionally, it will download the specified video file to your local system.

## Security Note

The script includes sensitive information, such as your Azure Storage account connection string. Keep this information secure and do not share it publicly or store it in insecure locations.

## Contributing

## License
