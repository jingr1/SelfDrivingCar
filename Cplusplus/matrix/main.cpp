#include <iostream>
#include <vector>
#include "matrix.h"

int main () {
    
	// assign a 7x5 matrix to the variable initial_grid
    // all values in the matrix are 0.4
	std::vector <std:: vector <float> > 
	    initial_grid (7, std::vector <float>(5, 0.4));

    // Use the initial grid variable to instantiate a matrix object
    // The matrix object should be called matrixa
    Matrix matrixa(initial_grid);
    // Use the matrix_print() method to print out matrixa
    matrixa.matrix_print();
    // Print out the number of rows in matrixa. You will need
    // to use the getRows() function and std::cout
    std::cout << matrixa.getRows() << std::endl;
    // Print out the number of columns in matrixa 
    std::cout << matrixa.getCols() << std::endl;
    // Now you will use another 7x5 matrix called matrixb to 
    // give the results of the matrix_addition function
    
    // 7x5 2-dimensional vector with values 0.2
	std::vector <std:: vector <float> > 
	    second_grid (7, std::vector <float>(5, 0.2));
    
    // Instantiate an object called matrixb. Use the second_grid
    // variable as the input to initialize matrixb
    Matrix matrixb(second_grid);
    // Add matrixa and matrixb. Store the results in a new matrix
    // variable called matrixsum
    Matrix matrixsum = matrixa.matrix_addition(matrixb);
    //Matrix matrixsum(matrixa.matrix_addition(matrixb));
    // Print out the matrix contained in the matrixsum variable
    matrixsum.matrix_print();
    matrixa.matrix_transpose().matrix_print();
    return 0;	
}