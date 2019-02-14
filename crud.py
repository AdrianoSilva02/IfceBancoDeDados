# coding: utf-8  
import mysql.connector 

db = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "1234", database = "crud")

cursor = db.cursor() 
 
#inserindo usuários
nome = input("Insira um nome: ")
login = input("Insira um login: ")
senha = input("Insira uma senha: ") 
cursor.execute("INSERT INTO `crud`.`crud`(`nome`,`login`,`senha`) VALUES ('"+nome+"','"+login+"','"+senha+"')", (nome,login,senha))  
db.commit()

 
#Buscando usuários
login = input("Digite o login para busca: ")
#cursor.execute("SELECT `nome` FROM `crud`.`crud` WHERE login ='{}'").format('login')


# Buscando dados
cursor.execute("SELECT id, nome, login, senha FROM `crud`.`crud`")
for i, n, l, s in cursor.fetchall():
	print("id = %d\tnome = %s\tlogin = %s\tsenha = %s"%(i, n,a))


#resulatdo = cursor.fetchall()
#print('Usuário:')
#for linha in resultado:
#print(linha)
db.commit()

#atulizando usuarios
cursor.execute("UPDATE `crud`.`crud` SET nome = '{}'").format('nome') 


#Alterando dados
#cursor.execute("UPDATE usuarios set senha = MD5(senha)")
#db.commit()




#deletando usuários
#i = input('Digite o usuário que deseja deletar: ')
#for i in cursor.fetchall():
#cursor.execute("DELETE FROM `crud`.`crud` WHERE	id = %d"%(i))
#db.commit()


#cursor.execute("DELET FROM id FROM `crud`.`crud`")
#for i in cursor.fetchall():
#print("id = %d\t"%(i))
#db.commit()




db.close() 



 
