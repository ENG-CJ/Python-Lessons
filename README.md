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

## JQUERY Snippets
```javaScript

$('document').ready(()=>{

    // we make two function add and remove 

    function add_class(){
        $('.copied').addClass('bounceIn')
    };

    function remove_class(){
        $('.copied').removeClass('bounceIn')
    };

    // calling functions
    $('#copy-btn').click(()=>{
        $('#text-field').select();
        document.execCommand('copy')
        add_class();
        setTimeout(remove_class,900)
    })
})
```
