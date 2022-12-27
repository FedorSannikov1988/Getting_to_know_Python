import tkinter as tk
import download_files_from_youtube as d_f_f_y

def start_graphical_interface():
    
    windows = tk.Tk()
    
    def get_url_and_name_download_file():
        url_txt = youtube_video_url.get("1.0",'end-1c')
        name_txt = name_for_download_file.get("1.0",'end-1c')
        if url_txt:
            d_f_f_y.downloading_from_youtube(str(url_txt), str(name_txt), True, True, True, True)
            
    windows.title("Video download application")
    windows.geometry("700x300+600+280")

    label_for_url = tk.Label(windows, 
                            text= "Enter URL for download video and audio Youtube", 
                            fg='black',
                            font=('Arial', 15,'bold'))

    label_for_example_url = tk.Label(windows, 
                            text= "Example URL: https://www.youtube.com/watch?v=ХХХХХХХХХХХ", 
                            fg='black',
                            font=('Arial', 8,'bold'))
    
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
                            width=100, 
                            height=1, 
                            font="Arial 8")

    name_for_download_file = tk.Text(windows,
                            width=45, 
                            height=1, 
                            font="Arial 8")
    
    
    label_for_url.pack()
    label_for_url.place(x=115, y=0)

    label_for_example_url.pack()
    label_for_example_url.place(x=165, y=26)

    youtube_video_url.pack()
    youtube_video_url.place(x=55, y=55)

    label_for_name_download_file.pack()
    label_for_name_download_file.place(x=187, y=90)

    name_for_download_file.pack()
    name_for_download_file.place(x=189, y=140)

    start_button.pack()
    start_button.place(x=245, y=190)

    windows.iconphoto(False, tk.PhotoImage(file='icon.png'))
    windows.mainloop()