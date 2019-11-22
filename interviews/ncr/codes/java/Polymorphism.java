// method overloading

class MehotOverloading{
	static int Multiply(int a, int b){
		return (a*b); 
	}

	static double Multiply(double a, double b){
		return (a*b);
	}

	static int Multiply(int a, int b, int c){
		return(a*b); 
	}
}

class OperatorOverloading{
	void operator(int a, int b){
		System.out.println(a+b);
	}
	void operator(String a, String b){
		System.out.println(a+b);
	}
}

// Mehtod Overriding
class Base{
	void print(){
		System.out.println("Base Class");
	}
}
class Child1 extends Base{
	void print(){
		System.out.println("child Class1");
	}
}
class Child2 extends Base{
	void print(){
		System.out.println("Child Class 2");
	}
}

public class Polymorphism{
	public static void main(String args[]){
		MehotOverloading mo = new MehotOverloading();
		int a = mo.Multiply(2,3);
		System.out.println(a);
		double b = mo.Multiply(2.4,3.5);
		System.out.println(b);

		OperatorOverloading oo = new OperatorOverloading();
		oo.operator(2,3);
		oo.operator("a", "b");	

		Base c1 = new Child1();
		c1.print();
		Base c2 = new Child2();			
		c2.print();
	}
}