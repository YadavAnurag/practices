class BaseClass{
	static void fun(){
		System.out.println("A.fun()");
	}
}
class ChildClass extends BaseClass{
	static void fun(){
		System.out.println("B.fun()");
	}
}

public class ShadowingStaticFunction{
	public static void main(String args[]){
		BaseClass b = new ChildClass();
		b.fun();

		ChildClass c = new ChildClass();
		c.fun();
	}
}

class A { 
   static void fun() { 
      System.out.println("A.fun()"); 
   } 
} 
  
// class B extends A {  
//    static void fun() {    
//       System.out.println("B.fun()"); 
//    } 
// } 
  
// public class ShadowingStaticFunction { 
//    public static void main(String args[]) { 
//       A a = new B(); 
//       a.fun();  // prints A.fun() 
//    } 
// } 