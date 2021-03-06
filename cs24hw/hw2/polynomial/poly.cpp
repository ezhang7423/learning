#include <math.h>
#include "poly.h"
poly::poly(){
    this -> degree = 0;
}

poly::poly(const int k, const double inital_coeff[] ){
    this -> degree = k ;
    for (int i = 1; i <= k; i++){
        this -> data[i] =  inital_coeff[i];
    }
}

void poly::set(const int k, const double coeff){
    this -> data[k] = this -> coeff;
}

int poly::degree() const{
    return this -> degree;
}
double poly::get(const int k) const{
    return this -> data[k];
}

double poly::evaluate(const double xval) const{
    double ans = 0;
    for (int i = 1; i <= this -> degree; i++){
        ans += pow(this -> data[i] * xval, i)
    }
    return ans;
}

bool operator == (const poly& p1, const poly& p2){
    if (p1.degree() != p2.degree()) return false;
    int deg = p1.degree();
    for (int i = 1; i <= deg; i++){
        if (p1.get(i) != p2.get(i)){
            return false;
        }
    }
    return true;
}