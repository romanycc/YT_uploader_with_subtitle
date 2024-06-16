import os

# python upload_video.py --file="test.mov" --title="Test" --subtitle="test.srt"

def list_files_recursively(folder_path):
    count = 0
    for root, dirs, files in os.walk(folder_path):
        file_list = []
        flag = 0
        vflag = 0
        srt = ""
        video = ""
        title = ""
        for file in files:
            flag = 1
            file_list.append(os.path.join(root, file))
            if file[-3:] == "srt":
                srt = os.path.join(root, file)
                file_list.append(srt)
            elif file[-3:] == "mp4":
                vflag = 1
                video = os.path.join(root, file)
                file_list.append(video)
                if len(video[7:])<=100:
                    title = video[7:]
                else:
                    title = video[7:107]
                file_list.append(title)
        if flag==1 and vflag==1:
            secret = "client_secret/client_secret_"+ str(int(count/5)) +".json"
            if srt!="":
                print('"python upload_video.py --file={video} --title={title} --subtitle={srt} --secret={secret}"'.format(video=video, title=title, srt=srt, secret=secret))
            else:
                print('"python upload_video.py --file={video} --title={title} --secret={secret}"'.format(video=video, title=title, secret=secret))
            count = count + 1

    return file_list

# Example usage:
if __name__ == "__main__":
    folder_path = "upload"
    list_files_recursively(folder_path)
