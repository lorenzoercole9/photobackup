import os
import time
from pyudev import Context, Monitor
from pyudev.glib import MonitorObserver
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Funzione per caricare file su Google Drive
def upload_to_google_drive(file_path):
    gauth = GoogleAuth()
    # Effettua l'autenticazione con Google Drive
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    # Carica il file su Google Drive
    file_name = os.path.basename(file_path)
    file = drive.CreateFile({'title': file_name})
    file.SetContentFile(file_path)
    file.Upload()
    print("File {} caricato su Google Drive.".format(file_name))

# Funzione per gestire l'evento di collegamento di una periferica USB
def handle_usb_event(action, device):
    if 'usb' in device.subsystem:
        if action == 'add':
            print("Periferica USB collegata: {}".format(device.get('DEVNAME')))
            # Ottieni il percorso della periferica USB
            usb_path = device.get('DEVNAME')
            # Elenca i file nella periferica USB e carica ognuno su Google Drive
            for root, dirs, files in os.walk(usb_path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    upload_to_google_drive(file_path)
        elif action == 'remove':
            print("Periferica USB rimossa: {}".format(device.get('DEVNAME')))

def main():
    # Crea il contesto di udev
    context = Context()

    # Crea un monitor udev e lo configura per monitorare i dispositivi USB
    monitor = Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    # Crea un observer per monitorare gli eventi del monitor udev
    observer = MonitorObserver(monitor, handle_usb_event, name='usb-monitor')
    observer.start()

    print("In attesa di periferiche USB...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()
