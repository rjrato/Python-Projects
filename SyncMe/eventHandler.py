from watchdog.events import FileSystemEventHandler


class EventHandler(FileSystemEventHandler):
    def __init__(self, app_interface, logs_folder):
        self.app_interface = app_interface
        self.logs_folder = logs_folder

    def on_created(self, event):
        create_event = f"File created: {event.src_path}"
        self.app_interface.append_log(message=create_event)
        print(create_event)

        with open(f"{self.logs_folder.get()}/event_log.txt", "a") as output_file:
            output_file.write(create_event + f"\n")

    def on_deleted(self, event):
        delete_event = f"File Deleted: {event.src_path}"
        self.app_interface.append_log(message=delete_event)
        print(delete_event)

        with open(f"{self.logs_folder.get()}/event_log.txt", "a") as output_file:
            output_file.write(delete_event + f"\n")

