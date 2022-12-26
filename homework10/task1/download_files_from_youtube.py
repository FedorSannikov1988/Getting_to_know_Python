from pytube import YouTube

def downloading_from_youtube(youtube_video_url: str, flag_for_video: bool, flag_for_audio: bool, name_for_file: str):

    try: 
        yt_object = YouTube(youtube_video_url, use_oauth=True, allow_oauth_cache=True)
        
        for_downloading_video = yt_object.streams.filter(progressive=True).desc().first()
        
        for_downloading_audio = yt_object.streams.filter(only_audio=True).desc().first()
        
        name_for_file_video = name_for_file + "." + \
            str(str(for_downloading_video).replace('"', '').split("video/")[1].split(" ")[0])
        
        name_for_file_audio = name_for_file + "_audio" + "." + \
            str(str(for_downloading_audio).replace('"', '').split("audio/")[1].split(" ")[0])
        
        if flag_for_video:
            for_downloading_video.download(filename = name_for_file_video)
            print('Downloaded Successfully Video')
            
        if flag_for_audio:
            for_downloading_audio.download(filename = name_for_file_audio)
            print('Downloaded Successfully Audio')
    
    except Exception as message:
        print(f"Problem: {message} with url: {youtube_video_url}")

'''
youtube_video_url = "https://www.youtube.com/watch?v=QdabIfmcqSQ"

downloading_from_youtube(youtube_video_url, True, True, "chek")
'''