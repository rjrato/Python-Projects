from tkinter import filedialog


class DirectorySelection:

    def __init__(self, source_folder_entry=None, replica_folder_entry=None, logs_folder_entry=None):
        self.source_folder_entry = source_folder_entry
        self.replica_folder_entry = replica_folder_entry
        self.logs_folder_entry = logs_folder_entry

    def source_folder(self):
        source = filedialog.askdirectory()
        self.source_folder_entry.delete(0, "end")
        self.source_folder_entry.insert(0, source)

    def replica_folder(self):
        replica = filedialog.askdirectory()
        self.replica_folder_entry.delete(0, "end")
        self.replica_folder_entry.insert(0, replica)

    def logs_folder(self):
        logs = filedialog.askdirectory()
        self.logs_folder_entry.delete(0, "end")
        self.logs_folder_entry.insert(0, logs)

