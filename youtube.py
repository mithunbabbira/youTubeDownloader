import pytube
import tkinter as tk


HEIGHT=400
WIDTH=500




def download(url):
	#url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
	youtube = pytube.YouTube(str(url))
	video = youtube.streams[1]
	video.download('C:/Users/mithu/OneDrive/Desktop/python')
	print('done')

	label['text']= 'len(streams)'


root =tk.Tk()

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()


background_lable = tk.Label(root)
background_lable.place(relwidth=1 , relheight=1)

frame = tk.Frame(root, bg='#9999ff' , bd=5 )
frame.place(relx=0.5,rely=0.1, relwidth=0.75, relheight=0.08 , anchor='n')

entry=tk.Entry(frame , font=('courier',14))
entry.place(relwidth= 0.65 , relheight=1)

button=tk.Button(frame, text="download" , font=40 , command=lambda: download(entry.get()) )
button.place(relx=0.7 , relwidth=0.3, relheight =1)

lower_frame = tk.Frame(root, bg = '#9999ff', bd =10)
lower_frame.place(relx=0.5 , rely = 0.25, relwidth =0.75, relheight =0.65, anchor='n')

label=tk.Label(lower_frame,font=('courier',18))
label.place( relwidth=1 , relheight =1)

root.mainloop()


# video = youtube.streams.get_by_itag(22)
# video.download('C:/Users/mithu/OneDrive/Desktop/python')
# print('done')
# streams = youtube.streams.all()
# for i in streams:
# 	print(itag)
