
class Bicycle{
	public int gear;
	public int speed;

	public Bicycle(int gear, int speed){
		this.gear = gear;
		this.speed = speed;
	}

	public void applyBrake(int decrement){
		this.speed -= decrement;
	}
	public void speedUp(int increment){
		this.speed += increment;
	}
	public String toString(){
		return("No of gears " + this.gear + "and speed is "+ this.speed);
	}
}

class MountainBike extends Bicycle{
	public int seatHeight;

	public MountainBike(int gear, int speed, int seatHeight){
		super(gear, speed);
		this.seatHeight = seatHeight;
	}
	public void setSeatHeight(int newSeatHeight){
		this.seatHeight = newSeatHeight;
	}
	@Override
	public String toString(){
		return(super.toString() + " seatHeight "+ this.seatHeight);
	}
}


public class Inheritance{
	public static void main(String args[]){
		MountainBike m = new MountainBike(3, 120, 50);
		m.speedUp(200);
		System.out.println(m.toString());
	}	
}
