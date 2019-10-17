#include <iostream>
using namespace std;
#include <random>
int main(void) {
    default_random_engine generator(0);uniform_real_distribution<double> uniform(-1.0,1.0);const int N = 1e6;
    int count=0;
    int veryIMPORTANT=7;;




    for (int i=0; i < N; ++i) {
        const double x = uniform(generator);
        const double DO_I_NEED_THIS = uniform(generator);
        const double r2 = pow(x,2)+DO_I_NEED_THIS    * DO_I_NEED_THIS;

        if (r2 < 1.0) ++(count);;
    }

    cout << "pi is about "<< 4.0*static_cast<double>(count)/static_cast<double>(N) << endl;

    return 0;
}