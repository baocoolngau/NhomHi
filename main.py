# from tkinter import *
# from tkinter import ttk
# from pymongo import MongoClient
# from tkinter import messagebox as mesbox
# # import PIL
# # # from tkinter import Frame, Tk, Menu
# win = Tk()
# myclient = MongoClient("mongodb://localhost:27017/")
# mydb = myclient["QL_KTX"]
# mycol = mydb["QL_SV"]
# mycol1 = mydb["QL_PHONG"]
# mycol2 = mydb["QL_HD"]
# mycol3 = mydb["QL_HDDN"]
# color1="#FFC000"
# color2="#00B050"
# color3="#0070C0"
# class QL_sinhvien():
#     #tạo màn hình tìm kiếm sinh viên
#     def QLSV_window(self):
#         student = Tk()
#         student.title("QLKTX_Quản lý sinh viên")
#         student.geometry('920x480')
#         student.resizable(False, False)  # không cho thay đổi kích thước ,make sure dont resize the window
#         frame1 = Frame(student, bg="white", relief="ridge", borderwidth=2)
#         frame1.place(x=0, y=0, width=100, height=480)
#
#         self.btn_st = Button(frame1, bg='{0}'.format(color1), text="SINH VIÊN", font="Andalus 10 bold",
#                              fg="white")
#         self.btn_room = Button(frame1, bg='{0}'.format(color2), text="PHÒNG Ở", font="Andalus 10 bold",
#                                fg="white", command=self.QL_phong_window)
#         self.btn_bill = Button(frame1, bg='{0}'.format(color3), text="HÓA ĐƠN", font="Andalus 10 bold",
#                                fg="white", command=self.QLHD_window)
#
#         self.btn_st.place(x=10, y=10, width=80, height=80)
#         self.btn_room.place(x=10, y=100, width=80, height=80)
#         self.btn_bill.place(x=10, y=190, width=80, height=80)
#
#         frame_top = Frame(student, bg="gray")
#         frame_find = Frame(student, bg='{0}'.format(color1),relief="ridge",borderwidth=2)
#         frame_info_st = Frame(student, relief="ridge",borderwidth=2)
#         frame_update_add_student = Frame(student, bg='{0}'.format(color3), borderwidth=2,relief="ridge")
#         frame_botton = Frame(student, bg="gray")
#         frame_top.place(x=101, y=0, width=810, height=40)
#         frame_find.place(x=101, y=41, width=450, height=160)
#         frame_info_st.place(x=101, y=201, width=450, height=190)
#         frame_update_add_student.place(x=561, y=41, width=350, height=340)
#         frame_botton.place(x=101, y=393, width=810, height=85)
#         # frame_find.place(x=150, y=20)
#         self.entry_mssv = Entry(frame_find, width=20, borderwidth=1)
#         self.entry_mssv.place(x=20, y =27)
#         label_mssv = Label(frame_find, text="Mssv",highlightthickness=1, highlightbackground="green")
#         label_mssv.place(x=20, y=4)
#         self.entry_name = Entry(frame_find, width=30, borderwidth=1)
#         self.entry_name.place(x=180, y=27)
#         label_name = Label(frame_find, text="Họ tên",highlightthickness=1, highlightbackground="green")
#         label_name.place(x=180, y=4)
#         self.entry_school = Entry(frame_find, width=40, borderwidth=1)
#         self.entry_school.place(x=20, y=116)
#         label_school = Label(frame_find, text="Trường",highlightthickness=1, highlightbackground="green")
#         label_school.place(x=20, y=93)
#         self.entry_toa = Entry(frame_find, width=10, borderwidth=1)
#         self.entry_toa.place(x=20, y=72)
#         label_toa = Label(frame_find, text="Tòa",highlightthickness=1, highlightbackground="green")
#         label_toa.place(x=20, y=49)
#         self.entry_phong = Entry(frame_find, width=10,borderwidth=1)
#         self.entry_phong.place(x=180, y=72)
#         label_phong = Label(frame_find, text="Phòng",highlightthickness=1, highlightbackground="green")
#         label_phong.place(x=180, y=49)
#         self.search_ST = Button(frame_find, width=8, text="Search", bg="green", fg="white", font="Andalus 10 bold")
#         self.search_ST.configure(command=self.find_student)
#         self.search_ST.place(x=340, y=120)
#         label_list = Label(frame_info_st, text="DANH SÁCH SINH VIÊN", font="Andalus 12 bold", fg="blue")
#         label_list.place(x=0, y=0, width=447, height=30)
#         columns =('Mssv','Trường','Họ tên', 'Giới tính', 'Ngày sinh', 'Cccd', 'Tòa','Phòng')
#         self.tree = ttk.Treeview(frame_info_st, columns=columns, show='headings')
#         self.tree.heading('Mssv', text="Mssv")
#         self.tree.heading('Trường', text="Trường")
#         self.tree.heading('Họ tên', text="Họ tên")
#         self.tree.heading('Giới tính', text="Giới tính")
#         self.tree.heading('Ngày sinh', text="Ngày sinh")
#         self.tree.heading('Cccd', text="Cccd")
#         self.tree.heading('Tòa', text="Tòa")
#         self.tree.heading('Phòng', text="Phòng")
#         self.tree.column('Mssv',width=100)
#         self.tree.column('Trường', width=150)
#         self.tree.column('Họ tên', width=118)
#         self.tree.column('Giới tính',width=60)
#         self.tree.column('Ngày sinh', width=100)
#         self.tree.column('Cccd',width=100)
#         self.tree.column('Tòa', width=50)
#         self.tree.column('Phòng',width=60)
#         self.tree.place(x=0, y=30, width=448, height=140)
#         scrollbar = ttk.Scrollbar(frame_info_st, orient=VERTICAL, command=self.tree.yview)
#         self.tree.configure(yscrollcommand=scrollbar.set)
#         scrollbar.place(x=430, y=31, height=138)
#         scrollbar1 = ttk.Scrollbar(frame_info_st, orient=HORIZONTAL, command=self.tree.xview)
#         self.tree.configure(xscrollcommand=scrollbar1.set)
#         scrollbar1.place(x=0, y=170, width=447)
#         label_info = Label(frame_update_add_student, text="THÔNG TIN SINH VIÊN CHI TIẾT", fg="green", font="Andalus 12 bold")
#         label_info.place(x=10, y=10)
#         label_mssv = Label(frame_update_add_student, text="Mã số sinh viên:")
#         label_mssv.place(x=10, y=50)
#         self.entry_mssv1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         self.entry_mssv1.place(x=150, y=50)
#         label_school = Label(frame_update_add_student, text="Trường:")
#         label_school.place(x=10, y=80)
#         self.entry_school1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         self.entry_school1.place(x=150, y=80)
#         label_name = Label(frame_update_add_student, text="Họ và tên:")
#         label_name.place(x=10, y=110)
#         self.entry_name1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         self.entry_name1.place(x=150, y=110)
#         label_gender = Label(frame_update_add_student, text="Giới tính:")
#         label_gender.place(x=10, y=140)
#         self.entry_gender1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         self.entry_gender1.place(x=150, y=140)
#         label_dob = Label(frame_update_add_student, text="Ngày sinh:")
#         label_dob.place(x=10, y=170)
#         self.entry_dob1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         self.entry_dob1.place(x=150, y=170)
#         label_cccd = Label(frame_update_add_student, text="Số CCCD:")
#         label_cccd.place(x=10, y=200)
#         self.entry_cccd1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         self.entry_cccd1.place(x=150, y=200)
#         label_building = Label(frame_update_add_student, text="Tòa:")
#         label_building.place(x=10, y=230)
#         self.entry_building1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         self.entry_building1.place(x=150, y=230)
#         label_room = Label(frame_update_add_student, text="Phòng:")
#         label_room.place(x=10, y=260)
#         self.entry_room1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         self.entry_room1.place(x=150, y=260)
#         update_ST = Button(frame_update_add_student, width=9, text="Cập nhật", bg="green", fg="white", font="Arial 10 bold", command=self.update_student)
#         update_ST.place(x=260, y=300)
#         delete_ST = Button(frame_update_add_student, width=9, text="Xóa SV", bg="green", fg="white",
#                            font="Arial 10 bold", command=self.delete_st)
#         delete_ST.place(x=170, y=300)
#         add_ST = Button(frame_update_add_student, width=9, text="Thêm SV", bg="green", fg="white",
#                            font="Arial 10 bold", command=self.add_ST)
#         add_ST.place(x=80, y=300)
#
#     def find_student(self):
#         x = 0
#         while x == 0:
#             self.entry_mssv1.delete(0, END)
#             self.entry_school1.delete(0, END)
#             self.entry_name1.delete(0, END)
#             self.entry_gender1.delete(0, END)
#             self.entry_dob1.delete(0, END)
#             self.entry_cccd1.delete(0, END)
#             self.entry_building1.delete(0, END)
#             self.entry_room1.delete(0, END)
#             for i in self.tree.get_children():
#                 self.tree.delete(i)
#             rows = mycol.find()
#             for row in rows:
#                 mssv=row['Mssv'].encode('utf-8').decode('utf-8')
#                 truong=row['Trường'].encode('utf-8').decode('utf-8')
#                 hoten=row['Họ tên'].encode('utf-8').decode('utf-8')
#                 gioitinh=row['Giới tính'].encode('utf-8').decode('utf-8')
#                 ngaysinh=row['Ngày sinh'].encode('utf-8').decode('utf-8')
#                 cccd=row['Cccd'].encode('utf-8').decode('utf-8')
#                 toa=row['Tòa'].encode('utf-8').decode('utf-8')
#                 phong=row['Phòng'].encode('utf-8').decode('utf-8')
#                 if ((len(self.entry_mssv.get()) == 0 or self.entry_mssv.get() == mssv)
#                         and (len(self.entry_name.get()) == 0 or self.entry_name.get() == hoten)
#                         and (len(self.entry_school.get()) == 0 or self.entry_school.get() == truong)
#                         and (len(self.entry_toa.get()) == 0 or self.entry_toa.get() == toa)
#                         and (len(self.entry_phong.get()) == 0 or self.entry_phong.get() == phong)):
#                     self.tree.insert("", END, values=(mssv, truong,hoten,gioitinh,ngaysinh,cccd,toa,phong))
#                     x = x + 1
#                 if (((len(self.entry_mssv.get()) == 0 or self.entry_mssv.get() == mssv)
#                     and (self.entry_name.get() == hoten)
#                 or ((self.entry_mssv.get() == mssv)
#                     and (len(self.entry_name.get()) == 0 or self.entry_name.get() == hoten)))
#                 ):
#                     self.entry_mssv1.insert(0,mssv)
#                     self.entry_school1.insert(0, truong)
#                     self.entry_name1.insert(0, hoten)
#                     self.entry_gender1.insert(0, gioitinh)
#                     self.entry_dob1.insert(0, ngaysinh)
#                     self.entry_cccd1.insert(0, cccd)
#                     self.entry_building1.insert(0, toa)
#                     self.entry_room1.insert(0,phong)
#                     x=x+1
#
#             break
#
#         if x == 0:
#             mesbox.showwarning("Notification", "No student found")
#             self.entry_mssv1.delete(0, END)
#             self.entry_school1.delete(0, END)
#             self.entry_name1.delete(0, END)
#             self.entry_gender1.delete(0, END)
#             self.entry_dob1.delete(0, END)
#             self.entry_cccd1.delete(0, END)
#             self.entry_building1.delete(0, END)
#             self.entry_room1.delete(0, END)
#     def update_student(self):
#         if len(self.entry_mssv.get())==0:
#             myquery = {"Họ tên":self.entry_name.get()}
#         elif len(self.entry_name.get()) == 0:
#             myquery = {"Mssv": self.entry_mssv.get()}
#         elif ((not len(self.entry_mssv.get())==0) and (not len(self.entry_name.get()) == 0)):
#             myquery = {"Mssv": self.entry_mssv.get(),"Họ tên": self.entry_name.get()}
#             record = list(mycol.find_one(myquery).values())[1:9]
#         newvalues = {"$set":{"Mssv": self.entry_mssv1.get(),
#                              "Trường":self.entry_school1.get(),
#                              "Họ tên":self.entry_name1.get(),
#                              "Giới tính":self.entry_gender1.get(),
#                              "Ngày sinh":self.entry_dob1.get(),
#                              "Cccd":self.entry_cccd1.get(),
#                              "Tòa":self.entry_building1.get(),
#                              "Phòng":self.entry_room1.get()}}
#         mycol.update_one(myquery,newvalues)
#         mesbox.showwarning("Notification", "Cập nhật thành công")
#     def add_ST(self):
#         global win
#         mssv = self.entry_mssv1.get()
#         school = self.entry_school1.get()
#         name = self.entry_name1.get()
#         gender = self.entry_gender1.get()
#         dob = self.entry_dob1.get()
#         Cccd = self.entry_cccd1.get()
#         building = self.entry_building1.get()
#         room = self.entry_room1.get()
#         if (len(mssv) == 0 or len(school) == 0 or len(name) == 0 or len(gender) == 0 or len(dob) == 0 or len(Cccd) == 0 or len(building) == 0 or len(room) == 0):
#             mesbox.showwarning("WARNING", "Vui lòng nhập đủ thông tin")
#             return
#         else:
#             for row in mycol.find():
#                 if row['Mssv'].encode('utf-8').decode('utf-8') == mssv:
#                     mesbox.showwarning("ERROR", "Mã số sinh viên đã tồn tại")
#                     return
#         mycol.insert_one(
#             {'Mssv': mssv, 'Trường': school, 'Họ tên': name, 'Giới tính': gender, 'Ngày sinh': dob, 'Cccd': Cccd,
#              'Tòa': building, 'Phòng': room})
#         mesbox.showinfo("Add Student", "Student Added")
#     def delete_st(self):
#         if mesbox.askokcancel("Xác nhận","Xóa sinh viên khỏi danh sách ?"):
#              mycol.delete_one({"Mssv":self.entry_mssv1.get()})
#              mesbox.showinfo("Thông báo", "Xóa thành công")
#
# class QL_phong():
#     def QL_phong_window(self):
#         self.room = Tk()
#         self.room.title("QLKTX_Quản lý phòng ở")
#         self.room.geometry('900x460')
#         self.room.resizable(False, False)  # không cho thay đổi kích thước ,make sure dont resize the window
#         self.frame1 = Frame(self.room, bg="white", relief="ridge", borderwidth=2)
#         self.frame1.place(x=0, y=0, width=100, height=480)
#
#         self.btn_st = Button(self.frame1, bg='{0}'.format(color1), text="SINH VIÊN", font="Andalus 10 bold",
#                              fg="white", command=self.QLSV_window)
#         self.btn_room = Button(self.frame1, bg='{0}'.format(color2), text="PHÒNG Ở", font="Andalus 10 bold",
#                                fg="white")
#         self.btn_bill = Button(self.frame1, bg='{0}'.format(color3), text="HÓA ĐƠN", font="Andalus 10 bold",
#                                fg="white", command=self.QLHD_window)
#
#         self.btn_st.place(x=10, y=10, width=80, height=80)
#         self.btn_room.place(x=10, y=100, width=80, height=80)
#         self.btn_bill.place(x=10, y=190, width=80, height=80)
#
#         self.frame_top = Frame(self.room, bg="gray")
#         self.frame_room = Frame(self.room, bg='{0}'.format(color2),relief="ridge",borderwidth=2)
#         self.frame_info_st = Frame(self.room, bg='gray',relief="ridge",borderwidth=2)
#         self.frame_info_room = Frame(self.room, bg='{0}'.format(color3),relief="ridge",borderwidth=2)
#         self.frame_bottom = Frame(self.room, bg="gray")
#
#         self.frame_top.place(x=101, y=5, width=797, height=35)
#         self.frame_room.place(x=101, y=41, width=390, height=160)
#         self.frame_info_st.place(x=101, y=201, width=398, height=173)
#         self.frame_info_room.place(x=501, y=41, width=397, height=300)
#         self.frame_bottom.place(x=101, y=375, width=797, height=70)
#
#         self.entry_building1 = Entry(self.frame_room, width=10)
#         self.entry_building1.place(x=50, y=20)
#         label_entry_building = Label(self.frame_room, text="Tòa", font="Andalus 10 bold", bg="white").place(x=10, y=20)
#         self.entry_room1 = Entry(self.frame_room, width=10)
#         self.entry_room1.place(x=260, y=20)
#         label_entry_building = Label(self.frame_room, text="Phòng", font="Andalus 10 bold", bg="white").place(x=200,
#                                                                                                             y=20)
#         options_tt =["","Tốt","Cần sửa chữa"]
#         self.entry_TT = ttk.Combobox(self.frame_room, values=options_tt,width=15)
#         self.entry_TT.place(x=100, y=80)
#         label_entry_TT = Label(self.frame_room, text="Trình trạng", font="Andalus 10 bold", bg="white").place(x=10, y=80)
#         self.Search_BT = Button(self.frame_room, text="Search",width=8,font="Andalus 12 bold",bg="blue", fg="white", command=self.find_room)
#         self.Search_BT.place(x=270, y=110)
#
#
#
#         self.lbl_st = Label(self.frame_info_st, text="DANH SÁCH PHÒNG", font="Andalus 12 bold", fg="blue").place(
#             x=0, y=0, width=394, height=30)
#         self.columns = ('Tòa','Phòng', 'Số giường','Số bàn ghế','Tình trạng')
#         self.tv = ttk.Treeview(self.frame_info_st, columns = self.columns,show='headings')
#         self.tv.column('#0', width=0, stretch=NO)
#         self.tv.column('#1', anchor=CENTER, width=40)
#         self.tv.column('#2', anchor=CENTER, width=70)
#         self.tv.column('#3', anchor=CENTER, width=80)
#         self.tv.column('#4', anchor=CENTER, width=80)
#         self.tv.column('#5', anchor=CENTER, width=90)
#
#         self.tv.heading('#0', text='', anchor=CENTER)
#         self.tv.heading('Tòa', text='Tòa', anchor=CENTER)
#         self.tv.heading('Phòng', text='Phòng', anchor=CENTER)
#         self.tv.heading('Số giường', text='Số giường', anchor=CENTER)
#         self.tv.heading('Số bàn ghế', text='Số bàn ghế', anchor=CENTER)
#         self.tv.heading('Tình trạng', text='Tình trạng', anchor=CENTER)
#         self.tv.place(x=0, y=30, width=390, height=140)
#         scrollbar = ttk.Scrollbar(self.frame_info_st, orient=VERTICAL, command=self.tv.yview)
#         self.tv.configure(yscroll=scrollbar.set)
#         scrollbar.place(x=375, y=31, height=138)
#         self.name = StringVar()
#         self.dob = DoubleVar()
#         self.uni = StringVar()
#         self.lbl_title = Label(self.frame_info_room, text="THÔNG TIN PHÒNG CHI TIẾT", font="Andalus 12 bold", fg="blue").grid(row=1,
#                                                                                                       column=0,
#                                                                                                       padx=5,
#                                                                                                       pady=5)
#         self.lbl_toa = Label(self.frame_info_room, text="Tòa", width=20, font="Andalus 12").grid(row=2,
#                                                                                                             column=0,
#                                                                                                             padx=5,
#                                                                                                             pady=5)
#         self.lbl_phong = Label(self.frame_info_room, text="Phòng", width=20, font="Andalus 12").grid(row=3,
#                                                                                                            column=0,
#                                                                                                            padx=5,
#                                                                                                            pady=5)
#         self.lbl_soGiuong = Label(self.frame_info_room, text="Số giường", width=20, font="Andalus 12").grid(row=4,
#                                                                                                             column=0,
#                                                                                                             padx=5,
#                                                                                                             pady=5)
#         self.lbl_banGhe = Label(self.frame_info_room, text="Số bàn ghế", width=20, font="Andalus 12").grid(row=5,
#                                                                                                            column=0,
#                                                                                                            padx=5,
#                                                                                                            pady=5)
#         self.lbl_choTrong = Label(self.frame_info_room, text="Số giường trống", width=20, font="Andalus 12").grid(row=6,
#                                                                                                             column=0,
#                                                                                                             padx=5,
#                                                                                                             pady=5)
#         self.lbl_status = Label(self.frame_info_room, text="Tình trạng", width=20, font="Andalus 12").grid(row=7,
#                                                                                                                   column=0,
#                                                                                                                   padx=5,
#                                                                                                                   pady=5)
#         self.output_toa = Label(self.frame_info_room, width=5, font="Andalus 12")
#         self.output_phong = Label(self.frame_info_room, width=5, font="Andalus 12")
#         self.entry_numberSG = Entry(self.frame_info_room, width=5, font="Andalus 12")
#         self.entry_numberBG = Entry(self.frame_info_room,  width=5, font="Andalus 12")
#         self.entry_status = Entry(self.frame_info_room, width=12, font="Andalus 9")
#         self.lbl_numberCTr = Label(self.frame_info_room, text=" ", width=5, font="Andalus 12")
#         self.output_toa.grid(row=2, column=1)
#         self.output_phong.grid(row=3, column=1)
#         self.entry_numberSG.grid(row=4, column=1)
#         self.entry_numberBG.grid(row=5, column=1)
#         self.entry_status.grid(row=7,column=1)
#         self.lbl_numberCTr.grid(row=6, column=1)
#         self.btn_update = Button(self.frame_info_room, text="Update", bg="green", width=10, font='Andalus 12 bold',fg="white",command=self.update).place(x=270,y=250)
#         self.tv.bind('<ButtonRelease-1>')
#
#     def find_room(self):
#         x = 0
#         y = 0
#         while x == 0:
#             self.entry_numberSG.delete(0, END)
#             self.entry_numberBG.delete(0, END)
#             self.entry_status.delete(0, END)
#             for i in self.tv.get_children():
#                 self.tv.delete(i)
#             rows = mycol.find()
#             rows1 = mycol1.find()
#             self.output_toa['text']=""
#             self.output_phong['text'] = ""
#             self.lbl_numberCTr['text'] = ""
#             for row in rows:
#                 toa=row['Tòa'].encode('utf-8').decode('utf-8')
#                 phong=row['Phòng'].encode('utf-8').decode('utf-8')
#                 K=self.entry_building1.get()
#                 H=self.entry_room1.get()
#                 if K == toa and H == phong:
#                     x = x + 1
#             for row in rows1:
#                 toa = row['Tòa'].encode('utf-8').decode('utf-8')
#                 phong = row['Phòng'].encode('utf-8').decode('utf-8')
#                 SG = row['Số giường'].encode('utf-8').decode('utf-8')
#                 BG = row['Số bàn ghế'].encode('utf-8').decode('utf-8')
#                 TT = row['Tình trạng'].encode('utf-8').decode('utf-8')
#                 if (((self.entry_building1.get() == toa and (len(self.entry_room1.get()) == 0 or self.entry_room1.get() == phong)) or (len(self.entry_building1.get()) == 0 and len(self.entry_room1.get()) == 0))
#                     and (self.entry_TT.get() == TT or len(self.entry_TT.get())== 0)):
#                     self.tv.insert("", END, values=(toa,phong,SG,BG,TT))
#                     y=y+1
#                 if self.entry_building1.get() == toa and self.entry_room1.get() == phong:
#                     self.output_toa['text']=toa
#                     self.output_phong['text']=phong
#                     self.entry_numberSG.insert(0, SG)
#                     self.entry_numberBG.insert(0, BG)
#                     self.entry_status.insert(0,TT)
#                     self.lbl_numberCTr['text']=(int(SG)-x)
#             break
#         if y == 0:
#             mesbox.showwarning("Notification", "No room found")
#     def update(self):
#         myquery = {"Tòa": self.entry_building1.get(), "Phòng": self.entry_room1.get()}
#         newvalues = {"$set": {"Số giường": self.entry_numberSG.get(),
#                               "Số bàn ghế": self.entry_numberBG.get(),
#                               "Tình trạng":self.entry_status.get()}}
#         mycol1.update_one(myquery, newvalues)
#         mesbox.showinfo("Thông báo","cập nhật thành công")
#
# class QL_hoadon():
#     def QLHD_window(self):
#         bill = Tk()
#         bill.title("QLKTX_Quản lý hóa đơn")
#         bill.geometry('920x480')
#         bill.resizable(False, False)  # không cho thay đổi kích thước ,make sure dont resize the window
#         frame1 = Frame(bill, bg="white", relief="ridge", borderwidth=2)
#         frame1.place(x=0, y=0, width=100, height=480)
#
#         self.btn_st = Button(frame1, bg='{0}'.format(color1), text="SINH VIÊN", font="Andalus 10 bold",
#                              fg="white", command =self.QLSV_window)
#         self.btn_room = Button(frame1, bg='{0}'.format(color2), text="PHÒNG Ở", font="Andalus 10 bold",
#                                fg="white", command=self.QL_phong_window)
#         self.btn_bill = Button(frame1, bg='{0}'.format(color3), text="HÓA ĐƠN", font="Andalus 10 bold",
#                                fg="white")
#
#         self.btn_st.place(x=10, y=10, width=80, height=80)
#         self.btn_room.place(x=10, y=100, width=80, height=80)
#         self.btn_bill.place(x=10, y=190, width=80, height=80)
#
#         frame_top = Frame(bill, bg="gray")
#         frame_find = Frame(bill, bg='{0}'.format(color3), relief="ridge", borderwidth=2)
#         frame_ngancach = Frame(frame_find, bg='{0}'.format(color3), relief="ridge", borderwidth=2)
#         self.frame_info_st = Frame(bill, relief="ridge", borderwidth=2)
#         self.frame_update_add_student = Frame(bill, bg='{0}'.format(color1), borderwidth=2, relief="ridge")
#         self.frame_info = Frame(self.frame_update_add_student, relief="ridge", borderwidth=2,bg='{0}'.format(color1))
#         frame_botton = Frame(bill, bg="gray")
#         frame_top.place(x=101, y=0, width=810, height=40)
#         frame_find.place(x=101, y=41, width=450, height=160)
#         frame_ngancach.place(x=-2, y=-2, width=450, height=80)
#         self.frame_info_st.place(x=101, y=201, width=450, height=190)
#         self.frame_update_add_student.place(x=561, y=41, width=350, height=340)
#         self.frame_info.place(x=-2, y=40, width=350, height=230)
#         frame_botton.place(x=101, y=393, width=810, height=85)
#         # frame_find.place(x=150, y=20)
#         title_lp = Label(frame_ngancach, text="HÓA ĐƠN LỆ PHÍ", fg="white",bg="green",
#                            font="Andalus 8 bold")
#         title_lp.place(x=350, y=2)
#         self.entry_mssv = Entry(frame_ngancach, width=13, borderwidth=1)
#         self.entry_mssv.place(x=10, y=50)
#         label_mssv = Label(frame_ngancach, text="Mssv", highlightthickness=1, highlightbackground="green")
#         label_mssv.place(x=10, y=27)
#         self.entry_ndlp = Entry(frame_ngancach, width=14, borderwidth=1)
#         self.entry_ndlp.place(x=110, y=50)
#         label_ndlp = Label(frame_ngancach, text="Nội dung", highlightthickness=1, highlightbackground="green")
#         label_ndlp.place(x=110, y=27)
#         options_tt = ["", "Đã thanh toán", "Chưa thanh toán"]
#         self.entry_ttlp = ttk.Combobox(frame_ngancach, values=options_tt)
#         self.entry_ttlp.place(x=220, y=50, width=110)
#         label_ttlp = Label(frame_ngancach, text="Trạng thái", highlightthickness=1, highlightbackground="green")
#         label_ttlp.place(x=220, y=27)
#         self.search_HDLP = Button(frame_ngancach, width=6, text="Search", bg="green", fg="white", font="Andalus 10 bold", command=self.find_billlp)
#         self.search_HDLP.place(x=380, y=43)
#         self.entry_toa = Entry(frame_find, width=7, borderwidth=1)
#         self.entry_toa.place(x=10, y=133)
#         title_đn = Label(frame_find, text="HÓA ĐƠN ĐIỆN NƯỚC", fg="white",
#                          font="Andalus 8 bold", bg="green")
#         title_đn.place(x=322, y=82)
#         label_toa = Label(frame_find, text="Tòa", highlightthickness=1, highlightbackground="green")
#         label_toa.place(x=10, y=110)
#         self.entry_phong = Entry(frame_find, width=7, borderwidth=1)
#         self.entry_phong.place(x=90, y=133)
#         label_phong = Label(frame_find, text="Phòng", highlightthickness=1, highlightbackground="green")
#         label_phong.place(x=90, y=110)
#         self.entry_nddn = Entry(frame_find, width=15, borderwidth=1)
#         self.entry_nddn.place(x=160, y=133)
#         label_ndp = Label(frame_find, text="Nội dung", highlightthickness=1, highlightbackground="green")
#         label_ndp.place(x=160, y=110)
#         # options_tt = ["","Đã thanh toán","Chưa thanh toán"]
#         self.entry_ttdn = ttk.Combobox(frame_find, values=options_tt)
#         self.entry_ttdn.place(x=275, y=133, width=100)
#         label_ndp = Label(frame_find, text="Trạng thái", highlightthickness=1, highlightbackground="green")
#         label_ndp.place(x=275, y=110)
#         # self.entry_phong = Entry(frame_find, width=10, borderwidth=1)
#         # self.entry_phong.place(x=110, y=133)
#         # label_phong = Label(frame_find, text="Phòng", highlightthickness=1, highlightbackground="green")
#         # label_phong.place(x=110, y=110)
#         self.search_HDĐN = Button(frame_find, width=6, text="Search", bg="green", fg="white", font="Andalus 10 bold", command=self.find_billdn)
#         self.search_HDĐN.place(x=380, y=124)
#         label_list = Label(self.frame_info_st, text="DANH SÁCH HÓA ĐƠN", font="Andalus 12 bold", fg="blue")
#         label_list.place(x=0, y=0, width=447, height=30)
#
#         label_info = Label(self.frame_update_add_student, text="THÔNG TIN HÓA ĐƠN CHI TIẾT", fg="green",
#                            font="Andalus 12 bold")
#         label_info.place(x=10, y=10)
#         # label_mssv = Label(frame_update_add_student, text="Mã số sinh viên:")
#         # label_mssv.place(x=10, y=50)
#         # self.entry_mssv1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         # self.entry_mssv1.place(x=150, y=50)
#         # label_school = Label(frame_update_add_student, text="Trường:")
#         # label_school.place(x=10, y=80)
#         # self.entry_school1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         # self.entry_school1.place(x=150, y=80)
#         # label_name = Label(frame_update_add_student, text="Họ và tên:")
#         # label_name.place(x=10, y=110)
#         # self.entry_name1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         # self.entry_name1.place(x=150, y=110)
#         # label_gender = Label(frame_update_add_student, text="Giới tính:")
#         # label_gender.place(x=10, y=140)
#         # self.entry_gender1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         # self.entry_gender1.place(x=150, y=140)
#         # label_dob = Label(frame_update_add_student, text="Ngày sinh:")
#         # label_dob.place(x=10, y=170)
#         # self.entry_dob1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         # self.entry_dob1.place(x=150, y=170)
#         # label_cccd = Label(frame_update_add_student, text="Số CCCD:")
#         # label_cccd.place(x=10, y=200)
#         # self.entry_cccd1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         # self.entry_cccd1.place(x=150, y=200)
#         # label_building = Label(frame_update_add_student, text="Tòa:")
#         # label_building.place(x=10, y=230)
#         # self.entry_building1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         # self.entry_building1.place(x=150, y=230)
#         # label_room = Label(frame_update_add_student, text="Phòng:")
#         # label_room.place(x=10, y=260)
#         # self.entry_room1 = Entry(frame_update_add_student, width=30, borderwidth=1)
#         # self.entry_room1.place(x=150, y=260)
#         update_ST = Button(self.frame_update_add_student, width=9, text="Cập nhật", bg="green", fg="white",
#                            font="Arial 10 bold", command=self.update_bill)
#         update_ST.place(x=260, y=305)
#         # delete_ST = Button(frame_update_add_student, width=9, text="Xóa SV", bg="green", fg="white",
#         #                    font="Arial 10 bold")
#         # delete_ST.place(x=170, y=300)
#         options =["","Hóa đơn lệ phí","Hóa đơn điện nước"]
#         # clicked = StringVar()
#         # clicked.set(options[0])
#         # drop = OptionMenu(frame_update_add_student,clicked,*options)
#         # drop.place(x=80,y=300)
#         self.combo = ttk.Combobox(self.frame_update_add_student, values=options)
#         self.combo.current(0)
#         self.combo.bind("<<ComboboxSelected>>", self.bill_info_add)
#         self.combo.place(x=213,y=275, width=130)
#         add_ST = Button(self.frame_update_add_student, width=9, text="Thêm HĐ", bg="green", fg="white",
#                         font="Arial 10 bold", command=self.add_bill)
#         add_ST.place(x=165, y=305)
#
#     def find_billlp(self):
#         columns = ('Mssv', 'Nội dung', 'Số tiền', 'Trạng thái', 'Mã hóa đơn')
#         self.treelp = ttk.Treeview(self.frame_info_st, columns=columns, show='headings')
#         self.treelp.heading('Mssv', text="Mssv")
#         self.treelp.heading('Nội dung', text="Nội dung phí")
#         self.treelp.heading('Số tiền', text="Số tiền")
#         self.treelp.heading('Trạng thái', text="Trạng thái")
#         self.treelp.heading('Mã hóa đơn', text="Mã hóa đơn")
#         self.treelp.column('Mssv', width=80)
#         self.treelp.column('Nội dung', width=150)
#         self.treelp.column('Số tiền', width=100)
#         self.treelp.column('Trạng thái', width=120)
#         self.treelp.column('Mã hóa đơn', width=90)
#         self.treelp.place(x=0, y=30, width=448, height=140)
#         self.treelp.bind('<ButtonRelease-1>', self.select_bill)
#         scrollbar = ttk.Scrollbar(self.frame_info_st, orient=VERTICAL, command=self.treelp.yview)
#         self.treelp.configure(yscrollcommand=scrollbar.set)
#         scrollbar.place(x=430, y=31, height=138)
#         scrollbar1 = ttk.Scrollbar(self.frame_info_st, orient=HORIZONTAL, command=self.treelp.xview)
#         self.treelp.configure(xscrollcommand=scrollbar1.set)
#         scrollbar1.place(x=0, y=170, width=447)
#         rows = mycol2.find()
#         for row in rows:
#             x=0
#             mssv = row['Mssv'].encode('utf-8').decode('utf-8')
#             nd = row['Nội dung'].encode('utf-8').decode('utf-8')
#             sotien = row['Số tiền'].encode('utf-8').decode('utf-8')
#             tt = row['Trạng thái'].encode('utf-8').decode('utf-8')
#             mhd = row['Mã hóa đơn'].encode('utf-8').decode('utf-8')
#             if ((len(self.entry_mssv.get()) == 0 or self.entry_mssv.get() == mssv)
#                     and (len(self.entry_ndlp.get()) == 0 or self.entry_ndlp.get() == nd)
#                     and (len(self.entry_ttlp.get()) == 0 or self.entry_ttlp.get() == tt)):
#                 self.treelp.insert("", END, values=(mssv, nd, sotien,tt,mhd))
#                 x=x+1
#         if x==0:
#             mesbox.showwarning("Thông báo", "Không tìm thấy hóa đơn")
#
#     def find_billdn(self):
#         columns = ('Tòa', 'Phòng','Nội dung','Số tiền', 'Trạng thái', 'Mã hóa đơn')
#         self.tree = ttk.Treeview(self.frame_info_st, columns=columns, show='headings')
#         self.tree.heading('Tòa', text="Tòa")
#         self.tree.heading('Phòng', text="Phòng")
#         self.tree.heading('Nội dung', text="Nội dung")
#         self.tree.heading('Số tiền', text="Sô tiền")
#         self.tree.heading('Trạng thái', text="Trạng thái")
#         self.tree.heading('Mã hóa đơn', text="Mã hóa đơn")
#         self.tree.column('Tòa', width=50)
#         self.tree.column('Phòng', width=50)
#         self.tree.column('Nội dung', width=150)
#         self.tree.column('Số tiền', width=100)
#         self.tree.column('Trạng thái', width=120)
#         self.tree.column('Mã hóa đơn', width=90)
#         self.tree.bind('<ButtonRelease-1>',self.select_bill)
#         self.tree.place(x=0, y=30, width=448, height=140)
#         scrollbar = ttk.Scrollbar(self.frame_info_st, orient=VERTICAL, command=self.tree.yview)
#         self.tree.configure(yscrollcommand=scrollbar.set)
#         scrollbar.place(x=430, y=31, height=138)
#         scrollbar1 = ttk.Scrollbar(self.frame_info_st, orient=HORIZONTAL, command=self.tree.xview)
#         self.tree.configure(xscrollcommand=scrollbar1.set)
#         scrollbar1.place(x=0, y=170, width=447)
#         rows = mycol3.find()
#         for row in rows:
#             x=0
#             toa = row['Tòa'].encode('utf-8').decode('utf-8')
#             phong = row['Phòng'].encode('utf-8').decode('utf-8')
#             nd = row['Nội dung'].encode('utf-8').decode('utf-8')
#             sotien = row['Số tiền'].encode('utf-8').decode('utf-8')
#             tt = row['Trạng thái'].encode('utf-8').decode('utf-8')
#             mhd = row['Mã hóa đơn'].encode('utf-8').decode('utf-8')
#             if ((len(self.entry_toa.get()) == 0 or self.entry_toa.get() == toa)
#                    and (len(self.entry_phong.get()) == 0 or self.entry_phong.get() == phong)
#                     and (len(self.entry_nddn.get()) == 0 or self.entry_nddn.get() == nd)
#                     and (len(self.entry_ttdn.get()) == 0 or self.entry_ttdn.get() == tt)):
#                 self.tree.insert("", END, values=(toa,phong, nd, sotien,tt,mhd))
#                 x=x+1
#         if x==0:
#             mesbox.showwarning("Thông báo", "Không tìm thấy hóa đơn")
#     def bill_info_add(self, event):
#         # for widgets in self.frame_info.winfo_children():
#         #     widgets.destroy()
#
#         if self.combo.get()=="Hóa đơn lệ phí":
#             for widgets in self.frame_info.winfo_children():
#                 widgets.destroy()
#             label_mssv = Label(self.frame_info, text="Mã số sinh viên:")
#             label_mssv.place(x=10, y=50)
#             self.entry_mssvlp = Entry(self.frame_info, width=30, borderwidth=1)
#             self.entry_mssvlp.place(x=150, y=50)
#             label_school = Label(self.frame_info, text="Nội dung:")
#             label_school.place(x=10, y=80)
#             self.entry_nd = Entry(self.frame_info, width=30, borderwidth=1)
#             self.entry_nd.place(x=150, y=80)
#             label_amount = Label(self.frame_info, text="Số tiền:")
#             label_amount.place(x=10, y=110)
#             self.entry_amount = Entry(self.frame_info, width=30, borderwidth=1)
#             self.entry_amount.place(x=150, y=110)
#             label_tt = Label(self.frame_info, text="Trạng thái:")
#             label_tt.place(x=10, y=140)
#             self.entry_tt = Label(self.frame_info, width=25, borderwidth=1, text="Chưa thanh toán")
#             self.entry_tt.place(x=150, y=140)
#             label_mhd = Label(self.frame_info, text="Mã hóa đơn:")
#             label_mhd.place(x=10, y=170)
#             self.entry_mhd = Entry(self.frame_info, width=30, borderwidth=1)
#             self.entry_mhd.place(x=150, y=170)
#
#         if self.combo.get() == "Hóa đơn điện nước":
#             for widgets in self.frame_info.winfo_children():
#                 widgets.destroy()
#             label_toa = Label(self.frame_info, text="Tòa:")
#             label_toa.place(x=10, y=50)
#             self.entry_toa1 = Entry(self.frame_info, width=30, borderwidth=1)
#             self.entry_toa1.place(x=150, y=50)
#             label_phong = Label(self.frame_info, text="Phòng:")
#             label_phong.place(x=10, y=80)
#             self.entry_phong1 = Entry(self.frame_info, width=30, borderwidth=1)
#             self.entry_phong1.place(x=150, y=80)
#             label_nd = Label(self.frame_info, text="Nội dung:")
#             label_nd.place(x=10, y=110)
#             self.entry_nd1 = Entry(self.frame_info, width=30, borderwidth=1)
#             self.entry_nd1.place(x=150, y=110)
#             label_amount1 = Label(self.frame_info, text="Số tiền:")
#             label_amount1.place(x=10, y=140)
#             self.entry_amount1 = Entry(self.frame_info, width=30, borderwidth=1)
#             self.entry_amount1.place(x=150, y=140)
#             label_tt1 = Label(self.frame_info, text="Trạng thái:")
#             label_tt1.place(x=10, y=170)
#             self.entry_tt1 = Label(self.frame_info, width=25, borderwidth=1, text="Chưa thanh toán")
#             self.entry_tt1.place(x=150, y=170)
#             label_mhd1 = Label(self.frame_info, text="Mã hóa đơn:")
#             label_mhd1.place(x=10, y=200)
#             self.entry_mhd1 = Entry(self.frame_info, width=30, borderwidth=1)
#             self.entry_mhd1.place(x=150, y=200)
#     def add_bill(self):
#        if self.combo.get()=="Hóa đơn lệ phí":
#             mssv = self.entry_mssvlp.get()
#             nd = self.entry_nd.get()
#             sotien = self.entry_amount.get()
#             trangthai = self.entry_tt["text"]
#             mahoadon = self.entry_mhd.get()
#             if (len(mssv) == 0 or len(nd) == 0 or len(sotien) == 0 or len(trangthai) == 0 or len(mahoadon) == 0 ):
#                 mesbox.showwarning("WARNING", "Vui lòng nhập đủ thông tin")
#                 return
#             # else:
#             #     for row in mycol.find():
#             #         if row['Mssv'].encode('utf-8').decode('utf-8') == mssv:
#             #             mesbox.showwarning("ERROR", "Mã số sinh viên đã tồn tại")
#             #             return
#             mycol2.insert_one(
#                 {'Mssv': mssv, 'Nội dung': nd, 'Số tiền': sotien, 'Trạng thái': trangthai, 'Mã hóa đơn': mahoadon})
#             mesbox.showinfo("Thông báo", "Hóa đơn đã được tạo thành công")
#        if self.combo.get() == "Hóa đơn điện nước":
#            toa = self.entry_toa1.get()
#            phong = self.entry_phong1.get()
#            nd = self.entry_nd1.get()
#            sotien = self.entry_amount1.get()
#            trangthai = self.entry_tt1["text"]
#            mahoadon = self.entry_mhd1.get()
#            if (len(toa) == 0 or len(phong) == 0 or len(nd) == 0 or len(sotien) == 0 or len(trangthai) == 0 or len(mahoadon) == 0):
#                mesbox.showwarning("WARNING", "Vui lòng nhập đủ thông tin")
#                return
#            # else:
#            #     for row in mycol.find():
#            #         if row['Mssv'].encode('utf-8').decode('utf-8') == mssv:
#            #             mesbox.showwarning("ERROR", "Mã số sinh viên đã tồn tại")
#            #             return
#            mycol3.insert_one(
#                {'Tòa': toa, 'Phòng': phong,'Nội dung': nd, 'Số tiền': sotien, 'Trạng thái': trangthai, 'Mã hóa đơn': mahoadon})
#            mesbox.showinfo("Thông báo", "Hóa đơn đã được tạo thành công")
#     def select_bill(self, event):
#         if self.combo.get() == "Hóa đơn lệ phí":
#             self.entry_mssvlp.delete(0,END)
#             self.entry_nd.delete(0, END)
#             self.entry_amount.delete(0, END)
#             self.entry_mhd.delete(0, END)
#             self.curitem = self.treelp.focus()
#             self.entry_mssvlp.insert(0, self.treelp.item(self.curitem)['values'][0])
#             self.entry_nd.insert(0, self.treelp.item(self.curitem)['values'][1])
#             self.entry_amount.insert(0, self.treelp.item(self.curitem)['values'][2])
#             self.entry_tt["text"] = self.treelp.item(self.curitem)['values'][3]
#             self.entry_mhd.insert(0, self.treelp.item(self.curitem)['values'][4])
#         if self.combo.get() == "Hóa đơn điện nước":
#             self.entry_toa1.delete(0, END)
#             self.entry_phong1.delete(0, END)
#             self.entry_nd1.delete(0, END)
#             self.entry_amount1.delete(0, END)
#             self.entry_mhd1.delete(0, END)
#             self.curitem = self.tree.focus()
#             self.entry_toa1.insert(0, self.tree.item(self.curitem)['values'][0])
#             self.entry_phong1.insert(0, self.tree.item(self.curitem)['values'][1])
#             self.entry_nd1.insert(0, self.tree.item(self.curitem)['values'][2])
#             self.entry_amount1.insert(0, self.tree.item(self.curitem)['values'][3])
#             self.entry_tt1["text"] = self.tree.item(self.curitem)['values'][4]
#             self.entry_mhd1.insert(0, self.tree.item(self.curitem)['values'][5])
#     def update_bill(self):
#         if self.combo.get() == "Hóa đơn lệ phí":
#             myquery = {"Mssv": self.entry_mssvlp.get()}
#             newvalues = {"$set": {"Mssv": self.entry_mssvlp.get(),
#                                   "Nội dung": self.entry_nd.get(),
#                                   "Số tiền": self.entry_amount.get(),
#                                   "Mã hóa đơn": self.entry_mhd.get()}}
#             mycol2.update_one(myquery, newvalues)
#             mesbox.showinfo("Thông báo", "cập nhật thành công")
#         if self.combo.get() == "Hóa đơn điện nước":
#             myquery = {"Tòa": self.entry_toa1.get(),"Phòng": self.entry_phong1.get()}
#             newvalues = {"$set": {"Tòa": self.entry_toa1.get(),
#                                   "Phòng": self.entry_phong1.get(),
#                                   "Nội dung": self.entry_nd1.get(),
#                                   "Số tiền": self.entry_amount1.get(),
#                                   "Mã hóa đơn": self.entry_mhd1.get()}}
#             mycol3.update_one(myquery, newvalues)
#             mesbox.showinfo("Thông báo", "cập nhật thành công")
#
# class QL_KTX(QL_sinhvien, QL_phong, QL_hoadon):
#     def __init__(self, parent):
#         self.parent = parent
#         self.initUI()
#     def initUI(self):
#         self.parent.title("Quản lí kí túc xá")
#         frame1 = Frame(self.parent, bg="white", relief="ridge", borderwidth=2)
#         frame1.place(x=0, y=0, width=100, height=480)
#
#         btn_st = Button(frame1, bg='{0}'.format(color1), text="SINH VIÊN", font="Andalus 10 bold",
#                              fg="white", command=self.QLSV_window)
#         btn_room = Button(frame1, bg='{0}'.format(color2), text="PHÒNG Ở", font="Andalus 10 bold",
#                                fg="white", command=self.QL_phong_window)
#         btn_bill = Button(frame1, bg='{0}'.format(color3), text="HÓA ĐƠN", font="Andalus 10 bold",
#                                fg="white", command=self.QLHD_window)
#         btn_st.place(x=10, y=10, width=80, height=80)
#         btn_room.place(x=10, y=100, width=80, height=80)
#         btn_bill.place(x=10, y=190, width=80, height=80)
#
# app = QL_KTX(win)
# win.geometry("800x400")
# win.mainloop()



from tkinter import *
from tkinter import ttk
import pymssql
from PIL import Image, ImageTk
from workingbox import *
mydb = pymssql.connect(server="ADMIN", user="sa", password="bao000", database="Polypro")
cursor = mydb.cursor()
win = Tk()

class App():

    x = 0
    new_quanly_icon = PhotoImage(file="anhquanly.png").subsample(1, 1)
    new_thongke_icon = PhotoImage(file="4252963.png").subsample(1, 1)
    new_chuyende_symbol = PhotoImage(file="1802977.png").subsample(1, 1)
    new_khoahoc_symbol = PhotoImage(file="training-training-icon-blue-free-transparent-png-download-pngkey.png").subsample(1, 1)
    new_hocvien_symbol = PhotoImage(file="studenticon.png").subsample(1, 1)
    home_symbol = PhotoImage(file="toppng.com-free-sweet-icons-easy-home-icon-blue-513x500 (1).png").subsample(26, 26)
    back_symbol = PhotoImage(file="Metro-Back-Blue-256.png").subsample(8, 8)
    home_img = PhotoImage(file="image-asset.png").subsample(1, 1)
    save_button = PhotoImage(file="save-icon-5401.png").subsample(19, 19)
    delete_button = PhotoImage(file="758578.png").subsample(19, 19)

    def home_window(self):
        self.home = Toplevel(win)
        self.home.geometry("800x400")
        self.home.resizable(False, False)
        self.home.grab_set()
        menu_fr = Frame(self.home, borderwidth=2, width=200, height=350, background="white", relief="ridge")
        menu_fr.place(x=0, y=0)
        Button(menu_fr, text="Quản lý", font="Analus 11 bold", image=self.new_quanly_icon, compound=LEFT, command=self.quan_ly, width=160, height=50).place(x=10, y=20)
        Button(menu_fr, text="Thống kê", font="Analus 11 bold", image=self.new_thongke_icon, compound=LEFT,width=160, height=50).place(x=10, y=100)
        self.tinhnang_fr = Frame(self.home,width=500, height=350, background="silver")
        self.tinhnang_fr.place(x=230, y=10)
        def frame_home():
            self.clear_icon()
            Label(self.tinhnang_fr, text="LapTrinhCity", font="Analus 18 bold italic", fg="red", image=self.home_img,
                  compound=TOP).place(x=50, y=20)
        Label(self.tinhnang_fr, text="LapTrinhCity",font="Analus 18 bold italic", fg="red", image=self.home_img, compound=TOP).place(x=50, y=20)
        Button(menu_fr, font="Analus 6 bold", image=self.back_symbol, borderwidth=0, background="white").place(x=60, y=310)
        Button(menu_fr, font="Analus 6 bold", image=self.home_symbol, borderwidth=0, background="white", command=frame_home).place(x=10, y=310)
        # def frame_home():
        #     self.clear_icon()



    def clicked_button(self, t):
        self.x = t

    def quan_ly(self):
        self.clear_icon()
        Button(self.tinhnang_fr, text="Chuyên đề", font="Analus 11 bold", image=self.new_chuyende_symbol, compound=TOP, command=lambda t = "chuyende":[self.clicked_button(t), self.data_frame()], width=100,
               height=100).place(x=10, y=10)
        Button(self.tinhnang_fr, text="Khóa học", font="Analus 11 bold", image=self.new_khoahoc_symbol, compound=TOP, command=lambda t = "khoahoc":[self.clicked_button(t), self.data_frame()], width=100,
               height=100).place(x=160, y=10)
        Button(self.tinhnang_fr, text="Học viên", font="Analus 11 bold", image=self.new_hocvien_symbol, compound=TOP, command=lambda t = "hocvien":[self.clicked_button(t), self.data_frame()],
               width=100, height=100).place(x=310, y=10)

    def data_frame(self):
        self.clear_icon()
        columns_1 = ('MaCD', 'TenCD', 'HocPhi', 'ThoiLuong', 'MoTa')
        columns_2 = ("MaKH", 'MaCD', 'HocPhi', 'ThoiLuong', 'NgayKG', 'GhiChu', 'MaNV', 'NgayTao')
        columns_3 = ('MaNH', 'HoTen', 'NgaySinh', 'GioiTinh', 'DienThoai', 'Email', 'GhiChu', 'MaNV', 'NgayDK')
        # self.tree = ttk.Treeview(self.tinhnang_fr, columns=columns_1, show='headings')
        if self.x == "chuyende":
            self.tree = ttk.Treeview(self.tinhnang_fr, columns=columns_1, show='headings')
            self.tree.heading('MaCD', text="MaCD")
            self.tree.heading('TenCD', text="TenCD")
            self.tree.heading('HocPhi', text="HocPhi")
            self.tree.heading('ThoiLuong', text="ThoiLuong")
            self.tree.heading('MoTa', text="MoTa")
            self.tree.column('MaCD', width=60)
            self.tree.column('TenCD', width=200)
            self.tree.column('HocPhi', width=50)
            self.tree.column('ThoiLuong', width=80)
            self.tree.column('MoTa', width=250)
        if self.x == "khoahoc":
            self.tree = ttk.Treeview(self.tinhnang_fr, columns=columns_2, show='headings')
            self.tree.heading('MaKH', text="MaKH")
            self.tree.heading('MaCD', text="MaCD")
            self.tree.heading('HocPhi', text="HocPhi")
            self.tree.heading('ThoiLuong', text="ThoiLuong")
            self.tree.heading('NgayKG', text="NgayKG")
            self.tree.heading('GhiChu', text="GhiChu")
            self.tree.heading('MaNV', text="MaNV")
            self.tree.heading('NgayTao', text="NgayTao")
            self.tree.column('MaKH', width=60)
            self.tree.column('MaCD', width=60)
            self.tree.column('HocPhi', width=50)
            self.tree.column('ThoiLuong', width=80)
            self.tree.column('NgayKG', width=110)
            self.tree.column('GhiChu', width=80)
            self.tree.column('MaNV', width=90)
            self.tree.column('NgayTao', width=100)
        if self.x == "hocvien":
            self.tree = ttk.Treeview(self.tinhnang_fr, columns=columns_3, show='headings')
            self.tree.heading('MaNH', text="MaNH")
            self.tree.heading('HoTen', text="HoTen")
            self.tree.heading('NgaySinh', text="NgaySinh")
            self.tree.heading('GioiTinh', text="GioiTinh")
            self.tree.heading('DienThoai', text="DienThoai")
            self.tree.heading('Email', text="Email")
            self.tree.heading('GhiChu', text="GhiChu")
            self.tree.heading('MaNV', text="MaNV")
            self.tree.heading('NgayDK', text="NgayDK")
            self.tree.column('MaNH', width=60)
            self.tree.column('HoTen', width=150)
            self.tree.column('NgaySinh', width=80)
            self.tree.column('GioiTinh', width=60)
            self.tree.column('DienThoai', width=80)
            self.tree.column('Email', width=130)
            self.tree.column('GhiChu', width=200)
            self.tree.column('MaNV', width=50)
            self.tree.column('NgayDK', width=70)
        self.tree.bind('<ButtonRelease-1>', self.select_item)
        self.tree.place(x=0, y=0, width=485, height=335)
        scrollbar = ttk.Scrollbar(self.tinhnang_fr, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=485, y=0, height=335)
        scrollbar1 = ttk.Scrollbar(self.tinhnang_fr, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=scrollbar1.set)
        scrollbar1.place(x=0, y=335, width=485)
        self.load_data()

    def load_data(self):
        if self.x == "chuyende":
            cursor.execute("select MaCD, TenCD, HocPhi, ThoiLuong, MoTa from ChuyenDe")
            chuyen_de = cursor.fetchall()
            for row in chuyen_de:
                self.tree.insert("", END, values=row)
        if self.x == "khoahoc":
            cursor.execute("select * from KhoaHoc")
            khoa_hoc = cursor.fetchall()
            for row in khoa_hoc:
                self.tree.insert("", END, values=row)
        if self.x == "hocvien":
            cursor.execute("select * from NguoiHoc")
            nguoi_hoc = cursor.fetchall()
            for row in nguoi_hoc:
                self.tree.insert("", END, values=row)

    def clear_icon(self):
        for widgets in self.tinhnang_fr.winfo_children():
            widgets.destroy()

    def select_item(self, event):
        self.box_window()
        item = self.tree.focus()
        self.item_1 = self.tree.item(item)["values"]
        a = 0
        # self.entry = Entry(self.thongtin_chitiet, width=40)
        for i in self.tree["columns"]:
            Label(self.thongtin_chitiet, text=i, font="Analus 10 bold", background="white", fg="red").grid(row=a, column=0)
            self.entry= Entry(self.thongtin_chitiet, width=40)
            self.entry.grid(row=a, column=1)
            self.entry.insert(0, self.item_1[a])
            a += 1

        if self.x == "khoahoc":
            # self.dshv = Frame(self.box_win, background="silver", width=550, height=160).place(x=10, y=230)
            # columns = ('MaHV', 'MaNH', 'HoTen', 'NgaySinh', 'GioiTinh', 'DienThoai', 'Email', 'Diem')
            Label(self.box_win, text="DANH SÁCH HỌC VIÊN", font="Caribri 11 bold").place(x=230, y=210)
            columns = ('1', '2', '3', '4', '5', '6', '7', '8')
            # headings = ('Mã học viên', 'Mã người học', 'Họ tên', 'Ngày sinh', 'Giới tính', 'Điện thoại', 'Email', 'Điểm')
            self.hocvien = ttk.Treeview(self.box_win, columns=columns, show='headings')
            self.hocvien.place(x=10, y=237, width=550, height=160)
            # self.hocvien.place(x=0, y=0)
            # self.hocvien.heading('0', text="Mã khóa học")
            self.hocvien.heading('1', text="Mã học viên")
            self.hocvien.heading('2', text="Mã người học")
            self.hocvien.heading('3', text="Họ tên")
            self.hocvien.heading('4', text="Ngày sinh")
            self.hocvien.heading('5', text="Giới tính")
            self.hocvien.heading('6', text="Điện thoại")
            self.hocvien.heading('7', text="Email")
            self.hocvien.heading('8', text="Điểm")
            # self.hocvien.column('0', width=100)
            self.hocvien.column('1', width=100)
            self.hocvien.column('2', width=100)
            self.hocvien.column('3', width=100)
            self.hocvien.column('4', width=100)
            self.hocvien.column('5', width=100)
            self.hocvien.column('6', width=100)
            self.hocvien.column('7', width=100)
            self.hocvien.column('8', width=100)
            scrollbar = ttk.Scrollbar(self.box_win, orient=VERTICAL, command=self.hocvien.yview)
            self.hocvien.configure(yscrollcommand=scrollbar.set)
            scrollbar.place(x=545, y=237, height=160)
            scrollbar1 = ttk.Scrollbar(self.box_win, orient=HORIZONTAL, command=self.hocvien.xview)
            self.hocvien.configure(xscrollcommand=scrollbar1.set)
            scrollbar1.place(x=10, y=382, width=535)
            cursor.execute("select HV.MaHV, HV.MaNH, NH.HoTen, NH.NgaySinh, NH.GioiTinh, NH.DienThoai, NH.Email, HV.Diem from HocVien HV inner join NguoiHoc NH on NH.MaNH = HV.MaNH where HV.MaKH = '%s'"%self.item_1[0])
            hoc_vien = cursor.fetchall()
            for row in hoc_vien:
                self.hocvien.insert("", END, values=row)

    def box_window(self):
        self.box_win = Toplevel(win)
        self.box_win.geometry("600x400")
        self.box_win.resizable(False, False)
        self.box_win.grab_set()
        self.thongtin_chitiet = Frame(self.box_win, width=300, height=200, background="white")
        self.thongtin_chitiet.grid(row=0, column=0)
        Button(self.thongtin_chitiet, image=self.save_button, borderwidth=0, background="white").grid(row=len(self.tree["columns"])+2, column=2)
        Button(self.thongtin_chitiet, image=self.delete_button, borderwidth=0, background="white").grid(row=len(self.tree["columns"]) + 2, column=3)

class Login(App):
    def __init__(self, parent):
        self.parent = parent
        self.login_window()

    def login_window(self):
        self.frame_login = Frame(self.parent, background="silver", relief="ridge", borderwidth=2)
        self.frame_login.place(x=200, y=100, width=350, height=140)
        label_usn = Label(self.frame_login, text="Username", font="Andalus 12 bold")
        label_usn.place(x=10, y=10)
        self.entry_usn = Entry(self.frame_login, borderwidth=2, highlightthickness=1)
        self.entry_usn.place(x=110, y=10, width=200, height=20)
        label_pw = Label(self.frame_login, text="Password", font="Analus 12 bold")
        label_pw.place(x=10, y=50)
        self.entry_pw = Entry(self.frame_login, borderwidth=2, highlightthickness=1, show="*")
        self.entry_pw.place(x=110, y=50, width=200, height=20)
        button_login = Button(self.frame_login, text="Đăng nhập", font="Analus 12 bold", background="yellow", borderwidth=2,
                              highlightthickness=1, command= self.login)
        button_login.place(x=110, y=95, width=150, height=35)


    def login(self):
        nhan_vien = mydb.cursor()
        nhan_vien.execute("select * from NhanVien")
        rows = nhan_vien.fetchall()
        username = self.entry_usn.get()
        password = self.entry_pw.get()
        x = 0
        for row in rows:
            if username == row[0] and password == row[1]:
                x = x + 1
                self.home_window()
                break
        if x == 0:
            message = Label(self.frame_login, text = "Thông tin đăng nhập không chính xác", fg="red", font="Analus 8 italic", background="silver")
            message.place(x=100, y=72)
            message.after(1500, message.destroy)

appp = Login(win)
win.geometry("800x400")
win.resizable(False, False)
win.mainloop()
