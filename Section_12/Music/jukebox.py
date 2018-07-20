import sqlite3

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs)
        super().__init__(window, **kwargs)
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspan=rowspan, **kwargs)
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)
        self.cursor = connection.cursor()
        self.linked_box = None
        self.linked_field = None
        self.table = table
        self.ids=[]
        self.field = field
        self.bind('<<ListboxSelect>>', self.on_select)
        self.sort_order = sort_order
        self.sql_select = "SElECT {0}.{1}, {0}._id FROM {0}".format(self.table, self.field)
        if self.sort_order:
            self.sql_sort = " ORDER BY {0}".format(','.join(sort_order))
        else:
            self.sql_sort = " ORDER BY {0}".format(self.field)

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        self.linked_box.linked_field = link_field

    def requery(self, link_value=None):
        if link_value and self.linked_field:
            print(link_value)
            print(self.linked_field)
            sql = self.sql_select + " WHERE " + self.linked_field + "=?" + self.sql_sort
            self.cursor.execute(sql, (link_value,))
        else:
            sql = self.sql_select + self.sql_sort
            self.cursor.execute(sql)

        self.clear()
        self.ids=[]
        if self.linked_box:
            self.linked_box.clear()

        for value in self.cursor:
            self.insert(tkinter.END, value[0])
            self.ids.append(value[1])
    def on_select(self, event):
        if self.linked_box:
            if len(self.curselection()) > 0:
                index = self.curselection()[0]
                value = (self.get(index),)
                sql_statement = self.sql_select + " WHERE " + self.field + "=?"
                self.linked_box.requery(self.ids[index])

if __name__=='__main__':
    conn = sqlite3.connect('music.sqlite')

    mainWindow = tkinter.Tk()
    mainWindow.title('Music DB Browser')
    mainWindow.geometry('1024x768')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)  # spacer column

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # labels
    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # Artists Listbox

    artistList = DataListBox(mainWindow, conn, 'artists', 'name')
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artistList.config(border=2, relief='sunken')

    # for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    #     artistList.insert(tkinter.END, artist[0])
    artistList.requery()

    # Albums Listbox

    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an artist.",))

    albumList = DataListBox(mainWindow, conn, 'albums', 'name', sort_order=("name",), listvariable=albumLV)
    albumList.grid(row=1, column=1, sticky='nsew', rowspan=1, padx=(30, 0))
    albumList.config(border=2, relief='sunken')

    # albumList.bind('<<ListboxSelect>>', get_songs)
    artistList.link(albumList, "artist")
    # Songs Listbox

    songLV = tkinter.Variable(mainWindow)
    songLV.set(("Choose an album.",))

    songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"), listvariable=songLV)
    songList.grid(row=1, column=2, sticky='nsew', rowspan=1, padx=(30, 0))
    songList.config(border=2, relief='sunken')
    albumList.link(songList, "album")
    # Main loop
    albumLV.set(("Select artist",))
    mainWindow.mainloop()
    print("Closing database connection.")
    conn.close()
