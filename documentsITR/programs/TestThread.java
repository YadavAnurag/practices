class MultithreadClass implements Runnable{
	private Thread t;
	private String threadName;

	MultithreadClass(String name){
		threadName = name;
		System.out.println("Creating thread-> "+name);
	}

	public void run(){
		System.out.println("Running thread-> "+threadName);
		try{

			for(int i=0; i<4; i++){
				System.out.println("Thread "+threadName+ " "+i);
				Thread.sleep(0);
			}

		}catch(InterruptedException e){
			System.out.println("Thread "+ threadName + " interrupted");
		}
		System.out.println("Thread "+ threadName + " exiting");
	}

	public void start(){
		System.out.println("Starting "+threadName);
		if(t == null){
			t = new Thread(this, threadName);
			t.start();
		}
	}
}

public class TestThread{
	public static void main(String[] args){
		MultithreadClass M1 = new MultithreadClass("Thread-1");
		M1.start();

		MultithreadClass M2 = new MultithreadClass("Thread-2");
		M2.start();
	}
}