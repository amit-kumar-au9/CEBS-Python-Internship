import java.sql.*;
import java.util.*;
class MyJDBC 
{
	private static Scanner scan;
	static
	{
		scan = new Scanner(System.in);
	}
	public void userRegister()
	{
		try
		{
			System.out.print("Enter First Name : ");
			String fname = scan.nextLine();
			System.out.print("Enter Last Name : ");
			String lname = scan.nextLine();
			System.out.print("Enter Email : ");
			String email = scan.nextLine();
			System.out.print("Enter Phone : ");
			String phone = scan.nextLine();
			System.out.print("Enter User Name : ");
			String uname = scan.nextLine();
			System.out.print("Enter Password : ");
			String password = scan.nextLine();
			
			Class.forName("com.mysql.jdbc.Driver");
			Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/cebs-training","root","");
			Statement stmt = conn.createStatement();
			String sql = "insert into user(fname,lname,email,phone,uname,password) values ('"+fname+"','"+lname+"','"+email+"','"+phone+"','"+uname+"','"+password+"')";
			int i = stmt.executeUpdate(sql);
			if(i>0)
			{
				System.out.println("User Registered");
			}
			else
			{
				System.out.println("Sorry cant Register");
			}
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
		
	}
	public void userLogin()
	{
		try
		{
			System.out.print("Enter Email : ");
			String email = scan.nextLine();
			System.out.print("Enter Password : ");
			String password = scan.nextLine();
			
			Class.forName("com.mysql.jdbc.Driver");
			Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/cebs-training","root","");
			Statement stmt = conn.createStatement();
			String sql = "select * from user where email = '"+email+"' and password = '"+password+"' ";
			ResultSet rs = stmt.executeQuery(sql);
			if(rs.next())
			{
				System.out.println("Welcome : "+rs.getString("fname")+" "+rs.getString("lname"));
			}
			else
			{
				System.out.println("Invalid Email/Password");
			}
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
		
	}
	public static void main(String...s)
	{
		MyJDBC m = new MyJDBC();
		m.userLogin();
	}
}