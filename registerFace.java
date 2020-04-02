package plg;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class registerFace extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String aadhar = request.getParameter("aadhar");
        String command = "D:\\Coding\\python\\FR\\venv\\Scripts\\python.exe D:/Coding/python/FR/registerFace.py "+aadhar;
        Process p = Runtime.getRuntime().exec(command);
        
        BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String line = "";
        int i = 0;        
        String message = "";
        while ((line = reader.readLine()) != null) {
            message += line;
        }
        request.setAttribute("message", message);
        RequestDispatcher rd = request.getRequestDispatcher("/registerFace.jsp");
        rd.forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
    }
}
