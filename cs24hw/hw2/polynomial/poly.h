#ifndef POLY_H
#define POLY_H
class poly
{
public:
static const int MAX = 10;
// CONSTRUCTORS
poly();// a polynomial with degree 0
poly(const int k, const double initial_coeff[] );
// MODIFICATION MEMBER FUNCTIONS
void set(const int k, const double coeff);// sets the kth coefficient
// CONSTANT MEMBER FUNCTIONS
int ddegree() const; //get the degree of the polynomial
double get(const int k ) const;// gets the kth coefficient
double evaluate (const double xval) const;//evaluates the polynomial
private:
    double data[MAX];
    int degree;
};
// NON-MEMBER FUNCTIONS
bool operator == (const poly& p1, const poly& p2);
#endif