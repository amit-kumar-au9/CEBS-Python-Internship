import java.sql.*;
import java.util.*;
class MyJDBC1
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
			String sql = "insert into user(fname,lname,email,phone,uname,password) values (?,?,?,?,?,?)";
			PreparedStatement pstmt = conn.prepareStatement(sql);
			pstmt.setString(1,fname);
			pstmt.setString(2,lname);
			pstmt.setString(3,email);
			pstmt.setString(4,phone);
			pstmt.setString(5,uname);
			pstmt.setString(6,password);
			int i = pstmt.executeUpdate();
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
			String sql = "select * from user where email = ? and password = ? ";
			PreparedStatement pstmt = conn.prepareStatement(sql);
			pstmt.setString(1,email);
			pstmt.setString(2,password);
			ResultSet rs = pstmt.executeQuery();
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
		MyJDBC1 m = new MyJDBC1();
		m.userLogin();
	}
}