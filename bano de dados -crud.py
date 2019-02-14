




 # Importa os m�dulos necess�rios 'MySQLdb'
import MySQLdb, time

# Define endere�o do servidor, nome de usu�rio do bd, senha do usu�rio do bd e nome da base de dados
aServidor = "127.0.0.1"
aUsuario  = "root"
aSenha    = "1234"
aBanco    = "msql"

# Realiza a conex�o com o banco
db = MySQLdb.connect(aServidor, aUsuario, aSenha, aBanco)
cursor = db.cursor() # seta o cursor para a conex�o

# Fun��o que executa os comandos SQL no banco
def Executa_SQL(pSQL):
  try:
    cursor.execute(pSQL)
    db.commit()
  except:
    print("Erro: N�o foi poss�vel executar o SQL")
    db.rollback()

# Fun��o que executa comandos SQL (Select)
def Busca_SQL(pSQL):
  try:
    cursor.execute(pSQL)
    results = cursor.fetchall()
    return results
  except:
    print("Erro: N�o foi poss�vel buscar os dados")
    return 0


# Cria uma variavel com o SQL e chama a fun��o passando como parametro o SQL
vSQL = "CREATE TABLE IF NOT EXISTS USUARIO (NOME VARCHAR(50) NOT NULL, LOGIN VARCHAR(20), SENHA VARCHAR(20) )"
Executa_SQL(vSQL)

Executa_SQL("INSERT INTO USUARIO(NOME, LOGIN, SENHA) VALUES ('Kelvin S do Prado', 'Kelvin', 'Kelvin')")

# Chama a fun��o Busca_SQL passando o comando SQL como par�metro
vResultado = Busca_SQL("SELECT * FROM USUARIO WHERE LOGIN = 'Kelvin'")
for row in vResultado:
  # L� cada coluna de cada linha retornada do SELECT, come�ando pela coluna 0
  vNome  = row[0]
  vLogin = row[1]
  vSenha = row[2]

 print("Nome : " + vNome)
 print("Sobrenome : " + vLogin)
 print("Senha : " + vSenha+"\n")

Executa_SQL("UPDATE USUARIO SET NOME = 'Outro'")

# Chama a fun��o Busca_SQL passando o comando SQL como par�metro
vResultado = Busca_SQL("SELECT * FROM USUARIO WHERE LOGIN = 'Kelvin'")
for row in vResultado:
  vNome  = row[0]
  vLogin = row[1]
  vSenha = row[2]

 print("Nome : " + vNome)
 print("Sobrenome : " + vLogin)
 print("Senha : " + vSenha)

Executa_SQL("DELETE FROM USUARIO WHERE LOGIN = 'Kelvin'")

# Fecha a conex�o com o banco de dados
db.close()

time.sleep(3)