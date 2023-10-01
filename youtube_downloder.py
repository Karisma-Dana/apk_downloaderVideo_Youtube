import tkinter as tk 
from pytube import YouTube
from tkinter import messagebox 
import pyperclip 
import threading



def paste_text(): 
    paste = pyperclip.paste()
    user_link.insert(tk.END,paste)


def download_video():
    #import urf from entry
    url = user_link.get()
   

    if not url : 
        messagebox.showerror("Error","URL cannot be empty")
        return
    
        
    #eksekusi download 
    try: 
        ytb = YouTube(url)
        #resolusi youtube 
        stream = ytb.streams.get_highest_resolution()

        def download_withLoading(): 
            eksekusi.config(state=tk.DISABLED)
            loading_label.config(text="Dowloading...",font=("Helvetica",12))
            for _ in stream.download(output_path="download"): 
                pass 
            messagebox.showinfo("Download Complete", "Video downloaded successfully.")
            loading_label.config(text="")
            eksekusi.config(state=tk.NORMAL)

        download_execution = threading.Thread(target=download_withLoading)
        download_execution.start()


    except Exception as e : 
        messagebox.showerror("Error",f"An eror occurred: {str(e)}")
        
     

#jendela utama dari tkinter 
root = tk.Tk()
root.title("youtube downloader")
root.geometry("250x170")
root.resizable(False,False)

#isi dari jendela tkinter 
label1 = tk.Label(root,text="gift me your link youtube")
label1.pack()

user_link = tk.Entry(root)
user_link.pack()

title_video = tk.Entry(root)
title_video.pack
button_paste = tk.Button(root,text="paste",command=paste_text)
button_paste.pack(padx=5,pady=5)

#button eksekusi 
eksekusi = tk.Button(root,text="download",command=download_video)
eksekusi.pack(padx=7,pady=5)
loading_label = tk.Label(root,text="",font=("Helvetica", 12))
loading_label.pack()


root.mainloop()















