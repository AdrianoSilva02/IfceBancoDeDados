package aulaDeBD;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import com.mysql.jdbc.PreparedStatement;

public class Conexao {

	public static void main(String[] args) {
		
        String url = "jdbc:mysql://localhost:3306/login"; //Nome da base de dados
        String user = "root"; //nome do usuário do MySQL
        String password = "ifce"; //senha do MySQL
		
        Connection conexao = null;        

        try {
			conexao = DriverManager.getConnection(url, user, password);
			
//			String sql = "insert into Usuarios (Nome, Login, Senha) values ('Jonas Rodrigues', 'Jonas', MD5('123'))";
//			conexao.prepareStatement(sql).execute();
			
			String sql = "SELECT * FROM Usuarios";
			ResultSet rs = conexao.prepareStatement(sql).executeQuery();
			 
			//Faz a verificação de enquanto conter registros, percorre e resgata os valores
			while(rs.next()){
				int id = rs.getInt("ID");
				String nome = rs.getString("Nome");
				String usuario = rs.getString("Login");
				String senha = rs.getString("Senha");
				
				System.out.println(nome+" "+usuario);
			}			
			
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
        
	}

}
