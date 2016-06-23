#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;

#define PI 3.1415926535

// double sin120 = sin(PI/2);
// double cos120 = cos(PI/2);
double sin120 = sin(2*PI/3);
double cos120 = cos(2*PI/3);
//double R;
//double r;
//map <long long, point> ;
//map <long long, point> ;

struct point {
	double x_index;
	double y_index;
	double z_index;
};

//half done
double distance(point A, point B){
	double x2 = pow(A.x_index-B.x_index,2);
	double y2 = pow(A.y_index-B.y_index,2);
	double z2 = pow(A.z_index-B.z_index,2);

	return sqrt(x2+y2+z2);
}

//half done
point rotate_120(point A, point B){
	point result;
	result.x_index = (cos120+pow(A.x_index,2)*(1-cos120))*B.x_index + 
					 (A.x_index*A.y_index*(1-cos120) - A.z_index*sin120)*B.y_index +
					 (A.x_index*A.z_index*(1-cos120) + A.y_index*sin120)*B.z_index;

	result.y_index = (A.y_index*A.x_index*(1-cos120)+A.z_index*sin120)*B.x_index + 

					 (cos120+pow(A.y_index,2)*(1-cos120))*B.y_index +

					 (A.y_index*A.z_index*(1-cos120)-A.x_index*sin120)*B.z_index;

	result.z_index = (A.z_index*A.x_index*(1-cos120) - A.y_index*sin120)*B.x_index + 
					 (A.z_index*A.y_index*(1-cos120) + A.x_index*sin120)*B.y_index + 
					 (cos120 + pow(A.z_index,2)*(1-cos120))*B.z_index;

	// result.z_index = ()
	// cout <<  (A.x_index*A.y_index*(1-cos120)+A.z_index*sin120) <<endl;
	// cout << sin120 << endl;
	// cout << (A.x_index*A.y_index*(1-cos120)+A.z_index*sin120)*B.x_index << "+" << (cos120+pow(A.y_index,2)*(1-cos120))*B.y_index <<
	// "+" << 	(A.y_index*A.z_index*(1-cos120)-A.x_index*sin120)*B.z_index << endl;

	// result.z_index = (A.z_index*A.x_index*(1-120))				 
	cout << result.x_index << endl;
	cout << result.y_index << endl;
	cout << result.z_index << endl;
	return result;
}
//half done
double rotate_240(point A){

	return A.x_index;
}

// void IOfunction(){
// 	int plist_number;
// 	cin >> plist_number;

// 	for (int i=0;i++;i<plist_number){

// 	}

// }

int main(){
	// IOfunction();
	point p0;
	point p1;
	// double x,y,z;
	cin >> p0.x_index;
	cin >> p0.y_index;
	cin >> p0.z_index;
	cin >> p1.x_index;
	cin >> p1.y_index;
	cin >> p1.z_index;	
	rotate_120(p0,p1);

	int K_index;
	int P_index;
	// point *K
	while 

	return 0;
}
