#BIBLIOTECAS
#-------------------------------------------

from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import Image, ImageTk

#-------------------------------------------

#-------------------------------------------

#nomes que vc quer no menu escolha
listSexo=["Masculino","Feminino"]

#FUNÇÕES
#-------------------------------------------
#INSERIR
#------------
def insert():
    #Pega os dados dos campos e joga na variavel
    rg = e_rg.get()
    name = e_name.get()
    phone = e_phone.get()
    # so jogar o método get direto na variavel do mysql, irá sem erro
    def teste():
        sexo = lb_sexo.get();
        if sexo == ("Masculino"):
            sexo = "1"
        elif sexo == ("Feminino"):
            sexo = "2"
        return sexo
    teste()
    sexo=teste()
    #-----------------------------------------------------------------
    #verifica se tem algum campo vazio
    if(rg=="" or name =="" or phone==""):
        MessageBox.showinfo("Erro", "Todos os campos são obrigatórios")
    else:
      #TESTA CONEXAO
      try:
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="crud_python")
        cursor = con.cursor()
        
        #CONEXAO OK
        l_baseoff_crud.place_forget()
        l_baseon_crud.place(x=824,y=10)
        
     
        #Decisão se o usuario é cadastrado ou não 
        try:
          cursor.execute("select rg from cadastro where rg  = '"+ e_rg.get() +"'")
          teste22 = cursor.fetchall()
          if e_rg.get() == (f"{teste22[0][0]}"):
              e_rg.delete(0, 'end')
              MessageBox.showinfo("Insert Status", "Usúario Já cadastrado")
              con.close();
              e_rg.delete(0, 'end')
              e_name.delete(0, 'end')
              e_phone.delete(0, 'end')
              lb_sexo.delete(0, 'end')
        except:
            #------------------------------
            cursor.execute("insert into cadastro values(default,'"+ rg + "','"+ name + "','"+ phone + "','"+ sexo + "')")
            cursor.execute("commit");
            #------------------------------------
            #Após confirmar, apaga as linhas
            e_rg.delete(0, 'end')
            e_name.delete(0, 'end')
            e_phone.delete(0, 'end')
            lb_sexo.delete(0, 'end')
            show()
            contagem()
            #-------------------------------
            #Janela, Inserido com sucesso
            MessageBox.showinfo("Insert Status", "Inserido Com Sucesso!")
            con.close();
            #------------------------------
      except:
          semconexao()
          MessageBox.showinfo("Erro de Conexão", "Sem conexao!")

#DELETAR
#------------  
def delete():
    if(e_rg.get() == ""):
        MessageBox.showinfo("Delete status", "RG não está inserido para delete")

    else:
      #TESTA CONEXAO
      try:
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="crud_python")
        cursor = con.cursor()

        #CONEXAO OK
        l_baseoff_crud.place_forget()
        l_baseon_crud.place(x=824,y=10)

        try:
          cursor.execute("select rg from cadastro where rg  = '"+ e_rg.get() +"'")
          teste22 = cursor.fetchall()
          
          if e_rg.get() == (f"{teste22[0][0]}"):
              cursor.execute("delete from cadastro where rg='"+ e_rg.get() +"'")
              cursor.execute("commit");
              con.close();
              #------------------------------------
              #------------------------------------
              #Após confirmar, apaga as linhas
              e_rg.delete(0, 'end')
              e_name.delete(0, 'end')
              e_phone.delete(0, 'end')
              lb_sexo.delete(0, 'end')
              show()
              contagem()
              #-------------------------------
              #Janela, Deletando com sucesso
              MessageBox.showinfo("Status", "Deletado com Sucesso")
              #------------------------------
              
        except:
          #-------------------------------
            #Janela, Não Encontrado
            MessageBox.showinfo("Status", "Não encontrado")
            con.close();
            contagem()
            show()
            #------------------------------
      except:
          semconexao()
          MessageBox.showinfo("Erro de Conexão", "Sem conexao!")

#ATUALIZAR
#------------
def update():
    rg = e_rg.get()
    name = e_name.get()
    phone = e_phone.get();

    # so jogar o método get direto na variavel do mysql, irá sem erro
    def teste():
        sexo = lb_sexo.get();
        if sexo == ("Masculino"):
            sexo = "1"
        elif sexo == ("Feminino"):
            sexo = "2"
        return sexo
    teste()
    sexo=teste()

    if(rg=="" or name =="" or phone=="" or lb_sexo==""):
        MessageBox.showinfo("Update Status", "Todos os campos são Obrigatórios")
    else:
      #TESTA CONEXAO
      try:
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="crud_python")
        cursor = con.cursor()

        #CONEXAO OK
        l_baseoff_crud.place_forget()
        l_baseon_crud.place(x=824,y=10)

        try:
          cursor.execute("select rg from cadastro where rg  = '"+ e_rg.get() +"'")
          teste27 = cursor.fetchall()
          
          if e_rg.get() == (f"{teste27[0][0]}"):
                cursor.execute("update cadastro set name='"+ name + "', phone='"+ phone + "', id_sexo='"+ sexo + "' where rg='"+ rg +"'")
                cursor.execute("commit");
                #------------------------------------
                #Após confirmar, apaga as linhas
                e_rg.delete(0, 'end')
                e_name.delete(0, 'end')
                e_phone.delete(0, 'end')
                lb_sexo.delete(0, 'end')
                contagem()
                show()
                #-------------------------------
                #Janela, Inserido com sucesso
                MessageBox.showinfo("Status", "Atualizado Com Sucesso")
                con.close();
                #------------------------------
#--------------------------------------------------------------
        except:
            #-------------------------------
            #Janela, Não Encontrado
            MessageBox.showinfo("Status", "Não encontrado")
            con.close();
            contagem()
            show()
            #------------------------------
      except:
          semconexao()
          MessageBox.showinfo("Erro de Conexão", "Sem conexao!")

#PEGAR
#------------
def get():
    if(e_rg.get() == ""):
        MessageBox.showinfo("Fetch status", "RG não está inserido para PEGAR")

    else:
      #TESTA CONEXAO
      try:
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="crud_python")
        cursor = con.cursor()

        #CONEXAO OK
        l_baseoff_crud.place_forget()
        l_baseon_crud.place(x=824,y=10)
        
        #Decisão se o usuario é cadastrado ou não 
        try:
          cursor.execute("select rg from cadastro where rg  = '"+ e_rg.get() +"'")
          teste26 = cursor.fetchall()
          
          if e_rg.get() == (f"{teste26[0][0]}"):
              #------------------------------------
              #Coloca os dados do banco de dados nas caixas de textos
              cursor.execute("select t.rg, t.name, t.phone, s.sexo from cadastro as t join sexo_pessoa as s on s.id = id_sexo where rg='"+ e_rg.get() +"' ")
              rows = cursor.fetchall()
              con.close();

              e_rg.delete(0, 'end')
              e_name.delete(0, 'end')
              e_phone.delete(0, 'end')
              lb_sexo.delete(0, 'end')

              for row in rows:
                e_rg.insert(0, row[0])
                e_name.insert(0, row[1])
                e_phone.insert(0, row[2])
                lb_sexo.insert(0, row[3])
            
              
              MessageBox.showinfo("Status", "Localizado com Sucesso")
        except:
        
          #-------------------------------
          #Janela, Não Encontrado
          MessageBox.showinfo("Status", "Não encontrado")
          e_rg.delete(0, 'end')
          e_name.delete(0, 'end')
          e_phone.delete(0, 'end')
          lb_sexo.delete(0, 'end')
          con.close();
          
          #------------------------------
      except:
          semconexao()
          MessageBox.showinfo("Erro de Conexão", "Sem conexao!")

#CARREGA PAINEL 
#------------
def show():
        
        l_im_lista.place_forget()
    
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="crud_python")
        #conexao()
        cursor = con.cursor()
        #------------------------------------
        #
        cursor.execute('''
        select t.id, t.rg, t.name, t.phone, p.sexo from cadastro as t
        join sexo_pessoa as p
        on p.id =  id_sexo
        ''')
        rows = cursor.fetchall()
        con.close()

        #Para deleletar a a lista depois que foi gerada
        tv.delete(*tv.get_children())
        
        for row in rows:
            tv.insert("","end",values=row)
            
    
        print("mostra Painel")

#CONTAGEM PESSOAS, HOMEMS E MULHERES
#------------
def contagem():
    
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="crud_python")
      
        #conexao()
        cursor = con.cursor()
        #------------------------------------
        #comando para contar quantos tem no mysql
        cursor.execute("select count(*) from cadastro")
        const = cursor.fetchall()
        cursor.execute("select count(*) from cadastro where id_sexo=1")
        const1 = cursor.fetchall()
        cursor.execute("select count(*) from cadastro where id_sexo=2")
        const2 = cursor.fetchall()
        con.close()
        texto_pessoa_contagem['text'] = const
        texto_homem_contagem['text'] = const1
        texto_mulher_contagem['text'] = const2
        #Para deleletar a contagem depois que foi mostrada
        #list1.delete(0, list1.size())
        #--------------------------------------
        #------------------------------------
        #for co in const:
            #num = ' '+str(co[0])+''
            #list1.insert(list1.size()+1, num)
      
        print("chegou ate aqui")

#SEMCONEXAO - Limpa e Define para 0 por estar sem conexao           
def semconexao():
    tv.delete(*tv.get_children())
    texto_pessoa_contagem['text'] = "0"
    texto_homem_contagem['text'] = "0"
    texto_mulher_contagem['text'] = "0"
    l_baseon_crud.place_forget()
    #CRIA A IMAGEM BANCO OFF
    l_baseoff_crud.place(x=824,y=10)

#VERIFICA CONEXAO
def conexao():
  global con
  
  try:
    l_baseoff_crud.place_forget()
    con = mysql.connect(host="localhost", user="root", password="", database="crud_python")
    #CRIA A IMAGEM BANCO OFF
    l_baseon_crud.place(x=824,y=10)
    
    contagem()
    show()
    print("TUDO OK")
    
  except:
      print("Sem conexão")
      semconexao()

#CONSULTA TABELA
def consulta(event=None):
    like= e_name1.get();
    if(like==""):
        MessageBox.showinfo("Status", "Campo Obrigatório")
    else:
      try:
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="crud_python")

        consulta = f'''select t.id, t.rg, t.name, t.phone, p.sexo from cadastro as t
        join sexo_pessoa as p
        on p.id =  id_sexo
        where t.rg like '%{e_name1.get().strip()}%' or t.name like '%{e_name1.get().strip()}%';'''
        cursor = con.cursor()
        cursor.execute(consulta)
        rows = cursor.fetchall()
        con.close()
        #Deleta todos os registros para não duplicar
        tv.delete(*tv.get_children())
        
        for row in rows:
            tv.insert("","end",values=row)
        

        #Apaga a entrada depois que executada
        e_name1.delete(0, 'end')
        l_im_lista.place(x=380,y=100)
      except:
          semconexao()
          MessageBox.showinfo("Erro de Conexão", "Sem conexao!")


#Função de pegar da tv e colocar nas caixas de texto
def GetValue(event):
    e_name.delete(0, END)
    e_rg.delete(0, END)
    lb_sexo.delete(0, END)
    e_phone.delete(0, END)
    

    row_id = tv.selection()[0]
    select = tv.set(row_id)
    
    e_rg.insert(0,select['rg'])
    e_name.insert(0,select['nome'])
    e_phone.insert(0,select['telefone'])
    lb_sexo.insert(0,select['sexo'])



#CONFIGURACÃO JANELA
#------------------------------------
root = Tk()
root.geometry("900x600+200+50");
root.iconbitmap("images/crud3.ico")
root.title("Sistema de CRUD");
#FRAME TELA PRINCIPAL
tela_principal = Frame(root, bg="#353535")
tela_principal.place(x=0,y=0,width=900,height=600)
#------------------------------------

#DENTRO TELA PRINCIPAL
#------------------------------------
#TITULO
texto = Label(tela_principal, text="Sistema de CRUD", font=("Arial Black",25),bg="#353535", fg="white")
texto.place(x=299, y=20)
#PARTE CRUD TITULO
#------------------------------------

texto_admin = Label(tela_principal, text="Administrador", font=("Arial Black",22),bg="#353535", fg="white")
texto_admin.place(x=29, y=95)
#CRIA IMAGEM ADMIN-CRUD
#-----------------------------------------------
im_admin_crud = Image.open('images/admin_crud.png')
im_admin_crud = im_admin_crud.resize((60,60), Image.ANTIALIAS)
im_admin_crud = ImageTk.PhotoImage(im_admin_crud)
#-----------------------------------------------
#CARREGA IMAGEM ADMIN-CRUD
#-----------------------------------------------
l_admin_crud= Label(tela_principal, image=im_admin_crud, compound=LEFT, anchor='nw', bg="#353535",bd=0,activebackground="#3b3b3b")
l_admin_crud.place(x=261,y=95)

#-----------------------------------------------

#TEXTOS
#-----------------------------------------------

#RG
rg = Label(tela_principal, text="RG", font =('Arial Black', 12), bg="#353535",fg="white")
rg.place(x=20,y=176)
#NOME
name = Label(tela_principal, text="Nome", font =('Arial Black', 12), bg="#353535",fg="white")
name.place(x=20,y=216)
#TELEFONE
phone = Label(tela_principal, text="Telefone", font =('Arial Black', 12), bg="#353535",fg="white")
phone.place(x=20,y=256);
#SEXO
nomesexo1 = Label(tela_principal, text="Sexo", font =('Arial Black', 12), bg="#353535",fg="white")
nomesexo1.place(x=20,y=296);

#CAMPOS CRUD
#-----------------------------------------------

#RG
e_rg = Entry(tela_principal, width=23,font=1)
e_rg.place(x=120, y=180)
#NOME
e_name = Entry(tela_principal, width=23,font=1)
e_name.place(x=120, y=220)
#TELEFONE
e_phone = Entry(tela_principal, width=23, font=1)
e_phone.place(x=120, y=260)
#ESCOLHA SEXO
lb_sexo = ttk.Combobox(tela_principal, values=listSexo, font=1)
lb_sexo.place(x=120,y=300, width=180)


#BOTÕES DE FUNÇÕES CRUD
#-----------------------------------------------
#CRIA IMAGEM INSERIR
#-----------------------------------------------
im_ml_botao = Image.open('images/botao_crud_inserir_1.png')
im_ml_botao  = im_ml_botao .resize((60,30), Image.ANTIALIAS)
im_ml_botao  = ImageTk.PhotoImage(im_ml_botao )
#-----------------------------------------------
#CARREGA IMAGEM INSERIR - BOTAO INSERIR
#-----------------------------------------------
l_ml_botao= Button(tela_principal, image=im_ml_botao, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b", command=insert)
l_ml_botao.place(x=20,y=349)

#-----------------------------------------------
#CRIA IMAGEM DELETAR
#-----------------------------------------------
im_ml_botao1 = Image.open('images/botao_crud_deletar.png')
im_ml_botao1  = im_ml_botao1.resize((60,30), Image.ANTIALIAS)
im_ml_botao1  = ImageTk.PhotoImage(im_ml_botao1 )
#-----------------------------------------------
#CARREGA IMAGEM DELETAR - BOTAO DELETAR
#-----------------------------------------------
l_ml_botao1= Button(tela_principal, image=im_ml_botao1, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b", command=delete)
l_ml_botao1.place(x=100,y=349)

#-----------------------------------------------
#CRIA IMAGEM EDITAR
#-----------------------------------------------
im_ml_botao2 = Image.open('images/botao_crud_atualizar.png')
im_ml_botao2  = im_ml_botao2.resize((60,30), Image.ANTIALIAS)
im_ml_botao2  = ImageTk.PhotoImage(im_ml_botao2 )
#-----------------------------------------------
#CARREGA IMAGEM EDITAR - BOTAO EDITAR
#-----------------------------------------------
l_ml_botao2= Button(tela_principal, image=im_ml_botao2, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b", command=update)
l_ml_botao2.place(x=180,y=349)


#-----------------------------------------------
#CRIA IMAGEM BUSCAR
#-----------------------------------------------
im_ml_botao3 = Image.open('images/botao_crud_buscar.png')
im_ml_botao3  = im_ml_botao3.resize((60,30), Image.ANTIALIAS)
im_ml_botao3  = ImageTk.PhotoImage(im_ml_botao3 )
#-----------------------------------------------
#CARREGA IMAGEM BUSCAR - BOTAO BUSCAR
#-----------------------------------------------
l_ml_botao3= Button(tela_principal, image=im_ml_botao3, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b", command=get)
l_ml_botao3.place(x=260,y=349)

#------------------------------------




#------------------------------------
#PARTE PESQUISA E PAINEL DE DADOS
#-----------------------------------------------

#CRIA IMAGEM Pesquisar
#-----------------------------------------------
im_ml_pesquisa = Image.open('images/pesquisab.png')
im_ml_pesquisa = im_ml_pesquisa.resize((30,30), Image.ANTIALIAS)
im_ml_pesquisa = ImageTk.PhotoImage(im_ml_pesquisa)
#-----------------------------------------------
#CARREGA IMAGEM Pesquisar
#-----------------------------------------------
l_ml_pesquisa= Button(tela_principal, image=im_ml_pesquisa, compound=LEFT, anchor='nw', 
bg="#353535",bd=0,activebackground="#353535", command=consulta)
l_ml_pesquisa.place(x=460,y=95)
#Pesquisa
e_name1 = Entry(tela_principal, width=32,bd=0,bg="#353535",fg="white", insertbackground="white",font=1)
e_name1.place(x=510, y=95)
#linha
ttk.Separator(tela_principal, orient=HORIZONTAL).place(x=510,y=120,  width=290)

#CRIA IMAGEM - LISTA
#-----------------------------------------------
im_lista = Image.open('images/lista.png')
im_lista = im_lista.resize((40,40), Image.ANTIALIAS)
im_lista = ImageTk.PhotoImage(im_lista)
#-----------------------------------------------
#CARREGA IMAGEM - LISTA
#-----------------------------------------------
l_im_lista= Button(tela_principal, image=im_lista, compound=LEFT, anchor='nw', bg="#353535",bd=0,activebackground="#3b3b3b", command=show)

#------------------------------------
#Janela Que mostra a janela dos dados do banco e sua quantidade de colunas
tv=ttk.Treeview(tela_principal,columns=("id","rg","nome","telefone","sexo"), show='headings')
tv.place(x=380, y=150)
#coluna
tv.column('id',minwidth=0,width=50)
tv.column('rg',minwidth=0,width=100)
tv.column('nome',minwidth=0,width=150)
tv.column('telefone',minwidth=0,width=100)
tv.column('sexo',minwidth=0,width=100)
#cabeçalho
tv.heading('id',text='ID')
tv.heading('rg',text='RG')
tv.heading('nome',text='Nome')
tv.heading('telefone',text='Telefone')
tv.heading('sexo',text='Sexo')

#linha
ttk.Separator(tela_principal, orient=HORIZONTAL).place(x=100,y=405,  width=700)


#-----------------------------------------------
#CRIA IMAGEM - BANCO DE DADOS OFF
#-----------------------------------------------
im_baseoff_crud = Image.open('images/bancooff2_crud.png')
im_baseoff_crud = im_baseoff_crud.resize((60,60), Image.ANTIALIAS)
im_baseoff_crud = ImageTk.PhotoImage(im_baseoff_crud)
#-----------------------------------------------
#CARREGA IMAGEM - BANCO DE DADOS OFF
#-----------------------------------------------
l_baseoff_crud= Button(tela_principal, image=im_baseoff_crud, compound=LEFT, anchor='nw', bg="#353535", bd=0,activebackground="#353535", command=conexao)

#CRIA IMAGEM - BANCO DE DADOS ON
#-----------------------------------------------
im_baseon_crud = Image.open('images/bancoon_crud.png')
im_baseon_crud = im_baseon_crud.resize((60,60), Image.ANTIALIAS)
im_baseon_crud = ImageTk.PhotoImage(im_baseon_crud)
#-----------------------------------------------
#CARREGA IMAGEM - BANCO DE DADOS ON
#-----------------------------------------------
l_baseon_crud= Label(tela_principal, image=im_baseon_crud, compound=LEFT, anchor='nw', bg="#353535")

#-----------------------------------------------




#-----------------------------------------------
#PARTE DE BAIXO - IMAGEM E CONTADOR DE PESSOAS, HOMENS E MULHERES

#CRIA IMAGEM PESSOA
#-----------------------------------------------
im_pessoa_crud= Image.open('images/pessoas_crud.png')
im_pessoa_crud = im_pessoa_crud.resize((100,100), Image.ANTIALIAS)
im_pessoa_crud = ImageTk.PhotoImage(im_pessoa_crud)
#-----------------------------------------------
#CARREGA IMAGEM PESSOA
#-----------------------------------------------
l_pessoa_crud= Label(tela_principal, image=im_pessoa_crud, compound=LEFT, anchor='nw', bg="#353535",bd=0,activebackground="#3b3b3b")
l_pessoa_crud.place(x=200,y=408)

linha_menu_p_nt = ttk.Separator(tela_principal, orient=HORIZONTAL)
linha_menu_p_nt.place(x=190, y=510,width=121)

texto_pessoa_contagem = Label(tela_principal, text=" ", font=("Arial Black",40),bg="#353535",fg="#feffff")
texto_pessoa_contagem .place(x=194,y=515, width=113)

#CRIA IMAGEM HOMEM
#-----------------------------------------------
im_homem_crud = Image.open('images/homem_crud.png')
im_homem_crud = im_homem_crud.resize((100,100), Image.ANTIALIAS)
im_homem_crud = ImageTk.PhotoImage(im_homem_crud)
#-----------------------------------------------
#CARREGA IMAGEM HOMEM
#-----------------------------------------------
l_homem_crud= Label(tela_principal, image=im_homem_crud, compound=LEFT, anchor='nw', bg="#353535",bd=0,activebackground="#3b3b3b")
l_homem_crud.place(x=400,y=408)

linha_menu_p_nt = ttk.Separator(tela_principal, orient=HORIZONTAL)
linha_menu_p_nt.place(x=390, y=510,width=121)

texto_homem_contagem = Label(tela_principal, text=" ", font=("Arial Black",40),bg="#353535",fg="#feffff")
texto_homem_contagem.place(x=394,y=515, width=113)

#CRIA IMAGEM MULHER
#-----------------------------------------------
im_mulher_crud = Image.open('images/mulher_crud.png')
im_mulher_crud  = im_mulher_crud .resize((100,90), Image.ANTIALIAS)
im_mulher_crud  = ImageTk.PhotoImage(im_mulher_crud )
#-----------------------------------------------
#CARREGA IMAGEM MULHER
#-----------------------------------------------
l_mulher_crud = Label(tela_principal, image=im_mulher_crud , compound=LEFT, anchor='nw', bg="#353535",bd=0,activebackground="#3b3b3b")
l_mulher_crud .place(x=600,y=413)

linha_menu_p_nt = ttk.Separator(tela_principal, orient=HORIZONTAL)
linha_menu_p_nt.place(x=590, y=510,width=121)

texto_mulher_contagem = Label(tela_principal, text=" ", font=("Arial Black",40),bg="#353535",fg="#feffff")
texto_mulher_contagem.place(x=594,y=515, width=113)

#---------------------------------------------------




#COMANDOS
root.bind('<Return>', consulta)
tv.bind('<Double-Button-1>',GetValue)

#TESTA CONEXAO PARA INICIAR
conexao()

root.mainloop()


       