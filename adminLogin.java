package plg;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;

public class adminLogin extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
    }
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        PrintWriter out = response.getWriter();
        try {
            Connection con = db.getconnection();
            String id = request.getParameter("id");
            String pwd = request.getParameter("password");
            PreparedStatement ps = con.prepareStatement("select * from admin");
            ResultSet rs = ps.executeQuery();
            Boolean flag = false;
            while(rs.next()){
                
                String formId = (String)rs.getString(1);
                String formpwd = (String)rs.getString(2);
                if(id.equals(formId) && pwd.equals(formpwd)){
                    flag = true;
                    break;
                }
            }
            if(flag){
                RequestDispatcher rd = request.getRequestDispatcher("/verify.jsp");
                rd.forward(request, response);
            }
            else{
                
                out.println("Incorrect Credentials. Try Again!");
            }
        } catch (Exception ex) {
            
        }
        
    }

}
