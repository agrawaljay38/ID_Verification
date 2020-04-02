package plg;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class verify extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String command = "D:\\Coding\\python\\FR\\venv\\Scripts\\python.exe D:/Coding/python/FR/verification.py ";
        Process p = Runtime.getRuntime().exec(command);
        
        BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String line = "";
        int i = 0;        
        String message[] = new String[11];
        while ((line = reader.readLine()) != null) {
            message[i] = line;
            System.out.println(message[i]);
            i+=1;
        }
        request.setAttribute("message", message);
        RequestDispatcher rd = request.getRequestDispatcher("/verify.jsp");
        rd.forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
    }

}
