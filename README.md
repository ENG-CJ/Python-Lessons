# Python-Lessons
Download Short Lessons About Python 

## Python Snippets

```python

class PDF_VIEWER:
    def __init__(self,root):
        self.root=root
        self.open=Button(self.root,text='open',bg='#1c4b78',fg='#fff',
                         font=('Arial',20),bd=4,width=70,cursor='hand2',
                         command=self.browse_file)
        self.open.pack()

    def browse_file(self):
        self.filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                                 title='Select PDF File',
                                                 filetype=(('PDF FILE','.PDF'),
                                                           ('PDF FILE','.pdf'),
                                                           ('ALL Files','.txt')))
        view1=pdf.ShowPdf()
        view2=view1.pdf_view(root,pdf_location=open(self.filename,'r'),width=990,height=100)
        view2.pack(pady=(0,0))

```

## Interface Snippets

```python
class JUSTLOGIN:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.config(bg='#fff')
        self.root.title('MyJust Login')
        self.root.iconbitmap(r'C:\Users\PC\PycharmProjects\RoomProjects\GUIs Projects\PROJECT\JUSTEXAM_CENTER\images\JAM.ico')

        # img
        self.img_bg=Image.open('images/bg.PNG')
        self.img=ImageTk.PhotoImage(self.img_bg)
        Label(self.root,image=self.img,bg='white',bd=0).place(x=1,y=1)
        
        

```

```python


```
