#include <math.h>
#include "point3d.h"
Point3d::Point3d(double x, double y, double z){
    this -> x = x;
    this -> y = y;
    this -> z = z;
}

void Point3d::setX(double x){
    this -> x = x;
}

void Point3d::setY(double y){
    this -> y = y;
}

void Point3d::setZ(double z){
    this -> z = z;
}

void Point3d::shift(int axis, double distance){
    if (axis == 0){
        this -> x += distance;
    }
    if (axis == 1){
        this -> y += distance;
    }
    if (axis == 2){
        this -> z += distance;
    }
}

double Point3d::getX() const{
    return this -> x;
}

double Point3d::getY() const{
    return this -> y;
}

double Point3d::getZ() const{
    return this -> z;
}

bool operator == (const Point3d& p1, const Point3d& p2){
    return (p1.getX() == p2.getX() && 
    p1.getY() == p2.getY() && p1.getZ() == p2.getZ() );
};
double distance(const Point3d& p1, const Point3d& p2){
    double xD = p1.getX()-p2.getX();
    double yD = p2.getY()-p1.getY();
    double zD = p1.getZ()-p2.getZ();
    return sqrt(xD*xD+yD*yD+zD*zD);
};
