
### English:

# PhotoBackup

This Python script allows you to upload files from an external storage device to Google Drive automatically once the device is connected to the system.

## Dependencies

- [PyDrive](https://pythonhosted.org/PyDrive/): A Python library for interacting with the Google Drive API.
- [Pyudev](https://pyudev.readthedocs.io/en/latest/): A Python library for managing hardware device events on the system.
- Make sure to run the program in a `Linux` environment as it's not possible to run the software on Windows.

## Configuration

1. Install the dependencies by running `pip install PyDrive pyudev`.
2. Make sure you have a Google account and create a project on the [Google Cloud Console](https://console.cloud.google.com/).
3. Enable the Google Drive API for your project and create OAuth credentials.
4. Save the JSON credentials file in your execution environment and rename it to `client_secrets.json`.

## Usage

1. Connect the external storage device to the system.
2. Run the Python script `main.py` with the command `sudo python3 main.py` since the program can only be run as an administrator.
3. If it's the first time running the script, you'll be prompted to authorize access to Google Drive.
4. Once authorized, the files present on the device will be automatically uploaded to Google Drive.
5. 
## Note

- Ensure you have mounting permissions for the external storage device. Otherwise, file upload won't happen correctly.
- Files are uploaded to the root of your Google Drive.
- Currently, the mount path of the external device is hardcoded in the code. You can manually change it.

## Contributions

Feel free to contribute to this project through issues and pull requests!

## License
This project is licensed under the terms of the [MIT License](LICENSE).






