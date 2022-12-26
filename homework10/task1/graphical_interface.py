import tkinter as tk
import download_files_from_youtube as d_f_f_y

def start_graphical_interface():
    
    windows = tk.Tk()
    
    def get_text():
        value = youtube_video_url.get("1.0",'end-1c')
        if value:
            print(value)
            d_f_f_y.downloading_from_youtube(str(value), True, True, "chek")
        else:
            print("Emptry Entry")
            
    windows.title("Video download application")
    windows.geometry("700x200+600+280")

    label_for_url = tk.Label(windows, 
                            text= "Youtube video URL:", 
                            fg='black',
                            font=('Arial', 15,'bold'))

    start_button = tk.Button(windows, 
                            text= "start download",
                            fg='black',
                            font=('Arial', 15,'bold'),
                            command=get_text)

    youtube_video_url = tk.Text(windows, 
                                height=1, 
                                font="Arial 8")

    label_for_url.pack()
    youtube_video_url.pack()
    start_button.pack()

    windows.mainloop()