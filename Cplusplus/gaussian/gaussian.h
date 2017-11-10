#ifndef GAUSSIAN_H
#define GAUSSIAN_H

/*Class Declaration*/
class Gaussian
{
    //private:    /*By default, C++ makes all class variables and functions private.*/
        float mu, sigma2;

    public:

        // constructor functions
        Gaussian ();
        Gaussian (float, float);

        // change value of average and standard deviation 
        void setMu(float);
        void setSigma2(float);

        // output value of average and standard deviation
        float getMu();
        float getSigma2();

        // functions to evaluate 
        float evaluate (float);
        Gaussian multiply (Gaussian);
        Gaussian add (Gaussian);
};

#endif /*GAUSSIAN_H*/