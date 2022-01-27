import requests
from mysql import connector
from tabulate import tabulate

#open connection
db = connector.connect(
    host    = 'localhost',
    user    = 'root',
    passwd  = '',
    database= 'db_akademik_0556'
)

#dapatkan data API
def getDataEndpoint(endpoint):
    base_url = "https://api.abcfdab.cfd/"
    response = requests.get(base_url + endpoint)
    return response.json()
    
data = getDataEndpoint('students')
data_data = data['data']
dataHead = []
dataList = []
for d in data_data:
    for y,x in d.items():
        dataHead.append(y)
        dataList.append(x)
i = 0
Newlists = []
while i<len(dataList):
    Newlists.append(dataList[i:i+6])
    i+=6

head = dataHead[1:6]
    
def adddata():
    mycursor = db.cursor()
    for d in Newlists:
        q = tuple(d)
        mycursor.execute('INSERT INTO tbl_students_0556 (id, nim, nama, jk, jurusan, alamat) VALUES (%s,%s,%s,%s,%s,%s)', query ), 
    db.commit() 

# adddata() / Menambahankan data API ke Mysql Database

columnList=[]
dataLists = []
def getdata():
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM tbl_students_0556")
    myresult = mycursor.fetchall()
    listData=[]
    for i in myresult:
        for g in i:
            listData.append(g)

    i = 0
    while i<len(listData):
        dataLists.append(dataList[i:i+6])
        i+=6

def getColumn():
    mycursor = db.cursor()
    mycursor.execute("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='db_akademik_0556' AND `TABLE_NAME`='tbl_students_0556';")
    myresult = mycursor.fetchall()
    column = []
    for i in myresult:
        for g in i:
            column.append(g)

    for i in range(len(column)):
        column[i] = column[i].upper()
    columnList.append(column)

getdata()
getColumn()

dataFinal = columnList + dataLists
#Menampilkan Database
def Showdata():
    print(tabulate(dataFinal, headers='firstrow', tablefmt='grid'))

#Memberikan Batas Tampilan
def Limit():
    limit = int(input('Masukkan limit: '))
    dataLimit = dataFinal[0:limit+1]
    print(tabulate(dataLimit, headers='firstrow', tablefmt='grid'))

#Mencari Nim untuk ditampilkan
def searchNim():
    nim = str(input("Masukkan NIM: "))
    for x in dataFinal:
        check = nim in x
        if check == True:
            resList = x
            res = 'ada'
        else:
            res = 'none'
            
    if res == 'ada':
        hasil = []
        hasil.append(resList)
        dataBasedNim = columnList + hasil
        print(f'Data NIM {nim} ditemukan!')
        print(tabulate(dataBasedNim, headers='firstrow', tablefmt='grid'))
    
    else:
        fail = ['NA']
        empty =[]
        empty6 = fail*6
        empty.append(empty6)
        emptyFinal = columnList + empty
        print(f'Data NIM {nim} tidak ditemukan!')
        print(tabulate(emptyFinal, headers='firstrow', tablefmt='grid'))

#Membuat Daftar Menu    
def menu():
    menu = int(input(" 1. Tampilkan Semua data \n 2. Tampilkan data berdasarkan limit \n 3. Cari data berdasarkan NIM \n 0. Keluar \n Pilih menu> "))

    if menu == 1:
        Showdata()
    elif menu == 2:
        Limit()
    elif menu == 3:
        searchNim()
    elif menu == 0:
        exit()
    else:
        print('Masukkan pilihan yang benar')
        
while True:
    menu()