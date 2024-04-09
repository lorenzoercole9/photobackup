import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pyudev

gauth = GoogleAuth()

# Prova a caricare le credenziali salvate
if os.path.exists("mycreds.txt"):
    gauth.LoadCredentialsFile("mycreds.txt")

if gauth.access_token_expired:
    # Rinnova il token di accesso utilizzando il token di refresh
    gauth.Refresh()
elif gauth.credentials is None:
    # Autenticazione se non ci sono credenziali
    gauth.LocalWebserverAuth()
else:
    # Autorizza le credenziali salvate
    gauth.Authorize()

# Salva le credenziali per la prossima esecuzione
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)


context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='block')

for device in iter(monitor.poll, None):
    if 'ID_FS_TYPE' in device:
        device_name = device.get('DEVNAME')
        device_mount_point = device.get('ID_FS_MOUNT_POINT')
        print('Device {} was added'.format(device_name))
        print('Device mount point: {}'.format(device_mount_point))

        if device_mount_point is None:
            print("Device not mounted, attempting to mount...")
            # Crea un punto di montaggio basato sul nome del dispositivo
            mount_point = f"/media/lorenzo/{os.path.basename(device_name)}"  # sostituisci 'username' con il tuo nome utente
            os.makedirs(mount_point, exist_ok=True)
            mount_command = f"sudo mount {device_name} {mount_point}"
            result = os.system(mount_command)
            if result == 0:
                device_mount_point = mount_point
            else:
                print(f"Failed to mount {device_name}. Skipping...")
                continue

        # Prosegue con l'upload dei file se il dispositivo è già montato
        try:
            for root, dirs, files in os.walk(device_mount_point):
                for file in files:
                    file_path = os.path.join(root, file)
                    print(f"Found file: {file_path}")
                    gfile = drive.CreateFile({'title': os.path.basename(file_path)})
                    gfile.SetContentFile(file_path)
                    gfile.Upload()
                    print(f"Uploaded {file_path} to Google Drive")
                    
                    # Cancella il file dopo averlo caricato
                    os.remove(file_path)
                    print(f"Deleted {file_path} from local device")
        except TypeError:
            print("Errore: os.walk ha ricevuto un argomento non valido.")
