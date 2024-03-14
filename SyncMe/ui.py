from tkinter import *
from dirSelect import DirectorySelection
from syncFolders import SyncFolder
from eventHandler import EventHandler

FONT_COLOR = "#031f25"
BACKGROUND_COLOR = "#ffffff"
FONT_NAME = "Verdana"
BUTTON_COLOR_GREEN = "#2a8408"
BUTTON_HOOVERING_COLOR_GREEN = "#83d362"
BUTTON_COLOR_RED = "#D21312"
BUTTON_HOOVERING_COLOR_RED = "#F15A59"


class AppInterface:

    def __init__(self):
        # _______________________________ GUI CONFIG___________________________________________________________________
        self.window = Tk()
        self.window.title("SyncMe")
        self.window.iconbitmap("favicon.ico")
        self.window.config(padx=10, pady=5, bg="white")

        self.title = Label(
            text="SyncMe",
            fg=FONT_COLOR,
            bg=BACKGROUND_COLOR,
            font=(FONT_NAME, 16, "bold")
        )
        self.title.grid(column=0, row=0, columnspan=3)

        self.logo_img = PhotoImage(file="logo.png")
        self.logo = Canvas(width=358, height=231, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.logo.create_image(179, 115, image=self.logo_img)
        self.logo.grid(column=0, row=1, pady=5, columnspan=3)

        self.source_folder_label = Label(
            text="Source Folder",
            fg=FONT_COLOR,
            bg=BACKGROUND_COLOR,
            font=(FONT_NAME, 12, "bold")
        )

        self.source_folder_entry = Entry(width=60, borderwidth=2)

        self.source_folder_select = DirectorySelection(
            source_folder_entry=self.source_folder_entry
        )

        self.source_folder_dir = Button(
            width=10,
            text="Select",
            fg=BACKGROUND_COLOR,
            bg=BUTTON_COLOR_GREEN,
            font=(FONT_NAME, 10, "normal"),
            command=self.source_folder_select.source_folder
        )

        self.replica_folder_label = Label(
            text="Replica Folder",
            fg=FONT_COLOR,
            bg=BACKGROUND_COLOR,
            font=(FONT_NAME, 12, "bold")
        )

        self.replica_folder_entry = Entry(width=60, borderwidth=2)

        self.replica_folder_select = DirectorySelection(
            replica_folder_entry=self.replica_folder_entry
        )

        self.replica_folder_dir = Button(
            width=10,
            text="Select",
            fg=BACKGROUND_COLOR,
            bg=BUTTON_COLOR_GREEN,
            font=(FONT_NAME, 10, "normal"),
            command=self.replica_folder_select.replica_folder
        )

        self.logs_folder_label = Label(
            text="Logs Folder",
            fg=FONT_COLOR,
            bg=BACKGROUND_COLOR,
            font=(FONT_NAME, 12, "bold")
        )

        self.logs_folder_entry = Entry(width=60, borderwidth=2)

        self.logs_folder_select = DirectorySelection(
            logs_folder_entry=self.logs_folder_entry
        )

        self.logs_folder_dir = Button(
            width=10,
            text="Select",
            fg=BACKGROUND_COLOR,
            bg=BUTTON_COLOR_GREEN,
            font=(FONT_NAME, 10, "normal"),
            command=self.logs_folder_select.logs_folder
        )

        self.logs_folder_select = EventHandler(
            logs_folder=self.logs_folder_entry,
            app_interface=self
        )

        self.sync_time_label = Label(
            text="Sync Time",
            fg=FONT_COLOR,
            bg=BACKGROUND_COLOR,
            font=(FONT_NAME, 12, "bold")
        )

        self.sync_time_entry = Entry(width=10, borderwidth=2)

        self.sync_folder = SyncFolder(
            source_folder_entry=self.source_folder_entry,
            replica_folder_entry=self.replica_folder_entry,
            logs_folder_entry=self.logs_folder_entry,
            sync_time_entry=self.sync_time_entry,
            app_interface=self
        )

        self.sync_button = Button(
            width=15,
            text="Sync Folders",
            fg=BACKGROUND_COLOR,
            bg=BUTTON_COLOR_GREEN,
            font=(FONT_NAME, 12, "bold"),
            pady=10,
            command=self.start_sync
        )

        self.is_sync_active = False

        self.log_output = Text(
            self.window,
            width=75,
            height=10,
            bg=FONT_COLOR,
            fg=BACKGROUND_COLOR,
            state="disabled",
            wrap="word"
        )

        self.source_folder_label.grid(column=0, row=2, sticky="e")
        self.source_folder_entry.grid(column=1, row=2, padx=10, sticky="w")
        self.source_folder_dir.grid(column=2, row=2, padx=10, pady=2, sticky="e")
        self.replica_folder_label.grid(column=0, row=3, sticky="e")
        self.replica_folder_entry.grid(column=1, row=3, padx=10, sticky="w")
        self.replica_folder_dir.grid(column=2, row=3, padx=10, pady=2, sticky="e")
        self.logs_folder_label.grid(column=0, row=4, sticky="e")
        self.logs_folder_entry.grid(column=1, row=4, padx=10, sticky="w")
        self.logs_folder_dir.grid(column=2, row=4, padx=10, pady=2, sticky="e")
        self.sync_time_label.grid(column=0, row=5, sticky="e")
        self.sync_time_entry.grid(column=1, row=5, padx=10, pady=2, sticky="w")
        self.sync_button.grid(column=0, row=6, columnspan=3, pady=10)

        # _______________________________ BUTTON HOOVERING____________________________________________________________

        def source_folder_on_enter(e):
            self.source_folder_dir.config(background=BUTTON_HOOVERING_COLOR_GREEN, foreground=BACKGROUND_COLOR)

        def source_folder_on_leave(e):
            self.source_folder_dir.config(background=BUTTON_COLOR_GREEN, foreground=BACKGROUND_COLOR)

        def replica_folder_dir_on_enter(e):
            self.replica_folder_dir.config(background=BUTTON_HOOVERING_COLOR_GREEN, foreground=BACKGROUND_COLOR)

        def replica_folder_dir_on_leave(e):
            self.replica_folder_dir.config(background=BUTTON_COLOR_GREEN, foreground=BACKGROUND_COLOR)

        def logs_folder_on_enter(e):
            self.logs_folder_dir.config(background=BUTTON_HOOVERING_COLOR_GREEN, foreground=BACKGROUND_COLOR)

        def logs_folder_on_leave(e):
            self.logs_folder_dir.config(background=BUTTON_COLOR_GREEN, foreground=BACKGROUND_COLOR)

        def sync_button_on_enter(e):
            if self.sync_button["background"] == BUTTON_COLOR_GREEN:
                self.sync_button.config(background=BUTTON_HOOVERING_COLOR_GREEN, foreground=BACKGROUND_COLOR)
            else:
                self.sync_button.config(background=BUTTON_HOOVERING_COLOR_RED, foreground=BACKGROUND_COLOR)

        def sync_button_on_leave(e):
            if self.sync_button["background"] == BUTTON_HOOVERING_COLOR_GREEN:
                self.sync_button.config(background=BUTTON_COLOR_GREEN, foreground=BACKGROUND_COLOR)
            else:
                self.sync_button.config(background=BUTTON_COLOR_RED, foreground=BACKGROUND_COLOR)

        self.source_folder_dir.bind("<Enter>", source_folder_on_enter)
        self.source_folder_dir.bind("<Leave>", source_folder_on_leave)
        self.replica_folder_dir.bind("<Enter>", replica_folder_dir_on_enter)
        self.replica_folder_dir.bind("<Leave>", replica_folder_dir_on_leave)
        self.logs_folder_dir.bind("<Enter>", logs_folder_on_enter)
        self.logs_folder_dir.bind("<Leave>", logs_folder_on_leave)
        self.sync_button.bind("<Enter>", sync_button_on_enter)
        self.sync_button.bind("<Leave>", sync_button_on_leave)

        self.window.mainloop()

    def start_sync(self):

        if self.is_sync_active:

            self.stop_sync()
            self.sync_button.config(text="Sync Folders", bg=BUTTON_HOOVERING_COLOR_GREEN)

        else:

            if self.sync_folder.start_monitoring():

                self.sync_folder.sync_folders()
                self.is_sync_active = True
                self.sync_button.config(text="Stop Sync", bg=BUTTON_HOOVERING_COLOR_RED)
                self.log_output.config(state="normal")
                self.log_output.insert(INSERT, "Synchronization started\n")
                self.log_output.grid(column=0, row=7, columnspan=3, pady=5, padx=10)

            else:

                self.log_output.config(state="normal")
                self.log_output.insert(INSERT, "Synchronization cannot continue. Please provide the required missing fields.\n")
                self.log_output.grid(column=0, row=7, columnspan=3, pady=5, padx=10)

    def stop_sync(self):
        self.is_sync_active = False
        self.sync_folder.stop_monitoring()
        self.log_output.config(state="normal")
        self.log_output.insert(INSERT, "Synchronization stopped by user.\n")

    def append_log(self, message):
        self.log_output.config(state="normal")
        self.log_output.insert(END, message + "\n")
        self.log_output.config(state="disabled")
        self.log_output.see(END)
