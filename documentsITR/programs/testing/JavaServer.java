import java.io.*;
import java.net.*;

public class JavaServer{
	public static void main(String[] args){
		try{
			ServerSocket ss = new ServerSocket(8080, "127.0.0.1");
			System.out.println();
			Socket s = ss.accept();

			DataInputStream dis = new DataInputStream(s.getInputStream());
			DataOutputStream dout = new DataOutputStream(s.getOutputStream());
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

			String str = "", str2 = "";

			while(!str.equals("stop")){
				str = dis.readUTF();
				String[] numbers = str.split(" ");
				float num1 = Float.parseFloat(numbers[0]);
				float num2 = Float.parseFloat(numbers[1]);
				float total = num1+num2;
				System.out.println("Client numbers->  "+num1 + " "+ num2);
				System.out.println("Total-> "+total);

				str2 = br.readLine();
				dout.writeUTF("Total -> " + total);
				dout.flush();
			}

			dis.close();
			s.close();
			ss.close();
		}catch(Exception e){
			System.out.println(e);
		}
	}
}