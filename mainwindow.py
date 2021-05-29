import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import login
import storage


class mainwindow():

    def reback(self):
        self.initface.destroy()
        login.login(self.root)



    def print(self):
        x=self.tree.get_children()
        for i in x:
            self.tree.delete(i)
        for i in range(len(self.a.full)):
            t = self.a.full[i]
            self.tree.insert("", i, text=" ", values=(" "+str(t.id), " "+str(t.begin)," "+str(t.end)," "+str(t.length), "   已分配"))
        self.tree.insert("", len(self.a.full)+1, text=" ",values=(" " + "=======", "" + "=======", "=======", " "+"=======", "======="))
        for i in range(len(self.a.empty)):
            t = self.a.empty[i]
            self.tree.insert("", i + len(self.a.full) + 2, values=(" "+str(t.id), " "+str(t.begin)," "+str(t.end)," "+str(t.length), "   未分配"))
        self.tree.pack(side=BOTTOM)
        return

    def allocate(self):
        begin=int(self.e1.get())
        length=int(self.e2.get())
        flag=self.a.allocate(begin,length)
        if flag:
            tkinter.messagebox.showinfo('提示','分配成功')
        else:
            tkinter.messagebox.showinfo('提示', '分配失败')
        self.print()

    def recycle(self):
        id=int(self.e3.get())
        flag=self.a.recycle(id)
        if flag:
            tkinter.messagebox.showinfo('提示','回收成功')
        else:
            tkinter.messagebox.showinfo('提示', '回收失败')
        self.print()
    def __init__(self, master):
        self.root = master
        self.root.title('管理')
        self.initface = Frame(self.root, )
        self.initface.pack()
        self.a = storage.Storage()
        lb1 = Label(self.initface, text='分配：')
        lb1.grid(row=2, column=1, padx=5)
        lb2 = Label(self.initface, text='始址')
        lb2.grid(row=1, column=2, padx=5)
        lb3 = Label(self.initface, text='长度')
        lb3.grid(row=1, column=3, padx=5)
        self.e1 = Entry(self.initface, width=14)
        self.e1.grid(row=2, column=2, padx=5)
        self.e2 = Entry(self.initface, width=14)
        self.e2.grid(row=2, column=3, padx=5)
        btnsure1 = Button(self.initface, text='确认', fg='black', font=('黑体', 9), command=self.allocate)
        btnsure1.grid(row=2, column=4, padx=5)

        lb4 = Label(self.initface, text='回收:')
        lb4.grid(row=5, column=1, padx=5)
        lb5 = Label(self.initface, text='分区id')
        lb5.grid(row=4, column=2, padx=5)
        self.e3 = Entry(self.initface, width=14)
        self.e3.grid(row=5, column=2, padx=5)
        btnsure2 = Button(self.initface, text='确认', fg='black', font=('黑体', 9),command=self.recycle)
        btnsure2.grid(row=5, column=3, padx=5)

        columns = (("分区id", "始址","末址", "长度", "分配情况"))
        self.tree = ttk.Treeview(self.root, height=22, show="headings", columns=columns)  # #创建表格对象
        self.tree.column("分区id", width=80)  # #设置列
        self.tree.column("始址", width=80)
        self.tree.column("末址", width=80)
        self.tree.column("长度", width=80)
        self.tree.column("分配情况", width=80)
        self.tree.heading("分区id", text="分区id")  # #设置显示的表头名
        self.tree.heading("始址", text="始址")
        self.tree.heading("末址", text="末址")
        self.tree.heading("长度", text="长度")
        self.tree.heading("分配情况", text="分配情况")
        self.print()