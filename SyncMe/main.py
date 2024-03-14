from eventHandler import EventHandler
from ui import AppInterface
from syncFolders import SyncFolder


class SyncMeApp:
    def __init__(self):
        # _GUI INITIALIZING____________________________________________________
        self.app_interface = AppInterface()
        # _GET SOURCE, REPLICA AND SYNC_TIME FROM GUI__________________________
        self.source = self.app_interface.source_folder_entry
        self.replica = self.app_interface.replica_folder_entry
        self.sync_time = self.app_interface.sync_time_entry
        # _PASS PREVIOUS VALUES TO SYNCFOLDER___________________________________
        self.sync_folders = SyncFolder(
            self.source,
            self.replica,
            self.sync_time,
            self.app_interface
        )
        # _PASS GUI TO EVENTHANDLER TO SHOW LOGS________________________________
        self.event_handler = EventHandler(self.app_interface)


if __name__ == "__main__":
    app = SyncMeApp()
