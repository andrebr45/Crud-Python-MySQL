#Necessário
from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
#Só ira abrir depois que voce configurar seu banco dados  nas funções abaixo

def inserir():
    rg = e_rg.get()
    nome = e_nome.get()
    telefone = e_telefone.get();

    if(rg=="" or nome =="" or telefone==""):
        MessageBox.showinfo("Status", "Todos os Campos são exigidos")
    else:
        #Conexão e Entrada de dados no banco
        # (-- Mudar nome do banco de dados e suas configurações -- ) #
        con = mysql.connect(host="localhost", user="root", password="", database="teste")
        cursor = con.cursor()
        
        # (-- Mudar nome da tabela -- ) #
        cursor.execute("insert into cadastro values('"+ rg + "','"+ nome + "','"+ telefone + "')")

        cursor.execute("commit");
        #------------------------------------
        #Após confirmar, apaga as linhas
        e_rg.delete(0, 'end')
        e_nome.delete(0, 'end')
        e_telefone.delete(0, 'end')
        show()
        contagem()
        #-------------------------------
        #Janela, Inserido com sucesso
        MessageBox.showinfo("Status", "inserido com Sucesso")
        con.close();
        #------------------------------
    
def deletar():
    if(e_rg.get() == ""):
        MessageBox.showinfo("Status Deletar", "RG não está inserido para deletar")

    else:
        #Conexão e Entrada de dados no banco
        # (-- Mudar nome do banco de dados e suas configurações -- ) #
        con = mysql.connect(host="localhost", user="root", password="", database="teste")
        cursor = con.cursor()
        
        # (-- Mudar nome da tabela -- ) #
        cursor.execute("delete from cadastro where rg='"+ e_rg.get() +"'")

        cursor.execute("commit");
        #------------------------------------
        #Após confirmar, apaga as linhas
        e_rg.delete(0, 'end')
        e_nome.delete(0, 'end')
        e_telefone.delete(0, 'end')
        show()
        contagem()
        #-------------------------------
        #Janela, Deletando com sucesso
        MessageBox.showinfo("Status Deletar", "Deletado Com Sucesso")
        con.close();
        #------------------------------

def atualizar():
    rg = e_rg.get()
    nome = e_nome.get()
    telefone = e_telefone.get();

    if(rg=="" or nome =="" or telefone==""):
        MessageBox.showinfo("Status", "Todos os Campos são exigidos")
        
    else:
        #Conexão e Entrada de dados no banco
        # (-- Mudar nome do banco de dados e suas configurações -- ) #
        con = mysql.connect(host="localhost", user="root", password="", database="teste")
        cursor = con.cursor()
        # (-- Mudar nome da tabela -- ) #
        cursor.execute("update cadastro set name='"+ nome + "', phone='"+ telefone + "' where rg='"+ rg +"'")
        cursor.execute("commit");
        #------------------------------------
        #Após confirmar, apaga as linhas
        e_rg.delete(0, 'end')
        e_nome.delete(0, 'end')
        e_telefone.delete(0, 'end')
        show()
        contagem()
        #-------------------------------
        #Janela, Inserido com sucesso
        MessageBox.showinfo("Status Busca", "Atualizado Com Sucesso")
        con.close();
        #------------------------------

def pegar():
    if(e_rg.get() == ""):
        MessageBox.showinfo("Status Busca", "RG não está inserido para fazer a busca")
        

    else:
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="teste")
        cursor = con.cursor()
        #------------------------------------

        # (-- Mudar nome da tabela -- ) #
        cursor.execute("select * from cadastro where rg='"+ e_rg.get() +"'")
        rows = cursor.fetchall()
        for row in rows:
            e_nome.insert(0, row[1])
            e_telefone.insert(0, row[2])

        #-------------------------------
        #Janela, Encontrado com sucesso
        MessageBox.showinfo("Status Busca", "Localizado Com Sucesso")
        con.close();
        #------------------------------

def show():
        #Conexão e Entrada de dados no banco
        # (-- Mudar nome do banco de dados e suas configurações -- ) #
        con = mysql.connect(host="localhost", user="root", password="", database="teste")
        cursor = con.cursor()
        #------------------------------------

        # (-- Mudar nome da tabela -- ) #
        cursor.execute("select * from cadastro")

        rows = cursor.fetchall()
        #Para deleletar a a lista depois que foi gerada
        tv.delete(*tv.get_children())
        
        for row in rows:
            tv.insert("","end",values=row)
            
        con.close()

def contagem():
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="teste")
        cursor = con.cursor()
        #------------------------------------
        #comando para contar quantos tem no mysql

        # (-- Mudar nome da tabela -- ) #
        cursor.execute("select count(*) from cadastro")

        const = cursor.fetchall()
        #Para deleletar a contagem depois que foi mostrada
        list1.delete(0, list1.size())
        #--------------------------------------
       
        for co in const:
            num = ' '+str(co[0])+''
            list1.insert(list1.size()+1, num)
            
        con.close()

#Config da tela
root = Tk()
root.geometry("660x400");
root.title("Dev@Andre");
#Textos página
texto = Label(root, text="Gerenciador de Registros", font=("uppercase",20))
texto.place(x=150, y=20)

rg = Label(root, text="Entre com RG", font =('bold', 10))
rg.place(x=20,y=80)

nome = Label(root, text="Entre com NOME", font =('bold', 10))
nome.place(x=20,y=110)

telefone = Label(root, text="Entre com TEL", font =('bold', 10))
telefone.place(x=20,y=140)

textolist1 = Label(root, text="Quantidade Pessoas", font =('bold', 12))
textolist1.place(x=18,y=250);
#Entradas da caixa de texto
e_rg = Entry()
e_rg.place(x=141, y=80)

e_nome = Entry()
e_nome.place(x=141, y=110)

e_telefone = Entry()
e_telefone.place(x=141, y=140)
#Botões
binserir = Button(root, text="Inserir", font=("italic", 10), bg="white", command=inserir)
binserir.place(x=20, y=190)

bdeletar = Button(root, text="Deletar", font=("italic", 10), bg="white", command=deletar)
bdeletar.place(x=80, y=190)

batualizar = Button(root, text="Atualizar", font=("italic", 10), bg="white", command=atualizar)
batualizar.place(x=145, y=190)

bpegar = Button(root, text="Buscar", font=("italic", 10), bg="white", command=pegar)
bpegar.place(x=215, y=190, width=50)
#------------------------------------

#------------------------------------
#Janela da contagem do numero de pessoas no banco de dados
list1= Listbox(root)
list1.place(x=170,y=253, height=18, width=20)
contagem()
#------------------------------------
tv=ttk.Treeview(root,columns=("id","nome","telefone"), show='headings')
tv.place(x=380, y=80)
show()

tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=100)
tv.column('telefone',minwidth=0,width=100)

tv.heading('id',text='RG')
tv.heading('nome',text='Nome')
tv.heading('telefone',text='Telefone')


root.mainloop()