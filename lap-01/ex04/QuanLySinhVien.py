from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generateID(self):
        maxID = 1
        if (self.soLuongSinhVien() > 0):
            maxID = self.listSinhVien[0].id
            for sv in self.listSinhVien:
                if (maxID < sv.id):
                    maxID = sv.id   
            maxID += 1
        return maxID
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def NhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập ngành học sinh viên: ")
        diemTB = float(input("Nhập điểm trung bình sinh viên: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, ID): 
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập ngành học sinh viên: ")
            diemTB = float(input("Nhập điểm trung bình sinh viên: "))
            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.diemTB = diemTB
            self.xepLoaiHocLuc(sv) 
        else:
            print("Sinh vien có ID {} không tồn tại.".format(ID))
    
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x.id, reverse=False)
    
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x.name, reverse=False)
        
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x.diemTB, reverse=False)
    
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv.id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv.name.upper()):
                    listSV.append(sv)                
        return listSV
    
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:SinhVien):                                             
        if (sv.diemTB >= 8):
            sv.hocLuc = "Giỏi"
        elif (sv.diemTB >= 6.5):    
            sv.hocLuc = "Khá"
        elif (sv.diemTB >= 5):    
            sv.hocLuc = "Trung bình"
        else:
            sv.hocLuc = "Yếu"
     
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "Điểm TB", "Học lực"))
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv.id, sv.name, sv.sex, sv.major, sv.diemTB, sv.hocLuc))
        print("\n")
        
    def getListSinhVien(self):
        return self.listSinhVien    
        