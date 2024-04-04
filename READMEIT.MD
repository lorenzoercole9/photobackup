
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

## Licenza

Questo progetto è concesso in licenza sotto i termini della [Licenza MIT](LICENSE).

Puoi trovare i dettagli della licenza a questa pagina [Licenza MIT](https://opensource.org/licenses/).
