#ifndef POINT2D_H
#define POINT2D_H

class Point2D{
	public:
		Point2D(){
			xVal = 0;
			yVal = 0;
		}
		Point2D(double x, double y){
			xVal = x;
			yVal = y;
		}

		void setX(double x){
			xVal = x;
		}
		void setY(double y){
			yVal = y;
		}

		double x(){
			return xVal;
		}
		double y(){
			return yVal;
		}

	private:
		double xVal;
		double yVal;

};

#endif