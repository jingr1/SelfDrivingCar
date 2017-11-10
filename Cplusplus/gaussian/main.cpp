#include <iostream>
#include "gaussian.h"

using namespace std;   /* avoid using namespaces in a header file*/
/*main*/
int main ()
{

    Gaussian mygaussian(30.0,20.0);
    Gaussian othergaussian(10.0,30.0);
    
    cout << "average " << mygaussian.getMu() << endl;
    cout << "evaluation " << mygaussian.evaluate(15.0) << endl;

    cout << "mul results sigma " << mygaussian.multiply(othergaussian).getSigma2() << endl;
    cout << "mul results average " << mygaussian.multiply(othergaussian).getMu() << endl;

    cout << "add results sigma " << mygaussian.add(othergaussian).getSigma2() << endl;
    cout << "add results average " << mygaussian.add(othergaussian).getMu() << endl;

    return 0;
}