import tkinter as tk
import download_files_from_youtube as d_f_f_y

def start_graphical_interface():
    
    windows = tk.Tk()

    download_video_value = tk.IntVar()
    download_audio_value = tk.IntVar()
    authentication_value = tk.IntVar()
    authentication_once_value = tk.IntVar()

    def show_value_checkbutton():
        print("download_video_value", download_video_value.get())
        print("download_audio_value", download_audio_value.get())
        print("authentication_value", authentication_value.get())
        print("authentication_once_value", authentication_once_value.get())

    def get_url_and_name_download_file():
        show_value_checkbutton()
        url_txt = youtube_video_url.get("1.0",'end-1c')
        name_txt = name_for_download_file.get("1.0",'end-1c')
        if url_txt:
            d_f_f_y.downloading_from_youtube(
                str(url_txt), str(name_txt),\
                     download_video_value.get(), \
                        download_audio_value.get(), \
                            authentication_value.get(), \
                                authentication_once_value.get())
    
    windows.title("Video download application")
    windows.geometry("700x390+600+280")
    windows.resizable(False, False)
    windows.iconphoto(False, tk.PhotoImage(file='icon.png'))

    label_for_url = tk.Label(windows, 
                            text= "Enter URL for download video and audio Youtube", 
                            fg='black',
                            font=('Arial', 15,'bold'))

    label_for_example_url = tk.Label(windows, 
                            text= "Example URL: https://www.youtube.com/watch?v=ХХХХХХХХХХХ", 
                            fg='black',
                            font=('Arial', 9,'bold'))
    
    label_for_name_download_file = tk.Label(windows, 
                            text= "Enter name for download file", 
                            fg='black',
                            font=('Arial', 15,'bold'))

    start_button = tk.Button(windows, 
                            text= "start download",
                            fg='black',
                            font=('Arial', 15,'bold'),
                            command=get_url_and_name_download_file)

    youtube_video_url = tk.Text(windows,
                            width=60, 
                            height=2, 
                            font="Arial 14")

    name_for_download_file = tk.Text(windows,
                            width=45, 
                            height=1, 
                            font="Arial 14")

    flag_for_download_video = tk.Checkbutton(windows,
                            text="Download video",
                            font="Arial 16",
                            variable=download_video_value,
                            offvalue=0,
                            onvalue=1)

    flag_for_download_audio = tk.Checkbutton(windows,
                            text="Download audio",
                            font="Arial 16",
                            variable=download_audio_value,
                            offvalue=0,
                            onvalue=1)
    
    flag_for_authentication = tk.Checkbutton(windows,
                            text="Perform authentication (log in to your account)",
                            font="Arial 16",
                            variable=authentication_value,
                            offvalue=0,
                            onvalue=1)
    
    flag_for_authentication_once = tk.Checkbutton(windows,
                            text="Authentication (log in to your account) only once",
                            font="Arial 16",
                            variable=authentication_once_value,
                            offvalue=0,
                            onvalue=1)
    
    label_for_url.pack()
    label_for_url.place(x=115, y=0)

    label_for_example_url.pack()
    label_for_example_url.place(x=165, y=26)

    youtube_video_url.pack()
    youtube_video_url.place(x=16, y=55)

    label_for_name_download_file.pack()
    label_for_name_download_file.place(x=187, y=110)

    name_for_download_file.pack()
    name_for_download_file.place(x=95, y=145)

    start_button.pack()
    start_button.place(x=245, y=200)

    flag_for_download_video.pack()
    flag_for_download_video.place(x=110, y=270)

    flag_for_download_audio.pack()
    flag_for_download_audio.place(x=350, y=270)

    flag_for_authentication.pack()
    flag_for_authentication.place(x=100, y=305)

    flag_for_authentication_once.pack()
    flag_for_authentication_once.place(x=100, y=335)

    windows.mainloop()