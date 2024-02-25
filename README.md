
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

---

### Italiano:

# PhotoBackup

Questo script Python consente di caricare i file da un dispositivo di archiviazione esterno su Google Drive automaticamente una volta che il dispositivo viene collegato al sistema.

## Dipendenze

- [PyDrive](https://pythonhosted.org/PyDrive/): Una libreria Python per interagire con l'API di Google Drive.
- [Pyudev](https://pyudev.readthedocs.io/en/latest/): Una libreria Python per gestire eventi di dispositivi hardware sul sistema.
- Assicurati di eseguire il programma in un ambiente `Linux` poiche non possibile avviare il software su windows

## Configurazione

1. Installa le dipendenze eseguendo `pip install PyDrive pyudev`.
2. Assicurati di avere un account Google e crea un progetto su [Google Cloud Console](https://console.cloud.google.com/).
3. Abilita l'API di Google Drive per il tuo progetto e crea le credenziali OAuth.
4. Salva il file delle credenziali JSON nel tuo ambiente di esecuzione e rinominalo in `client_secrets.json`.

## Utilizzo

1. Collega il dispositivo di archiviazione esterno al sistema.
2. Esegui lo script Python `main.py` con il comando `sudo python3 main.py` poiche e' possibile avviare il programma solo come amministratore
3. Se è la prima volta che esegui lo script, sarà richiesto di autorizzare l'accesso a Google Drive.
4. Una volta autorizzato, i file presenti sul dispositivo verranno automaticamente caricati su Google Drive.

## Nota

- Assicurati di avere i permessi di montaggio per il dispositivo di archiviazione esterno. In caso contrario, il caricamento dei file non avverrà correttamente.
- I file vengono caricati nella radice del tuo Google Drive.
- Attualmente il percorso di montaggio del dispositivo esterno è fisso nel codice. È possibile modificarlo manualmente.

## Contributi

Senti libero di contribuire a questo progetto attraverso problemi e pull requests!

