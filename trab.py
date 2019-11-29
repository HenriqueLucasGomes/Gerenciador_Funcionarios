#coding: utf-8
#author Henrique Lucas Gomes Rezende
contador=0

import sqlite3
conn=sqlite3.connect(r"C:\dev\trab_db\informacoes.db")

def adimiti(c):
    n=str(input("Nome:"))
    s=float(input("Salário:"))
    da=str(input("Data de hoje:"))
    conn.execute("insert into Informe(Nome,Salario,DataAD,Id) values('"+n+"',"+str(s)+","+str(da)+","+str(c)+")")
    conn.commit()

def procura():
    n=input("""
    Deseja realizar a busca pelo:
    1-Nome
    2-Número de registro
    """)
    return n

def demiti():
    p=int(procura())
    if(p==1):
        n=str(input("Nome:"))
        da=str(input("Data de hoje:"))
        conn.execute("update Informe set Situaçao='D' where Nome='"+n+"'")
        conn.execute("update Informe set DataDM='"+da+"' where Nome='"+n+"'")
        conn.commit()
    elif(p==2):
        id=int(input("Número de registro"))
        da=str(input("Data de hoje:"))
        conn.execute("update Informe set Situaçao='D' where Nome="+str(id)+"")
        conn.execute("update Informe set DataDM='"+da+"' where Nome="+str(id)+"")
        conn.commit()
    else:
        demiti()

def excluir():
    p=int(procura())
    if(p==1):
        n=str(input("Nome:"))
        conn.execute("delete from Informe where Nome ="+n)
        conn.commit()
    elif(p==2):
        id=int(input("Número de registro"))
        conn.execute("delete from Informe where id ="+str(id))
        conn.commit()
    else:
        excluir()

def consultar(rows):
    for i in rows:
        print("Nome: "+i[0])
        print("Codigo de identificação: "+str(i[1]))
        print("Sálario: "+str(i[2]))
        print("Data de Admissão: "+i[3])
        print("Data de Demissão: "+i[4])
        print("Situação: "+i[5])

def consultaN():
    n=str(input("Nome:"))
    cursor=conn.execute("select * from Informe where Nome='"+n+"'")
    rows=cursor.fetchall()
    consultar(rows)

def consultaC():
    i=str(input("Codigo de identificação:"))
    cursor=conn.execute("select * from Informe where Id="+i+"")
    rows=cursor.fetchall()
    consultar(rows)

i=None
while (i!=11):
    i=int(input("""
    adimitir-1
    demitir-2
    excluir-3
    consultar nome-4
    consulta id-5
    lista maior salario-6
    lista menor salario-7
    lista todos os salarios-8
    lista func ativos-9
    lista func inativos-10
    encerrar-11
    """))
    if(i==1):
        contador+=1
        adimiti(contador)
    elif(i==2):
        demiti()
    elif(i==3):
        pass
        excluir()
    elif(i==4):
        pass
        consultaN()
    elif(i==5):
        pass
        consultaC()
    elif(i==6):
        pass
        #salMenor()
    elif(i==7):
        pass
        #salMaior()
    elif(i==8):
        pass
        #totalSal()
    elif(i==9):
        pass
        #funcAtivos()
    elif(i==10):
        pass
        #funcInativos()
    elif(i==11):
        conn.close()
