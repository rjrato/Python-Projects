from eventHandler import EventHandler
from watchdog.observers import Observer
from threading import Timer
from tkinter import messagebox
import os
import shutil


class SyncFolder:

    def __init__(self, source_folder_entry, replica_folder_entry, sync_time_entry, logs_folder_entry, app_interface):
        self.source_folder_entry = source_folder_entry
        self.replica_folder_entry = replica_folder_entry
        self.logs_folder_entry = logs_folder_entry
        self.sync_time_entry = sync_time_entry
        self.app_interface = app_interface
        self.observer = Observer()
        self.sync_timer = None

    def start_monitoring(self):

        self.observer = Observer()

        source_dir = self.source_folder_entry.get().strip()
        replica_dir = self.replica_folder_entry.get().strip()
        sync_time_entry = self.sync_time_entry.get().strip()

        try:

            if not source_dir:
                messagebox.showwarning(title="Error", message="Please insert the folder you want to replicate.")
                return False

            if not replica_dir:
                messagebox.showwarning(title="Error", message="Please insert the replication path.")
                return False

            if not sync_time_entry:
                messagebox.showwarning(title="Error", message="Sync time missing or invalid.\nPlease insert a number to define the Sync periodicity, in seconds.")
                return False

        except ValueError:

            return False

        else:

            event_handler = EventHandler(self.app_interface, self.logs_folder_entry)
            self.observer.schedule(event_handler, source_dir, recursive=True)
            self.observer.schedule(event_handler, replica_dir, recursive=True)
            self.observer.start()
            self.schedule_sync()

            return True

    def schedule_sync(self):
        sync_time_entry = int(self.sync_time_entry.get().strip())
        if self.sync_timer:
            self.sync_timer.cancel()
        self.sync_timer = Timer(sync_time_entry, self.sync_folders)
        self.sync_timer.start()

    def stop_monitoring(self):
        self.observer.stop()
        self.observer.join()

    def sync_folders(self):
        source_dir = self.source_folder_entry.get()
        replica_dir = self.replica_folder_entry.get()

        for root, dirs, files in os.walk(source_dir):
            for name in files:
                source_file = os.path.join(root, name)
                replica_file = source_file.replace(source_dir, replica_dir)
                os.makedirs(os.path.dirname(replica_file), exist_ok=True)

                if not os.path.exists(replica_file) or os.stat(str(source_file)).st_mtime - os.stat(str(replica_file)).st_mtime > 1:
                    shutil.copy2(str(source_file), str(replica_file))

        for root, dirs, files in os.walk(replica_dir):
            for name in files:
                replica_file = os.path.join(root, name)
                source_file = replica_file.replace(replica_dir, source_dir)
                if not os.path.exists(source_file):
                    os.remove(replica_file)

            for directory in dirs:
                replica_dir_path = os.path.join(root, directory)
                source_dir_path = replica_dir_path.replace(replica_dir, source_dir)

                if not os.path.exists(source_dir_path):
                    shutil.rmtree(replica_dir_path)

        self.schedule_sync()
