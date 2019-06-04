import java.io.*;
import java.net.*;

public class Client{
	public static void main(String[] args){
		try{

			Socket s = new Socket("localhost", 9999);

			DataInputStream dis = new DataInputStream(s.getInputStream());
			DataOutputStream dout = new DataOutputStream(s.getOutputStream());
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

			String str="", str2 = "";

			while(!str.equals("stop")){
				str = br.readLine();
				dout.writeUTF(str);
				dout.flush();

				str2 = dis.readUTF();
				System.out.println("Server response-> : "+str2);
			}

			dout.close();
			s.close();
		}catch(Exception e){
			System.out.println(e);
		}
	}
}