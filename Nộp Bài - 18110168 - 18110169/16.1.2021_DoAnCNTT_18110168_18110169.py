import sys
import pandas as pd
import tkinter as tk
import numpy as np
import tkinter.filedialog as fd
import webbrowser
import pylint
from tkinter import *
from tkinter import ttk
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open, SaveAs
from PIL import ImageTk, Image
from pandas import DataFrame

List_PhongBan = [('KH','Phong Kinh te Ke hoach'),
                ('KT','Phong Ke toan Tai chanh'),
                ('TC','Phong To chuc Nhan so'),
                ('TK','Phong Ky thuat Thiet ke'),
                ('VP','Van phong Xi nghiep')]
DataFrame_PhongBan = pd.DataFrame.from_records(List_PhongBan, columns = ['MaPB','TenPB'])

List_HSChucVu = [('GD',3.00),
                ('NV',1.00),
                ('PGD',2.20),
                ('PP',1.50),
                ('TK',1.20),
                ('TL',1.50),
                ('TP',2.00),
                ('TX',1.20)]
DataFrame_HSChucVu = pd.DataFrame.from_records(List_HSChucVu, columns = ['ChucVu','HSCV'])

List_NhanVien = [('001','Lai Van','Sam',0,'01/01/1966','30/04/1990','VP'),
                ('002','Tran Van','Minh',0,'23/02/1965','10/05/1990','VP'),
                ('003','Tong Canh','Son',0,'12/04/1963','24/10/1996','TK'),
                ('004','Ngo Viet','Hung',0,'11/02/1977','04/06/1997','TK'),
                ('005','Mai Tho','Loan',1,'23/05/1970','08/03/1989','TK'),
                ('006','Mac Xuan','Tien',0,'12/04/1963','28/03/1992','TK'),
                ('007','Vu Hoai','Anh',0,'15/06/1968','09/03/1993','KH'),
                ('008','Tran Thanh','Khanh',0,'15/07/1942','11/10/1985','KH'),
                ('009','Nguyen Hong','Hanh',1,'13/01/1962','06/06/1987','KT'),
                ('010','Le Thi','Huong',1,'23/05/1962','06/06/1988','KT'),
                ('011','Lam Quoc','Khanh',0,'21/06/1963','27/09/1991','KT'),
                ('012','Nguyen Hong','Van',1,'11/05/1976','05/05/1995','TK'),
                ('013','Nguyen Minh','Quang',0,'13/06/1951','05/05/1978','VP'),
                ('014','Trang Phi','Hung',0,'23/03/1953','07/07/1996','VP'),
                ('015','Tran Nguyet','Minh',1,'19/09/1963','10/10/1995','VP'),
                ('016','Nguyen Ngoc','Hien',1,'14/03/1961','08/04/1990','VP'),
                ('017','Do Anh','Hang',0,'11/01/1960','05/05/1979','VP'),
                ('018','Dinh Thi','Tam',1,'04/03/1962','05/05/1995','TC'),
                ('019','Nguyen Kim','Toan',1,'01/09/1960','31/07/1990','TC'),
                ('020','Nguyen Bich','Lien',1,'03/03/1969','16/12/1996','TC'),
                ('021','Huynh Bach','Tuyet',1,'07/03/1968','23/05/1994','KH'),
                ('022','Le Phuong','Thanh',1,'12/02/1957','05/05/1981','KH'),
                ('023','Ta The','Khanh',0,'23/05/1969','15/09/1993','KH'),
                ('024','Bui Son','Hai',0,'14/03/1951','08/05/1990','TC'),
                ('025','Luu Vu','Cam',0,'17/06/1970','22/08/1995','TK'),
                ('026','Doan Thi','Chi',0,'12/05/1960','30/10/1994','TC'),
                ('027','Tran Quang','Thanh',0,'14/09/1963','05/05/1992','TK'),
                ('028','Truong Le','Xuan',1,'13/04/1968','23/05/1994','KT'),
                ('029','Nguyen Van','Thanh',0,'02/09/1969','08/02/1996','TC'),
                ('030','Dang Van','Thuy',0,'01/01/1968','23/08/1992','TK'),
                ('031','Nguyen Van','Thanh',0,'02/02/1979','23/05/1994','KH'),
                ('032','Lam Van','Tuan',0,'12/02/1969','09/09/1993','TK'),
                ('033','Hoang Ngoc','Thanh',0,'13/05/1944','09/03/1978','VP'),
                ('034','Nguyen Van','Nuoi',0,'23/04/1970','02/10/1990','TK'),
                ('035','Do Dinh','Viet',0,'12/04/1945','31/07/1985','TC'),
                ('036','Le Trung','Binh',0,'13/04/1977','30/05/1997','TK'),
                ('037','Tran The','Duyet',0,'14/04/1970','26/04/1996','KH'),
                ('038','Le Bich','Phuong',1,'13/03/1974','04/08/1995','KH'),
                ('039','Mai Van','Duoc',0,'14/04/1960','04/10/1993','TC'),
                ('040','Truong Xuan','Hong',0,'15/05/1940','28/04/1979','TC'),
                ('041','Huynh Ngoc','Quanh',0,'23/05/1964','30/05/1990','TK'),
                ('042','Dao Thanh','Huong',1,'12/03/1969','08/08/1993','TK'),
                ('043','Pham Hoai','Nam',1,'15/06/1978','28/07/1992','VP'),
                ('044','Le Thi My','Linh',1,'19/09/1971','30/05/1995','TK'),
                ('045','Pham The','Dung',0,'23/05/1980','30/12/1997','TK'),
                ('046','Hoang Thanh','Trang',1,'12/03/1970','03/03/1997','KT'),
                ('047','Nguyen Van','Hien',0,'15/06/1960','05/05/1988','TK'),
                ('048','Tran Nguyet','Nga',1,'12/07/1965','26/04/1993','TK'),
                ('049','Mai Thi Hong','Xuan',1,'02/06/1962','09/09/1995','VP'),
                ('050','Nguyen Thi','Nam',1,'06/07/1960','06/06/1987','KT'),
                ('051','Ton Thi Thanh','Nhan',1,'14/06/1965','04/10/1993','TC'),
                ('052','Nguyen To','Uyen',1,'05/06/1963','07/10/1990','TK'),
                ('053','Luong Anh','Tuyen',1,'23/01/1975','02/10/1997','KT'),
                ('054','Doan Van','Thanh',0,'24/03/1971','06/06/1993','VP'),
                ('055','Luong Van','Chanh',0,'20/05/1963','12/01/1997','TK'),
                ('056','Truong Tuong','Nhat',0,'25/12/1972','23/05/1994','KH'),
                ('057','Nguyen Xuan','Phuong',0,'14/04/1960','05/01/1986','TK'),
                ('058','Vo Ngoc','Quang',0,'12/02/1960','07/10/1990','TK'),
                ('059','Nguyen Thanh','Thuy',1,'19/05/1960','07/07/1996','TK'),
                ('060','Nguyen Trong','Son',0,'20/05/1941','22/07/1989','KT')]
DataFrame_NhanVien = pd.DataFrame.from_records(List_NhanVien, columns = ['MaNV','Ho','Ten','Phai','NTNS','NgayBatDau','MaPB'])

List_ChiTiet = [('001','NV',4,'C1'),
                ('002','NV',5,'C3'),
                ('003','NV',3,'C2'),
                ('004','NV',2,'C1'),
                ('005','NV',6,'C3'),
                ('006','TL',6,'B2'),
                ('007','PP',5,'B2'),
                ('008','PGD',7,'A2'),
                ('009','PP',7,'B2'),
                ('010','NV',6,'C3'),
                ('011','NV',5,'C2'),
                ('012','NV',4,'C3'),
                ('013','NV',7,'C3'),
                ('014','TX',4,'B3'),
                ('015','TK',4,'C2'),
                ('016','NV',5,'C1'),
                ('017','PP',8,'B2'),
                ('018','NV',3,'C2'),
                ('019','PGD',7,'A2'),
                ('020','TK',4,'C2'),
                ('021','TL',5,'B2'),
                ('022','TP',7,'A3'),
                ('023','NV',4,'C2'),
                ('024','NV',4,'C3'),
                ('025','NV',3,'C3'),
                ('026','TL',4,'B2'),
                ('027','TX',5,'B3'),
                ('028','NV',7,'C3'),
                ('029','NV',3,'C3'),
                ('030','NV',3,'C3'),
                ('031','NV',4,'C2'),
                ('032','PP',6,'B3'),
                ('033','TP',7,'A3'),
                ('034','NV',5,'C3'),
                ('035','PP',6,'B3'),
                ('036','TK',4,'B1'),
                ('037','NV',3,'C2'),
                ('038','TK',4,'B1'),
                ('039','NV',4,'C2'),
                ('040','TP',7,'A3'),
                ('041','PGD',8,'A2'),
                ('042','NV',5,'C3'),
                ('043','TK',4,'B1'),
                ('044','NV',4,'C3'),
                ('045','NV',3,'C1'),
                ('046','NV',2,'C1'),
                ('047','TP',8,'A2'),
                ('048','NV',5,'C3'),
                ('049','NV',3,'C2'),
                ('050','NV',6,'C3'),
                ('051','NV',4,'C2'),
                ('052','PP',7,'B3'),
                ('053','NV',2,'C2'),
                ('054','NV',4,'C2'),
                ('055','NV',3,'C2'),
                ('056','NV',4,'C3'),
                ('057','GD',9,'A3'),
                ('058','NV',4,'C3'),
                ('059','NV',3,'C1'),
                ('060','TP',7,'A3')]
DataFrame_ChiTiet = pd.DataFrame.from_records(List_ChiTiet, columns = ['MaNV','ChucVu','HSLuong','MucDoCV'])
#??? ????y nh??m em l??u c??c list tr??n v??o c??c text file .txt tr???ng
f = open("Python_ChiTiet.txt", "w")#ghi ???? l??n
print(DataFrame_ChiTiet, file=f)
f.close()

f = open("Python_HSChucVu.txt", "w")#ghi ???? l??n
print(DataFrame_HSChucVu, file=f)
f.close()

f = open("Python_NhanVien.txt", "w")#ghi ???? l??n
print(DataFrame_NhanVien, file=f)
f.close()

f = open("Python_PhongBan.txt", "w")#ghi ???? l??n
print(DataFrame_PhongBan, file=f)
f.close()

class formNhanVien(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("TH??NG TIN NH??N VI??N")

        gr2 = tk.LabelFrame(self, padx = 20, pady = 15, text ="Th??ng Tin")
        gr2.pack(padx = 17, pady = 12)

        tk.Label(gr2, text="M?? Nh??n Vi??n").grid(row = 0, column = 0)
        entryMaNhanVien = tk.Entry(gr2)
        entryMaNhanVien.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="H??? ").grid(row = 0, column = 1)
        entryHo = tk.Entry(gr2)
        entryHo.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="T??n").grid(row = 0, column = 2)
        entryTen = tk.Entry(gr2)
        entryTen.grid(row=1,column=2,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ph??i").grid(row = 0, column = 3)
        entryPhai = tk.Entry(gr2)
        entryPhai.grid(row=1,column=3,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ng??y Th??ng N??m Sinh").grid(row = 0, column = 4)
        entryNgayThangNamSinh = tk.Entry(gr2)
        entryNgayThangNamSinh.grid(row=1,column=4,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ng??y B???t ?????u").grid(row = 0, column = 5)
        entryNgayBatDau = tk.Entry(gr2)
        entryNgayBatDau.grid(row=1,column=5,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="M?? Ph??ng Ban").grid(row = 0, column = 6)
        entryMaPhongBan = tk.Entry(gr2)
        entryMaPhongBan.grid(row =1,column=6,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="X??a m???u tin th???:").grid(row = 2, column = 0)
        entryXoaMauTin = tk.Entry(gr2)
        entryXoaMauTin.grid(row =3,column=0,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ch??n v??o tr?????c m???u tin th???:").grid(row = 2, column = 1)
        entryChenTruoc = tk.Entry(gr2)
        entryChenTruoc.grid(row =3,column=1,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ch??n v??o sau m???u tin th???:").grid(row = 2, column = 2)
        entryChenSau = tk.Entry(gr2)
        entryChenSau.grid(row =3,column=2,sticky=tk.W,padx=5,pady=5)

        gr3 = tk.LabelFrame(self, padx = 20, pady = 15, text = "B???ng Nh??n Vi??n")
        gr3.pack(padx = 17, pady = 12)

        my_text = tk.Text(gr3)
        my_text.grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)
        text_file = open("Python_NhanVien.txt","r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

        #------------- Functions ----------------

        def Xoa_Mau_Tin():
            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryXoaMauTin.get()
            e2 = int(e1)

            #Th???c Hi???n tr??n DataFrame_NhanVien:
            DataFrame_NhanVien_New = DataFrame_NhanVien.drop(DataFrame_NhanVien.index[[e2]])

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_NhanVien_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_NhanVien.txt", "w+")#ghi ???? l??n
            print(DataFrame_NhanVien_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_NhanVien.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryXoaMauTin.delete(0,END)

        # H??m ch??n d??ng b???t k??? v??o DataFrame
        #https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value): 
            # Starting value of upper half 
            start_upper = 0
            # End value of upper half 
            end_upper = row_number 
            # Start value of lower half 
            start_lower = row_number 
            # End value of lower half 
            end_lower = df.shape[0] 
            # Create a list of upper_half index 
            upper_half = [*range(start_upper, end_upper, 1)] 
            # Create a list of lower_half index 
            lower_half = [*range(start_lower, end_lower, 1)] 
            # Increment the value of lower half by 1 
            lower_half = [x.__add__(1) for x in lower_half] 
            # Combine the two lists 
            index_ = upper_half + lower_half 
            # Update the index of the dataframe 
            df.index = index_ 
            # Insert a row at the end 
            df.loc[row_number] = row_value 
            # Sort the index labels 
            df = df.sort_index() 
            # return the dataframe 
            return df 

        def Chen_Truoc():
            #row_number, DataFrame_NhanVien, row_value

            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryMaNhanVien.get()
            e2 = entryHo.get()
            e3 = entryTen.get()
            e4 = entryPhai.get()
            e5 = entryNgayThangNamSinh.get()
            e6 = entryNgayBatDau.get()
            e7 = entryMaPhongBan.get()
            
            e8 = entryChenTruoc.get()
            e9 = int(e8)

            #Th???c Hi???n tr??n DataFrame_NhanVien:
            #List_NhanVien.insert(e9, )
            #mautinmoi = pd.DataFrame([[e1,e2,e3,e4,e5,e6,e7]], columns= DataFrame_NhanVien.columns)
            mautinmoi = [e1,e2,e3,e4,e5,e6,e7]
            DataFrame_NhanVien_New = Insert_row(e9, DataFrame_NhanVien, mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_NhanVien_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_NhanVien.txt", "w+")#ghi ???? l??n
            print(DataFrame_NhanVien_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_NhanVien.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryMaNhanVien.delete(0,END)
            entryHo.delete(0,END)
            entryTen.delete(0,END)
            entryPhai.delete(0,END)
            entryNgayThangNamSinh.delete(0,END)
            entryNgayBatDau.delete(0,END)
            entryMaPhongBan.delete(0,END)
            entryChenTruoc.delete(0,END)  

        def Chen_Sau():
            #row_number, DataFrame_NhanVien, row_value

            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryMaNhanVien.get()
            e2 = entryHo.get()
            e3 = entryTen.get()
            e4 = entryPhai.get()
            e5 = entryNgayThangNamSinh.get()
            e6 = entryNgayBatDau.get()
            e7 = entryMaPhongBan.get()
            
            e8 = entryChenSau.get()
            e9 = int(e8) + 1

            #Th???c Hi???n tr??n DataFrame_NhanVien:
            #List_NhanVien.insert(e9, )
            #mautinmoi = pd.DataFrame([[e1,e2,e3,e4,e5,e6,e7]], columns= DataFrame_NhanVien.columns)
            mautinmoi = [e1,e2,e3,e4,e5,e6,e7]
            DataFrame_NhanVien_New = Insert_row(e9, DataFrame_NhanVien, mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_NhanVien_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_NhanVien.txt", "w+")#ghi ???? l??n
            print(DataFrame_NhanVien_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_NhanVien.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryMaNhanVien.delete(0,END)
            entryHo.delete(0,END)
            entryTen.delete(0,END)
            entryPhai.delete(0,END)
            entryNgayThangNamSinh.delete(0,END)
            entryNgayBatDau.delete(0,END)
            entryMaPhongBan.delete(0,END)
            entryChenSau.delete(0,END)

        def Chen_Cuoi():
            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryMaNhanVien.get()
            e2 = entryHo.get()
            e3 = entryTen.get()
            e4 = entryPhai.get()
            e5 = entryNgayThangNamSinh.get()
            e6 = entryNgayBatDau.get()
            e7 = entryMaPhongBan.get()

            #Th???c Hi???n tr??n DataFrame_NhanVien:
            mautinmoi = pd.DataFrame([[e1,e2,e3,e4,e5,e6,e7]], columns= DataFrame_NhanVien.columns)
            #mautinmoi = pd.DataFrame([[e1,e2,e3,e4,e5,e6,e7]], columns= ['MaNV','Ho','Ten','Phai','NTNS','NgayBatDau','MaPB'])
            DataFrame_NhanVien_New = DataFrame_NhanVien.append(mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_NhanVien_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_NhanVien.txt", "w+")#ghi ???? l??n
            print(DataFrame_NhanVien_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_NhanVien.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryMaNhanVien.delete(0,END)
            entryHo.delete(0,END)
            entryTen.delete(0,END)
            entryPhai.delete(0,END)
            entryNgayThangNamSinh.delete(0,END)
            entryNgayBatDau.delete(0,END)
            entryMaPhongBan.delete(0,END)        

        #----------------------------------------

        btnXoaMauTin = tk.Button(gr2, text="X??a M???u Tin", command = Xoa_Mau_Tin)
        btnXoaMauTin.grid(row = 4, column = 0, ipadx = 15, ipady = 1.5)

        btnChenTruoc = tk.Button(gr2, text="Ch??n tr?????c", command = Chen_Truoc)
        btnChenTruoc.grid(row = 4, column = 1, ipadx = 15, ipady = 1.5)


        btnChenSau = tk.Button(gr2, text="Ch??n sau", command = Chen_Sau)
        btnChenSau.grid(row = 4, column = 2, ipadx = 15, ipady = 1.5)

        btnChenCuoi = tk.Button(gr2, text="Ch??n ??? Cu???i", command = Chen_Cuoi)
        btnChenCuoi.grid(row = 4, column = 3, ipadx = 15, ipady = 1.5)
        

        formNhanVien.pack()

class formChucVu(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("H??? S?? CH???C V???")

        gr2 = tk.LabelFrame(self, padx = 20, pady = 15, text ="Th??ng Tin")
        gr2.pack(padx = 17, pady = 12)

        tk.Label(gr2, text="Ch???c V???").grid(row = 0, column = 0)
        entryChucVu = tk.Entry(gr2)
        entryChucVu.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="HS C??ng Vi???c").grid(row = 0, column = 1)
        entryHSCongViec = tk.Entry(gr2)
        entryHSCongViec.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="X??a m???u tin th???:").grid(row = 2, column = 0)
        entryXoaMauTin = tk.Entry(gr2)
        entryXoaMauTin.grid(row =3,column=0,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ch??n v??o tr?????c m???u tin th???:").grid(row = 2, column = 1)
        entryChenTruoc = tk.Entry(gr2)
        entryChenTruoc.grid(row =3,column=1,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ch??n v??o sau m???u tin th???:").grid(row = 2, column = 2)
        entryChenSau = tk.Entry(gr2)
        entryChenSau.grid(row =3,column=2,sticky=tk.W,padx=5,pady=5)

        gr3 = tk.LabelFrame(self, padx = 20, pady = 15, text = "B???ng Ch???c V???")
        gr3.pack(padx = 17, pady = 12)

        my_text = tk.Text(gr3)
        my_text.grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)
        text_file = open("Python_HSChucVu.txt","r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

        #------------- Functions ----------------

        def Xoa_Mau_Tin():
            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryXoaMauTin.get()
            e2 = int(e1)

            #Th???c Hi???n tr??n DataFrame_HSChucVu:
            DataFrame_HSChucVu_New = DataFrame_HSChucVu.drop(DataFrame_HSChucVu.index[[e2]])

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_HSChucVu_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_HSChucVu.txt", "w+")#ghi ???? l??n
            print(DataFrame_HSChucVu_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_HSChucVu.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryXoaMauTin.delete(0,END)

        # H??m ch??n d??ng b???t k??? v??o DataFrame
        #https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value): 
            # Starting value of upper half 
            start_upper = 0
            # End value of upper half 
            end_upper = row_number 
            # Start value of lower half 
            start_lower = row_number 
            # End value of lower half 
            end_lower = df.shape[0] 
            # Create a list of upper_half index 
            upper_half = [*range(start_upper, end_upper, 1)] 
            # Create a list of lower_half index 
            lower_half = [*range(start_lower, end_lower, 1)] 
            # Increment the value of lower half by 1 
            lower_half = [x.__add__(1) for x in lower_half] 
            # Combine the two lists 
            index_ = upper_half + lower_half 
            # Update the index of the dataframe 
            df.index = index_ 
            # Insert a row at the end 
            df.loc[row_number] = row_value 
            # Sort the index labels 
            df = df.sort_index() 
            # return the dataframe 
            return df 

        def Chen_Truoc():
            #row_number, DataFrame_HSChucVu, row_value

            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryChucVu.get()
            e2 = entryHSCongViec.get()
            
            e8 = entryChenTruoc.get()
            e9 = int(e8)

            #Th???c Hi???n tr??n DataFrame_HSChucVu:
            #List_HSChucVu.insert(e9, )
            #mautinmoi = pd.DataFrame([[e1,e2]], columns= DataFrame_HSChucVu.columns)
            mautinmoi = [e1,e2]
            DataFrame_HSChucVu_New = Insert_row(e9, DataFrame_HSChucVu, mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_HSChucVu_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_HSChucVu.txt", "w+")#ghi ???? l??n
            print(DataFrame_HSChucVu_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_HSChucVu.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryChucVu.delete(0,END)
            entryHSCongViec.delete(0,END)
            entryChenTruoc.delete(0,END)  

        def Chen_Sau():
            #row_number, DataFrame_HSChucVu, row_value

            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryChucVu.get()
            e2 = entryHSCongViec.get()
            
            e8 = entryChenTruoc.get()
            e9 = int(e8) + 1

            #Th???c Hi???n tr??n DataFrame_HSChucVu:
            #List_HSChucVu.insert(e9, )
            #mautinmoi = pd.DataFrame([[e1,e2]], columns= DataFrame_HSChucVu.columns)
            mautinmoi = [e1,e2]
            DataFrame_HSChucVu_New = Insert_row(e9, DataFrame_HSChucVu, mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_HSChucVu_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_HSChucVu.txt", "w+")#ghi ???? l??n
            print(DataFrame_HSChucVu_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_HSChucVu.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryChucVu.delete(0,END)
            entryHSCongViec.delete(0,END)
            entryChenSau.delete(0,END)        

        def Chen_Cuoi():
            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryChucVu.get()
            e2 = entryHSCongViec.get()

            #Th???c Hi???n tr??n DataFrame_HSChucVu:
            mautinmoi = pd.DataFrame([[e1,e2]], columns= DataFrame_HSChucVu.columns)
            #mautinmoi = pd.DataFrame([[e1,e2]], columns= ['ChucVu','HSCongViec'])
            DataFrame_HSChucVu_New = DataFrame_HSChucVu.append(mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_HSChucVu_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_HSChucVu.txt", "w+")#ghi ???? l??n
            print(DataFrame_HSChucVu_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_HSChucVu.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryChucVu.delete(0,END)
            entryHSCongViec.delete(0,END)

        #----------------------------------------

        btnXoaMauTin = tk.Button(gr2, text="X??a M???u Tin", command = Xoa_Mau_Tin)
        btnXoaMauTin.grid(row = 4, column = 0, ipadx = 15, ipady = 1.5)

        btnChenTruoc = tk.Button(gr2, text="Ch??n tr?????c", command = Chen_Truoc)
        btnChenTruoc.grid(row = 4, column = 1, ipadx = 15, ipady = 1.5)


        btnChenSau = tk.Button(gr2, text="Ch??n sau", command = Chen_Sau)
        btnChenSau.grid(row = 4, column = 2, ipadx = 15, ipady = 1.5)

        btnChenCuoi = tk.Button(gr2, text="Ch??n ??? Cu???i", command = Chen_Cuoi)
        btnChenCuoi.grid(row = 4, column = 3, ipadx = 15, ipady = 1.5)
        

        formChucVu.pack()
        
class formChiTiet(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("TH??NG TIN CHI TI???T")

        gr2 = tk.LabelFrame(self, padx = 20, pady = 15, text ="Th??ng Tin")
        gr2.pack(padx = 17, pady = 12)

        tk.Label(gr2, text="M?? Nh??n Vi??n").grid(row = 0, column = 0)
        entryMaNhanVien = tk.Entry(gr2)
        entryMaNhanVien.grid(row =1,column=0,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ch???c V???").grid(row = 0, column = 1)
        entryChucVu = tk.Entry(gr2)
        entryChucVu.grid(row =1,column=1,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="HS L????ng").grid(row = 0, column = 2)
        entryHSLuong = tk.Entry(gr2)
        entryHSLuong.grid(row =1,column=2,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="M???c ????? C??ng Vi???c").grid(row = 0, column = 3)
        entryMucDoCongViec = tk.Entry(gr2)
        entryMucDoCongViec.grid(row=1,column=3,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="X??a m???u tin th???:").grid(row = 2, column = 0)
        entryXoaMauTin = tk.Entry(gr2)
        entryXoaMauTin.grid(row =3,column=0,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ch??n v??o tr?????c m???u tin th???:").grid(row = 2, column = 1)
        entryChenTruoc = tk.Entry(gr2)
        entryChenTruoc.grid(row =3,column=1,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ch??n v??o sau m???u tin th???:").grid(row = 2, column = 2)
        entryChenSau = tk.Entry(gr2)
        entryChenSau.grid(row =3,column=2,sticky=tk.W,padx=5,pady=5)

        gr3 = tk.LabelFrame(self, padx = 20, pady = 15, text = "B???ng Chi Ti???t")
        gr3.pack(padx = 17, pady = 12)

        my_text = tk.Text(gr3)
        my_text.grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)
        text_file = open("Python_ChiTiet.txt","r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

        #------------- Functions ----------------

        def Xoa_Mau_Tin():
            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryXoaMauTin.get()
            e2 = int(e1)

            #Th???c Hi???n tr??n DataFrame_ChiTiet:
            DataFrame_ChiTiet_New = DataFrame_ChiTiet.drop(DataFrame_ChiTiet.index[[e2]])

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_ChiTiet_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_ChiTiet.txt", "w+")#ghi ???? l??n
            print(DataFrame_ChiTiet_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_ChiTiet.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryXoaMauTin.delete(0,END)

        # H??m ch??n d??ng b???t k??? v??o DataFrame
        #https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value): 
            # Starting value of upper half 
            start_upper = 0
            # End value of upper half 
            end_upper = row_number 
            # Start value of lower half 
            start_lower = row_number 
            # End value of lower half 
            end_lower = df.shape[0] 
            # Create a list of upper_half index 
            upper_half = [*range(start_upper, end_upper, 1)] 
            # Create a list of lower_half index 
            lower_half = [*range(start_lower, end_lower, 1)] 
            # Increment the value of lower half by 1 
            lower_half = [x.__add__(1) for x in lower_half] 
            # Combine the two lists 
            index_ = upper_half + lower_half 
            # Update the index of the dataframe 
            df.index = index_ 
            # Insert a row at the end 
            df.loc[row_number] = row_value 
            # Sort the index labels 
            df = df.sort_index() 
            # return the dataframe 
            return df 

        def Chen_Truoc():
            #row_number, DataFrame_ChiTiet, row_value

            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryMaNhanVien.get()
            e2 = entryChucVu.get()
            e3 = entryHSLuong.get()
            e4 = entryMucDoCongViec.get()
            
            e8 = entryChenTruoc.get()
            e9 = int(e8)

            #Th???c Hi???n tr??n DataFrame_ChiTiet:
            #List_ChiTiet.insert(e9, )
            #mautinmoi = pd.DataFrame([[e1,e2,e3,e4]], columns= DataFrame_ChiTiet.columns)
            mautinmoi = [e1,e2,e3,e4]
            DataFrame_ChiTiet_New = Insert_row(e9, DataFrame_ChiTiet, mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_ChiTiet_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_ChiTiet.txt", "w+")#ghi ???? l??n
            print(DataFrame_ChiTiet_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_ChiTiet.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryMaNhanVien.delete(0,END)
            entryChucVu.delete(0,END)
            entryHSLuong.delete(0,END)
            entryMucDoCongViec.delete(0,END)
            entryChenTruoc.delete(0,END)  

        def Chen_Sau():
            #row_number, DataFrame_ChiTiet, row_value

            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryMaNhanVien.get()
            e2 = entryChucVu.get()
            e3 = entryHSLuong.get()
            e4 = entryMucDoCongViec.get()
            
            e8 = entryChenSau.get()
            e9 = int(e8) + 1

            #Th???c Hi???n tr??n DataFrame_ChiTiet:
            #List_ChiTiet.insert(e9, )
            #mautinmoi = pd.DataFrame([[e1,e2,e3,e4]], columns= DataFrame_ChiTiet.columns)
            mautinmoi = [e1,e2,e3,e4]
            DataFrame_ChiTiet_New = Insert_row(e9, DataFrame_ChiTiet, mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_ChiTiet_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_ChiTiet.txt", "w+")#ghi ???? l??n
            print(DataFrame_ChiTiet_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_ChiTiet.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryMaNhanVien.delete(0,END)
            entryChucVu.delete(0,END)
            entryHSLuong.delete(0,END)
            entryMucDoCongViec.delete(0,END)
            entryChenSau.delete(0,END)

        def Chen_Cuoi():
            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryMaNhanVien.get()
            e2 = entryChucVu.get()
            e3 = entryHSLuong.get()
            e4 = entryMucDoCongViec.get()

            #Th???c Hi???n tr??n DataFrame_ChiTiet:
            mautinmoi = pd.DataFrame([[e1,e2,e3,e4]], columns= DataFrame_ChiTiet.columns)
            #mautinmoi = pd.DataFrame([[e1,e2,e3,e4]], columns= ['MaNV','ChucVu','HSLuong','MucDoCongViec'])
            DataFrame_ChiTiet_New = DataFrame_ChiTiet.append(mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_ChiTiet_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_ChiTiet.txt", "w+")#ghi ???? l??n
            print(DataFrame_ChiTiet_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_ChiTiet.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryMaNhanVien.delete(0,END)
            entryChucVu.delete(0,END)
            entryHSLuong.delete(0,END)
            entryMucDoCongViec.delete(0,END)        

        #----------------------------------------

        btnXoaMauTin = tk.Button(gr2, text="X??a M???u Tin", command = Xoa_Mau_Tin)
        btnXoaMauTin.grid(row = 4, column = 0, ipadx = 15, ipady = 1.5)

        btnChenTruoc = tk.Button(gr2, text="Ch??n tr?????c", command = Chen_Truoc)
        btnChenTruoc.grid(row = 4, column = 1, ipadx = 15, ipady = 1.5)


        btnChenSau = tk.Button(gr2, text="Ch??n sau", command = Chen_Sau)
        btnChenSau.grid(row = 4, column = 2, ipadx = 15, ipady = 1.5)

        btnChenCuoi = tk.Button(gr2, text="Ch??n ??? Cu???i", command = Chen_Cuoi)
        btnChenCuoi.grid(row = 4, column = 3, ipadx = 15, ipady = 1.5)
        

        formChiTiet.pack()
        
class formPhongBan(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("TH??NG TIN PH??NG BAN")

        gr2 = tk.LabelFrame(self, padx = 20, pady = 15, text ="Th??ng Tin")
        gr2.pack(padx = 17, pady = 12)

        tk.Label(gr2, text="M?? Ph??ng Ban").grid(row = 0, column = 0)
        entryMaPhongBan = tk.Entry(gr2)
        entryMaPhongBan.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="T??n Ph??ng Ban").grid(row = 0, column = 1)
        entryTenPhongBan = tk.Entry(gr2)
        entryTenPhongBan.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="X??a m???u tin th???:").grid(row = 2, column = 0)
        entryXoaMauTin = tk.Entry(gr2)
        entryXoaMauTin.grid(row =3,column=0,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ch??n v??o tr?????c m???u tin th???:").grid(row = 2, column = 1)
        entryChenTruoc = tk.Entry(gr2)
        entryChenTruoc.grid(row =3,column=1,sticky=tk.W,padx=5,pady=5)

        tk.Label(gr2, text="Ch??n v??o sau m???u tin th???:").grid(row = 2, column = 2)
        entryChenSau = tk.Entry(gr2)
        entryChenSau.grid(row =3,column=2,sticky=tk.W,padx=5,pady=5)

        gr3 = tk.LabelFrame(self, padx = 20, pady = 15, text = "B???ng Ph??ng Ban")
        gr3.pack(padx = 17, pady = 12)

        my_text = tk.Text(gr3)
        my_text.grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)
        text_file = open("Python_PhongBan.txt","r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

        #------------- Functions ----------------

        def Xoa_Mau_Tin():
            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryXoaMauTin.get()
            e2 = int(e1)

            #Th???c Hi???n tr??n DataFrame_PhongBan:
            DataFrame_PhongBan_New = DataFrame_PhongBan.drop(DataFrame_PhongBan.index[[e2]])

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_PhongBan_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_PhongBan.txt", "w+")#ghi ???? l??n
            print(DataFrame_PhongBan_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_PhongBan.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryXoaMauTin.delete(0,END)

        # H??m ch??n d??ng b???t k??? v??o DataFrame
        #https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value): 
            # Starting value of upper half 
            start_upper = 0
            # End value of upper half 
            end_upper = row_number 
            # Start value of lower half 
            start_lower = row_number 
            # End value of lower half 
            end_lower = df.shape[0] 
            # Create a list of upper_half index 
            upper_half = [*range(start_upper, end_upper, 1)] 
            # Create a list of lower_half index 
            lower_half = [*range(start_lower, end_lower, 1)] 
            # Increment the value of lower half by 1 
            lower_half = [x.__add__(1) for x in lower_half] 
            # Combine the two lists 
            index_ = upper_half + lower_half 
            # Update the index of the dataframe 
            df.index = index_ 
            # Insert a row at the end 
            df.loc[row_number] = row_value 
            # Sort the index labels 
            df = df.sort_index() 
            # return the dataframe 
            return df 

        def Chen_Truoc():
            #row_number, DataFrame_PhongBan, row_value

            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryMaPhongBan.get()
            e2 = entryTenPhongBan.get()
            
            e8 = entryChenTruoc.get()
            e9 = int(e8)

            #Th???c Hi???n tr??n DataFrame_PhongBan:
            #List_PhongBan.insert(e9, )
            #mautinmoi = pd.DataFrame([[e1,e2]], columns= DataFrame_PhongBan.columns)
            mautinmoi = [e1,e2]
            DataFrame_PhongBan_New = Insert_row(e9, DataFrame_PhongBan, mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_PhongBan_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_PhongBan.txt", "w+")#ghi ???? l??n
            print(DataFrame_PhongBan_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_PhongBan.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryMaPhongBan.delete(0,END)
            entryTenPhongBan.delete(0,END)
            entryChenTruoc.delete(0,END)  

        def Chen_Sau():
            #row_number, DataFrame_PhongBan, row_value

            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryMaPhongBan.get()
            e2 = entryTenPhongBan.get()
            
            e8 = entryChenTruoc.get()
            e9 = int(e8) + 1

            #Th???c Hi???n tr??n DataFrame_PhongBan:
            #List_PhongBan.insert(e9, )
            #mautinmoi = pd.DataFrame([[e1,e2]], columns= DataFrame_PhongBan.columns)
            mautinmoi = [e1,e2]
            DataFrame_PhongBan_New = Insert_row(e9, DataFrame_PhongBan, mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_PhongBan_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_PhongBan.txt", "w+")#ghi ???? l??n
            print(DataFrame_PhongBan, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_PhongBan.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryMaPhongBan.delete(0,END)
            entryTenPhongBan.delete(0,END)
            entryChenSau.delete(0,END)        

        def Chen_Cuoi():
            #?????t t??n cho n???i dung c???a c??c entry:
            e1 = entryMaPhongBan.get()
            e2 = entryTenPhongBan.get()

            #Th???c Hi???n tr??n DataFrame_PhongBan:
            mautinmoi = pd.DataFrame([[e1,e2]], columns= DataFrame_PhongBan.columns)
            #mautinmoi = pd.DataFrame([[e1,e2]], columns= ['MaPhongBan','TenPhongBan'])
            DataFrame_PhongBan_New = DataFrame_PhongBan.append(mautinmoi)

            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #print(DataFrame_PhongBan_New)

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_PhongBan.txt", "w+")#ghi ???? l??n
            print(DataFrame_PhongBan_New, file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_PhongBan.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            #x??a n???i dung trong c??c entry:
            entryMaPhongBan.delete(0,END)
            entryTenPhongBan.delete(0,END)

        #----------------------------------------

        btnXoaMauTin = tk.Button(gr2, text="X??a M???u Tin", command = Xoa_Mau_Tin)
        btnXoaMauTin.grid(row = 4, column = 0, ipadx = 15, ipady = 1.5)

        btnChenTruoc = tk.Button(gr2, text="Ch??n tr?????c", command = Chen_Truoc)
        btnChenTruoc.grid(row = 4, column = 1, ipadx = 15, ipady = 1.5)


        btnChenSau = tk.Button(gr2, text="Ch??n sau", command = Chen_Sau)
        btnChenSau.grid(row = 4, column = 2, ipadx = 15, ipady = 1.5)

        btnChenCuoi = tk.Button(gr2, text="Ch??n ??? Cu???i", command = Chen_Cuoi)
        btnChenCuoi.grid(row = 4, column = 3, ipadx = 15, ipady = 1.5)
        

        formPhongBan.pack()
        
class formCau5(tk.Toplevel):
    #MaNV, Ho, Ten, Phai, ChucVu, Luong, MaPB
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("C??U 5")

        gr2 = tk.LabelFrame(self, padx = 20, pady = 15, text ="????? B??i")
        gr2.pack(padx = 17, pady = 12)

        tk.Label(gr2, text="Cho ph??p xem trong 1 form g???m c??c field:").grid(row = 0, column = 0)
        tk.Label(gr2, text="MaNV, Ho, Ten, Phai, ChucVu, Luong, MaPB").grid(row = 1, column = 0)
        tk.Label(gr2, text="Trong ????: Luong = HSLuong*250.000").grid(row = 2, column = 0)
        tk.Label(gr2, text="K???t qu??? s???p x???p t??ng d???n theo MaPB, c??ng MaPB s???p t??ng d???n theo MaNV").grid(row = 3, column = 0)

        gr3 = tk.LabelFrame(self, padx = 20, pady = 15, text ="Th???c Thi C??u 5")
        gr3.pack(padx = 17, pady = 12)

        my_text = tk.Text(gr3)
        my_text.grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)

        def Cau5_CacField(): 
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)
            #Inner join dfNhanVien v???i DfChiTiet: column chung ????? join l?? "MaNV"
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            #L???c l???i nh???ng c???t c???n s??? d???ng:
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])            
            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau5.txt", "w")#ghi ???? l??n
            print(mergedDf_2, file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau5.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def Cau5_TinhLuong():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)
            #Inner join dfNhanVien v???i DfChiTiet: column chung ????? join l?? "MaNV"
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            #L???c l???i nh???ng c???t c???n s??? d???ng:
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])            
            #T??nh Luong = HSLuong*250000:
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x) 
            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau5.txt", "w")#ghi ???? l??n
            print(mergedDf_3, file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau5.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def Cau5_SapXep():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)
            #Inner join dfNhanVien v???i DfChiTiet: column chung ????? join l?? "MaNV"
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            #L???c l???i nh???ng c???t c???n s??? d???ng:
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])            
            #T??nh Luong = HSLuong*250000:
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x) 
            #S???p x???p t??ng d???n theo MaPB, c??ng MaPB th?? s???p t??ng d???n theo MaNV:
            mergedDf_4 = mergedDf_3.sort_values(by=["MaPB","MaNV"])
            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau5.txt", "w")#ghi ???? l??n
            print(mergedDf_4, file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau5.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        btnBangDau = tk.Button(gr2, text="C??c field y??u c???u", command = Cau5_CacField)
        btnBangDau.grid(row = 4, column = 1, ipadx = 15, ipady = 1.5)

        btnTinhLuong = tk.Button(gr2, text="T??nh L????ng", command = Cau5_TinhLuong)
        btnTinhLuong.grid(row = 4, column = 2, ipadx = 15, ipady = 1.5)

        btnSapXep = tk.Button(gr2, text="S???p X???p", command = Cau5_SapXep)
        btnSapXep.grid(row = 4, column = 3, ipadx = 15, ipady = 1.5)

        formCau5.pack()    

class formCau6(tk.Toplevel):
    
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("C??U 6")

        gr2 = tk.LabelFrame(self, padx = 20, pady = 15, text ="????? B??i")
        gr2.pack(padx = 17, pady = 12)

        tk.Label(gr2, text="Cho ph??p xem trong 1 form nh???ng ng?????i c?? l????ng cao nh???t g???m c??c field:").grid(row = 0, column = 0)
        tk.Label(gr2, text="MaNV, Ho, Ten, Phai, ChucVu, Luong, MaPB").grid(row = 1, column = 0)

        gr3 = tk.LabelFrame(self, padx = 20, pady = 15, text ="Th???c Thi C??u 6")
        gr3.pack(padx = 17, pady = 12)

        my_text = tk.Text(gr3)
        my_text.grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)

        def Cau6_CacField_Luong():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)
            #Inner join dfNhanVien v???i DfChiTiet: column chung ????? join l?? "MaNV"
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            #L???c l???i nh???ng c???t c???n s??? d???ng:
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])            
            #T??nh Luong = HSLuong*250000:
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x) 
            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau6.txt", "w")#ghi ???? l??n
            print(mergedDf_3, file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau6.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def Cau6_LuongCaoNhat():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)
            #Inner join dfNhanVien v???i DfChiTiet: column chung ????? join l?? "MaNV"
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            #L???c l???i nh???ng c???t c???n s??? d???ng:
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])            
            #T??nh Luong = HSLuong*250000:
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x) 

            #s???p x???p l????ng gi???m d???n
            mergedDf_4 = mergedDf_3.sort_values(by=["HSLuong"], ascending=False)

            #DF nh???ng ng?????i c?? l????ng cao nh???t
            #mergedDf_4 = mergedDf_3.loc[mergedDf_3["HSLuong"].idxmax(axis=1)]
            mergedDf_5 = mergedDf_4.head(10)
            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau6.txt", "w")#ghi ???? l??n
            print(mergedDf_5, file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau6.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()            

        btnBangDau = tk.Button(gr2, text="C??c field y??u c???u", command = Cau6_CacField_Luong)
        btnBangDau.grid(row = 4, column = 1, ipadx = 15, ipady = 1.5)

        btnTinhLuong = tk.Button(gr2, text="Ng?????i c?? l????ng cao nh???t c??ng ty", command = Cau6_LuongCaoNhat)
        btnTinhLuong.grid(row = 4, column = 2, ipadx = 15, ipady = 1.5)

        formCau6.pack()      

class formCau7(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("C??U 7")

        gr2 = tk.LabelFrame(self, padx = 20, pady = 15, text ="????? B??i")
        gr2.pack(padx = 17, pady = 12)

        tk.Label(gr2, text="Cho ph??p xem trong 1 form nh???ng ng?????i c?? l????ng cao nh???t c???a t???ng ph??ng ban g???m c??c field:").grid(row = 0)
        tk.Label(gr2, text="MaNV, Ho, Ten, Phai, ChucVu, Luong, MaPB").grid(row = 1)

        gr3 = tk.LabelFrame(self, padx = 20, pady = 15, text ="Th???c Thi C??u 7")
        gr3.pack(padx = 17, pady = 12)

        my_text = tk.Text(gr3)
        my_text.grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)

        def Cau7_TinhLuong():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)
            #Inner join dfNhanVien v???i DfChiTiet: column chung ????? join l?? "MaNV"
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            #L???c l???i nh???ng c???t c???n s??? d???ng:
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])            
            #T??nh Luong = HSLuong*250000:
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x) 
            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau7.txt", "w")#ghi ???? l??n
            print(mergedDf_3, file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau7.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def Cau7_LuongCaoNhatTheoPhong():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #Th???c hi???n h???p Nh??n Vi??n VS Chi Ti???t -> l???c nh???ng c???t c???n s??? d???ng -> t??nh l????ng
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])            
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x) 
            
            #L???c ra nh??n vi??n c???a ph??ng ban KH 
            option_KH = ['KH']
            mergedDf_KH = mergedDf_3[mergedDf_3['MaPB'].isin(option_KH)]#l???c nh??n vi??n KH
            KH_HSLuongmax = mergedDf_KH["HSLuong"].max()#HSLuong l???n nh???t trong KH
            option_KH_HSLuongmax = [KH_HSLuongmax]
            mergedDf_KH_HSLuongmax = mergedDf_KH[mergedDf_KH['HSLuong'].isin(option_KH_HSLuongmax)]#nh???ng ng?????i l????ng l???n nh???t trong KH

            #L???c ra nh??n vi??n c???a ph??ng ban KT
            option_KT = ['KT']
            mergedDf_KT = mergedDf_3[mergedDf_1['MaPB'].isin(option_KT)]#l???c nh??n vi??n KT
            KT_HSLuongmax = mergedDf_KT["HSLuong"].max()#HSLuong l???n nh???t trong KT
            option_KT_HSLuongmax = [KT_HSLuongmax]
            mergedDf_KT_HSLuongmax = mergedDf_KT[mergedDf_KT['HSLuong'].isin(option_KT_HSLuongmax)]#nh???ng ng?????i l????ng l???n nh???t trong KT

            #TC
            option_TC = ['TC']
            mergedDf_TC = mergedDf_3[mergedDf_1['MaPB'].isin(option_TC)]
            TC_HSLuongmax = mergedDf_TC["HSLuong"].max()
            option_TC_HSLuongmax = [TC_HSLuongmax]
            mergedDf_TC_HSLuongmax = mergedDf_TC[mergedDf_TC['HSLuong'].isin(option_TC_HSLuongmax)]#nh???ng ng?????i l????ng l???n nh???t trong TC

            #TK
            option_TK = ['TK']
            mergedDf_TK = mergedDf_3[mergedDf_1['MaPB'].isin(option_TK)]
            TK_HSLuongmax = mergedDf_TK["HSLuong"].max()
            option_TK_HSLuongmax = [TK_HSLuongmax]
            mergedDf_TK_HSLuongmax = mergedDf_TK[mergedDf_TK['HSLuong'].isin(option_TK_HSLuongmax)]#nh???ng ng?????i l????ng l???n nh???t trong TK

            #VP
            option_VP = ['VP']
            mergedDf_VP = mergedDf_3[mergedDf_1['MaPB'].isin(option_VP)]
            VP_HSLuongmax = mergedDf_VP["HSLuong"].max()
            option_VP_HSLuongmax = [VP_HSLuongmax]
            mergedDf_VP_HSLuongmax = mergedDf_VP[mergedDf_VP['HSLuong'].isin(option_VP_HSLuongmax)]#nh???ng ng?????i l????ng l???n nh???t trong VP

            Df_Cau7_1 = mergedDf_KH_HSLuongmax.append(mergedDf_KT_HSLuongmax)
            Df_Cau7_2 = Df_Cau7_1.append(mergedDf_TC_HSLuongmax) 
            Df_Cau7_3 = Df_Cau7_2.append(mergedDf_TK_HSLuongmax)
            Df_Cau7_4 = Df_Cau7_3.append(mergedDf_VP_HSLuongmax)
            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau7.txt", "w")#ghi ???? l??n
            print(Df_Cau7_4,file=f)

            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau7.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        btnTinhLuong = tk.Button(gr2, text="C??c Field y??u c???u", command = Cau7_TinhLuong)
        btnTinhLuong.grid(row = 4, column = 1, ipadx = 15, ipady = 1.5)

        btnMaxLuongPB = tk.Button(gr2, text="L????ng Cao Nh???t Theo PB", command = Cau7_LuongCaoNhatTheoPhong)
        btnMaxLuongPB.grid(row = 4, column = 2, ipadx = 15, ipady = 1.5)     

        formCau7.pack()

class formCau8(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("C??U 8")

        gr2 = tk.LabelFrame(self, padx = 20, pady = 15, text ="????? B??i")
        gr2.pack(padx = 17, pady = 12)

        tk.Label(gr2, text="Cho ph??p xem trong 1 form k???t qu??? th???ng k?? nh?? sau:").grid(row = 0, column = 0)
        tk.Label(gr2, text="TenPB, SoNam, SoNu, TongSo").grid(row = 1)

        gr3 = tk.LabelFrame(self, padx = 20, pady = 15, text ="Th???c Thi C??u 8")
        gr3.pack(padx = 17, pady = 12)

        my_text = tk.Text(gr3)
        my_text.grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)

        def Cau8_ThongKe():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #Th???c hi???n h???p Ph??ng Ban VS Nh??n Vi??n
            mergedDf_1 = DataFrame_PhongBan.merge(DataFrame_NhanVien)
            
            #KH
            option_KH = ['KH']
            mergedDf_KH = mergedDf_1[mergedDf_1['MaPB'].isin(option_KH)]
            #mergedDf_KH = mergedDf_1.apply(lambda x: True if x['MaPB'] == "KH" else False, axis = 1)#l???c nh??n vi??n thu???c KH
            sl_KH_tongso = len(mergedDf_KH[mergedDf_KH == True].index)#t???ng s??? nh??n vi??n KH
            #mergedDf_KH_nam = mergedDf_1.apply(lambda x: True if (x['MaPB'] == "KH" & x['Phai'] == "0") else False)#l???c nh??n vi??n thu???c KH l?? nam
            option_KH_Nam = ['0']
            mergedDf_KH_Nam = mergedDf_KH[mergedDf_KH['Phai'].isin(option_KH_Nam)]
            sl_KH_Nam = len(mergedDf_KH_Nam[mergedDf_KH_Nam == True].index)#s??? l?????ng nh??n vi??n KH l?? nam
            #mergedDf_KH_nu = mergedDf_KH.apply(lambda x: True if x['Phai'] == "1" else False)#l???c nh??n vi??n thu???c KH l?? n???
            #sl_KH_nu = len(mergedDf_KH_nu[mergedDf_KH_nu == True].index)#s??? l?????ng nh??n vi??n KH l?? n???
            sl_KH_Nu = sl_KH_tongso - sl_KH_Nam

            #KT
            option_KT = ['KT']
            mergedDf_KT = mergedDf_1[mergedDf_1['MaPB'].isin(option_KT)]
            sl_KT_tongso = len(mergedDf_KT[mergedDf_KT == True].index)#t???ng s??? nh??n vi??n KT
            option_KT_Nam = ['0']
            mergedDf_KT_Nam = mergedDf_KT[mergedDf_KT['Phai'].isin(option_KT_Nam)]
            sl_KT_Nam = len(mergedDf_KT_Nam[mergedDf_KT_Nam == True].index)#s??? l?????ng nh??n vi??n KT l?? nam
            sl_KT_Nu = sl_KT_tongso - sl_KT_Nam

            #TC
            option_TC = ['TC']
            mergedDf_TC = mergedDf_1[mergedDf_1['MaPB'].isin(option_TC)]
            sl_TC_tongso = len(mergedDf_TC[mergedDf_TC == True].index)#t???ng s??? nh??n vi??n TC
            option_TC_Nam = ['0']
            mergedDf_TC_Nam = mergedDf_TC[mergedDf_TC['Phai'].isin(option_TC_Nam)]
            sl_TC_Nam = len(mergedDf_TC_Nam[mergedDf_TC_Nam == True].index)#s??? l?????ng nh??n vi??n TC l?? nam
            sl_TC_Nu = sl_TC_tongso - sl_TC_Nam

            #TK
            option_TK = ['TK']
            mergedDf_TK = mergedDf_1[mergedDf_1['MaPB'].isin(option_TK)]
            sl_TK_tongso = len(mergedDf_TK[mergedDf_TK == True].index)#t???ng s??? nh??n vi??n TK
            option_TK_Nam = ['0']
            mergedDf_TK_Nam = mergedDf_TK[mergedDf_TK['Phai'].isin(option_TK_Nam)]
            sl_TK_Nam = len(mergedDf_TK_Nam[mergedDf_TK_Nam == True].index)#s??? l?????ng nh??n vi??n TK l?? nam
            sl_TK_Nu = sl_TK_tongso - sl_TK_Nam

            #VP
            option_VP = ['VP']
            mergedDf_VP = mergedDf_1[mergedDf_1['MaPB'].isin(option_VP)]
            sl_VP_tongso = len(mergedDf_VP[mergedDf_VP == True].index)#t???ng s??? nh??n vi??n VP
            option_VP_Nam = ['0']
            mergedDf_VP_Nam = mergedDf_VP[mergedDf_VP['Phai'].isin(option_VP_Nam)]
            sl_VP_Nam = len(mergedDf_VP_Nam[mergedDf_VP_Nam == True].index)#s??? l?????ng nh??n vi??n VP l?? nam
            sl_VP_Nu = sl_VP_tongso - sl_VP_Nam

            #DATAFRAME M???I ch???a T??n Ph??ng Ban, S??? l?????ng nh??n vi??n, T???ng nam, T???ng n???
            #T???o list
            List_Cau8 = [('Phong Kinh te Ke hoach',sl_KH_Nam, sl_KH_Nu, sl_KH_tongso),
                        ('Phong Ke toan Tai chanh',sl_KT_Nam, sl_KT_Nu, sl_KT_tongso),
                        ('Phong To chuc Nhan so',sl_TC_Nam, sl_TC_Nu, sl_TC_tongso),
                        ('Phong Ky thuat Thiet ke',sl_TK_Nam, sl_TK_Nu, sl_TK_tongso),
                        ('Van phong Xi nghiep',sl_VP_Nam, sl_VP_Nu, sl_VP_tongso)]
            DataFrame_Cau8 = pd.DataFrame.from_records(List_Cau8, columns = ['TenPB','SoNam','SoNu','TongSo'])

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau8.txt", "w")#ghi ???? l??n
            print(DataFrame_Cau8,file=f)
            f.close()

            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau8.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        btnThongKe = tk.Button(gr2, text="Th???ng K??", command = Cau8_ThongKe)
        btnThongKe.grid(row = 4, column = 1, ipadx = 15, ipady = 1.5)

        formCau8.pack()

class formCau9(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("C??U 9")

        gr2 = tk.LabelFrame(self, padx = 20, pady = 15, text ="????? B??i")
        gr2.pack(padx = 17, pady = 12)

        tk.Label(gr2, text="Cho ph??p xem trong 1 form g???m c??c field:").grid(row = 0)
        tk.Label(gr2, text="MaNV, Ho, Ten, Phai, ChucVu, Luong, MaPB").grid(row = 1)
        tk.Label(gr2, text="Cu???i m???i ph??ng ban c?? t???ng k???t:").grid(row = 2)
        tk.Label(gr2, text="T???ng s??? NV, T???ng s??? Nam, T???ng s??? N???, T???ng L????ng").grid(row = 3)

        gr3 = tk.LabelFrame(self, padx = 20, pady = 15, text ="Th???c Thi C??u 9")
        gr3.pack(padx = 17, pady = 12)

        my_text = tk.Text(gr3)
        my_text.grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)

        def Cau9_PhongKH():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #Th???c hi???n h???p Nh??n Vi??n VS Chi Ti???t -> l???c nh???ng c???t c???n s??? d???ng -> t??nh l????ng
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x)

            #L???c ra nh??n vi??n c???a ph??ng ban KH
            option_KH = ['KH']
            mergedDf_KH = mergedDf_3[mergedDf_3['MaPB'].isin(option_KH)]
            sl_KH_tongso = len(mergedDf_KH[mergedDf_KH == True].index)#t???ng s??? nh??n vi??n KH
            option_KH_Nam = ['0']
            mergedDf_KH_Nam = mergedDf_KH[mergedDf_KH['Phai'].isin(option_KH_Nam)]
            sl_KH_Nam = len(mergedDf_KH_Nam[mergedDf_KH_Nam == True].index)#s??? l?????ng nh??n vi??n KH l?? nam
            sl_KH_Nu = sl_KH_tongso - sl_KH_Nam
            #T???ng L????ng:
            TongLuong_KH = sum(mergedDf_KH['HSLuong'])

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau9_PhongKH.txt", "w")#ghi ???? l??n
            print(mergedDf_KH,file=f)
            print("Tong so NV: ",sl_KH_tongso,file=f)
            print("Tong so Nam: ",sl_KH_Nam,file=f)
            print("Tong so Nu: ",sl_KH_Nu,file=f)
            print("Tong Luong: ",TongLuong_KH,file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau9_PhongKH.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def Cau9_PhongKT():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #Th???c hi???n h???p Nh??n Vi??n VS Chi Ti???t -> l???c nh???ng c???t c???n s??? d???ng -> t??nh l????ng
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x)

            #L???c ra nh??n vi??n c???a ph??ng ban KT
            option_KT = ['KT']
            mergedDf_KT = mergedDf_3[mergedDf_3['MaPB'].isin(option_KT)]
            sl_KT_tongso = len(mergedDf_KT[mergedDf_KT == True].index)#t???ng s??? nh??n vi??n KT
            option_KT_Nam = ['0']
            mergedDf_KT_Nam = mergedDf_KT[mergedDf_KT['Phai'].isin(option_KT_Nam)]
            sl_KT_Nam = len(mergedDf_KT_Nam[mergedDf_KT_Nam == True].index)#s??? l?????ng nh??n vi??n KT l?? nam
            sl_KT_Nu = sl_KT_tongso - sl_KT_Nam
            #T???ng L????ng:
            TongLuong_KT = sum(mergedDf_KT['HSLuong'])

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau9_PhongKT.txt", "w")#ghi ???? l??n
            print(mergedDf_KT,file=f)
            print("Tong so NV: ",sl_KT_tongso,file=f)
            print("Tong so Nam: ",sl_KT_Nam,file=f)
            print("Tong so Nu: ",sl_KT_Nu,file=f)
            print("Tong Luong: ",TongLuong_KT,file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau9_PhongKT.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()
        
        def Cau9_PhongTC():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #Th???c hi???n h???p Nh??n Vi??n VS Chi Ti???t -> l???c nh???ng c???t c???n s??? d???ng -> t??nh l????ng
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x)

            #L???c ra nh??n vi??n c???a ph??ng ban TC
            option_TC = ['TC']
            mergedDf_TC = mergedDf_3[mergedDf_3['MaPB'].isin(option_TC)]
            sl_TC_tongso = len(mergedDf_TC[mergedDf_TC == True].index)#t???ng s??? nh??n vi??n TC
            option_TC_Nam = ['0']
            mergedDf_TC_Nam = mergedDf_TC[mergedDf_TC['Phai'].isin(option_TC_Nam)]
            sl_TC_Nam = len(mergedDf_TC_Nam[mergedDf_TC_Nam == True].index)#s??? l?????ng nh??n vi??n TC l?? nam
            sl_TC_Nu = sl_TC_tongso - sl_TC_Nam
            #T???ng L????ng:
            TongLuong_TC = sum(mergedDf_TC['HSLuong'])

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau9_PhongTC.txt", "w")#ghi ???? l??n
            print(mergedDf_TC,file=f)
            print("Tong so NV: ",sl_TC_tongso,file=f)
            print("Tong so Nam: ",sl_TC_Nam,file=f)
            print("Tong so Nu: ",sl_TC_Nu,file=f)
            print("Tong Luong: ",TongLuong_TC,file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau9_PhongTC.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def Cau9_PhongTK():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #Th???c hi???n h???p Nh??n Vi??n VS Chi Ti???t -> l???c nh???ng c???t c???n s??? d???ng -> t??nh l????ng
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x)

            #L???c ra nh??n vi??n c???a ph??ng ban TK
            option_TK = ['TK']
            mergedDf_TK = mergedDf_3[mergedDf_3['MaPB'].isin(option_TK)]
            sl_TK_tongso = len(mergedDf_TK[mergedDf_TK == True].index)#t???ng s??? nh??n vi??n TK
            option_TK_Nam = ['0']
            mergedDf_TK_Nam = mergedDf_TK[mergedDf_TK['Phai'].isin(option_TK_Nam)]
            sl_TK_Nam = len(mergedDf_TK_Nam[mergedDf_TK_Nam == True].index)#s??? l?????ng nh??n vi??n TK l?? nam
            sl_TK_Nu = sl_TK_tongso - sl_TK_Nam
            #T???ng L????ng:
            TongLuong_TK = sum(mergedDf_TK['HSLuong'])

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau9_PhongTK.txt", "w")#ghi ???? l??n
            print(mergedDf_TK,file=f)
            print("Tong so NV: ",sl_TK_tongso,file=f)
            print("Tong so Nam: ",sl_TK_Nam,file=f)
            print("Tong so Nu: ",sl_TK_Nu,file=f)
            print("Tong Luong: ",TongLuong_TK,file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau9_PhongTK.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def Cau9_PhongVP():
            #x??a n???i dung trong text field tr?????c:
            my_text.delete("1.0",END)

            #Th???c hi???n h???p Nh??n Vi??n VS Chi Ti???t -> l???c nh???ng c???t c???n s??? d???ng -> t??nh l????ng
            mergedDf_1 = DataFrame_NhanVien.merge(DataFrame_ChiTiet)
            mergedDf_2 = mergedDf_1.filter(["MaNV","Ho","Ten","Phai","ChucVu","HSLuong","MaPB"])
            mergedDf_3 = mergedDf_2.apply(lambda x: x*250000 if x.name == 'HSLuong' else x)

            #L???c ra nh??n vi??n c???a ph??ng ban VP
            option_VP = ['VP']
            mergedDf_VP = mergedDf_3[mergedDf_3['MaPB'].isin(option_VP)]
            sl_VP_tongso = len(mergedDf_VP[mergedDf_VP == True].index)#t???ng s??? nh??n vi??n VP
            option_VP_Nam = ['0']
            mergedDf_VP_Nam = mergedDf_VP[mergedDf_VP['Phai'].isin(option_VP_Nam)]
            sl_VP_Nam = len(mergedDf_VP_Nam[mergedDf_VP_Nam == True].index)#s??? l?????ng nh??n vi??n VP l?? nam
            sl_VP_Nu = sl_VP_tongso - sl_VP_Nam
            #T???ng L????ng:
            TongLuong_VP = sum(mergedDf_VP['HSLuong'])

            #in n???i dung v???a x??? l?? v??o file text:
            f = open("Python_Cau9_PhongVP.txt", "w")#ghi ???? l??n
            print(mergedDf_VP,file=f)
            print("Tong so NV: ",sl_VP_tongso,file=f)
            print("Tong so Nam: ",sl_VP_Nam,file=f)
            print("Tong so Nu: ",sl_VP_Nu,file=f)
            print("Tong Luong: ",TongLuong_VP,file=f)
            f.close()
            #in n???i dung file text tr??n ra text field:
            text_file = open("Python_Cau9_PhongVP.txt","r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        btnPhongKH = tk.Button(gr2, text="Ph??ng KH", command = Cau9_PhongKH)
        btnPhongKH.grid(row = 4, column = 1, ipadx = 15, ipady = 1.5)

        btnPhongKT = tk.Button(gr2, text="Ph??ng KT", command = Cau9_PhongKT)
        btnPhongKT.grid(row = 4, column = 2, ipadx = 15, ipady = 1.5)

        btnPhongTC = tk.Button(gr2, text="Ph??ng TC", command = Cau9_PhongTC)
        btnPhongTC.grid(row = 4, column = 3, ipadx = 15, ipady = 1.5)

        btnPhongTK = tk.Button(gr2, text="Ph??ng TK", command = Cau9_PhongTK)
        btnPhongTK.grid(row = 4, column = 4, ipadx = 15, ipady = 1.5)

        btnPhongVP = tk.Button(gr2, text="Ph??ng VP", command = Cau9_PhongVP)
        btnPhongVP.grid(row = 4, column = 5, ipadx = 15, ipady = 1.5)

        formCau9.pack()

class Main(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("QU???N L?? L????NG C?? QUAN")
        self.pack(fill=BOTH, expand=1)
        #self.configure(background = 'pink')
  
        menubar = Menu(self.parent) #Menu: File , About
        self.parent.config(menu=menubar)
        #Menu g???m 2 ph???n: Y??u c???u ????? t??i + Exit
        #Y??u c???u ????? t??i: C??c c??u trong ????? ??n
        yeucaudetai = Menu(menubar, tearoff = 0)

        subMenu1 = Menu(yeucaudetai, tearoff=0)
        subMenu1.add_command(label="Nh??n Vi??n", command= self.open_formNhanVien)
        subMenu1.add_command(label="Chi Ti???t" , command= self.open_formChiTiet)
        subMenu1.add_command(label="Ch???c V???" , command= self.open_formChucVu)
        subMenu1.add_command(label="Ph??ng Ban" , command= self.open_formPhongBan)

        yeucaudetai.add_cascade(label = "M??? files", command = self.onOpen)
        yeucaudetai.add_separator()
        yeucaudetai.add_cascade(label = "M??? forms", menu = subMenu1, underline = 0)
        yeucaudetai.add_separator()
        yeucaudetai.add_cascade(label = "C??u 5", underline = 0, command = self.open_formCau5)
        yeucaudetai.add_separator()
        yeucaudetai.add_cascade(label = "C??u 6", underline = 0, command = self.open_formCau6)
        yeucaudetai.add_separator()
        yeucaudetai.add_cascade(label = "C??u 7", underline = 0, command = self.open_formCau7)
        yeucaudetai.add_separator()
        yeucaudetai.add_cascade(label = "C??u 8", underline = 0, command = self.open_formCau8)
        yeucaudetai.add_separator()
        yeucaudetai.add_cascade(label = "C??u 9", underline = 0, command = self.open_formCau9)
        yeucaudetai.add_separator()

        menubar.add_cascade(label = "Y??u c???u c???a ????? t??i", menu = yeucaudetai)
        menubar.add_cascade(label = "Exit", command = self.quit)
        
        #-----------------------------------------About:
        #aboutmenu = Menu(menubar, tearoff=0)
        #aboutmenu.add_command(label="B??i H?? Nhi - 18110168")
        #aboutmenu.add_command(label="Hu???nh Tr???n Th???o Nhi - 18110169")
        #menubar.add_cascade(label="Nh??m 3", menu=aboutmenu)

        #----------------------------------------MAIN FORM S??? C??-------------------------------------------------
        opts = { 'ipadx': 7, 'ipady': 7, 'fill': tk.BOTH } 

        label_emp = tk.Label(self, text=" ",font=("TkDefaultFont",15), wraplength=600)
        label_emp.pack(side=tk.TOP,**opts)
        label_z = tk.Label(self, text = "Tr?????ng ?????i h???c S?? Ph???m K??? Thu???t TP.HCM", font=("TkDefaultFont",15), wraplength=600)
        label_z.pack(side=tk.TOP, **opts)

        self.img = ImageTk.PhotoImage(Image.open("hcmute.jpg"))
        panel = tk.Label(self, image = self.img)
        panel.pack()

        label_a = tk.Label(self, text = "????? ??N CU???I K???", font=("TkDefaultFont",20),wraplength=600)
        label_a.pack(side=tk.TOP, **opts)
        label_b = tk.Label(self, text="PH???N M???M QU???N L?? L????NG C?? QUAN", font=("TkDefaultFont",23),wraplength=700)
        label_b.pack(side=tk.TOP, **opts)
        label_c = tk.Label(self, text="Gi???ng vi??n h?????ng d???n: Th???y Tr???n Ti???n ?????c", font=("TkDefaultFont",15), wraplength=600)
        label_c.pack(side=tk.TOP, **opts)
        label_d = tk.Label(self, text="Sinh vi??n th???c hi???n 1: B??i H?? Nhi - 18110168", font=("TkDefaultFont",15), wraplength=600)
        label_d.pack(side=tk.TOP, **opts)
        label_e = tk.Label(self, text="Sinh vi??n th???c hi???n 2: Hu???nh Tr???n Th???o Nhi - 18110169", font=("TkDefaultFont",15), wraplength=600)
        label_e.pack(side=tk.TOP, **opts)
        label_f = tk.Label(self, text="Th??nh ph??? H??? Ch?? Minh - Th??ng 12, n??m 2020", font=("TkDefaultFont",15), wraplength=600)
        label_f.pack(side=tk.TOP, **opts)

        self.pack(fill=BOTH, expand=1)

    def onOpen(self):
        filetypes = (("Plain text files", "*.txt"), ("Images", "*.jpg *.gif *.png"), ("All files", "*"))
        filename = fd.askopenfilename(title="Open file", initialdir="/", filetypes=filetypes)
        if filename:
            webbrowser.open(filename)
            filename.close()

    def open_formNhanVien(self):
        nhanvien = formNhanVien(self)
        nhanvien.grab_set()

    def open_formChiTiet (self):
        chitiet = formChiTiet(self)
        chitiet.grab_set()

    def open_formPhongBan (self):
        phongban = formPhongBan(self)
        phongban.grab_set()

    def open_formChucVu (self):
        chucvu = formChucVu(self)
        chucvu.grab_set()

    def open_formCau5(self):
        cau5 = formCau5(self)
        cau5.grab_set()

    def open_formCau6(self):
        cau6 = formCau6(self)
        cau6.grab_set()

    def open_formCau7(self):
        cau7 = formCau7(self)
        cau7.grab_set()

    def open_formCau8(self):
        cau8 = formCau8(self)
        cau8.grab_set()

    def open_formCau9(self):
        cau9 = formCau9(self)
        cau9.grab_set()


root = Tk()
Main(root)
root.geometry("700x620+100+100")
root.mainloop()
