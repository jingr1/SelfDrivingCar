#ifndef MATRIX_H
#define MATRIX_H

#include <vector>
#include <iostream>
#include <stdexcept>
// Header file for the Matrix class

class Matrix 
{
/* 
**    Declare the following private variables:
**      a 2D float vector variable called grid
**      a vector size_type variable called rows
**      a vector size_type variable called cols
*/
	private:
    	std::vector< std::vector<float> > grid;
		std::vector<int>::size_type rows;
		std::vector<int>::size_type cols;

	public:
/*
** For the matrix class, you will need two constructor functions.
** 1. An empty constructor function
** 2. A constructor function that accepts a 2-dimensional vector
*/     
        Matrix();
		Matrix(std::vector< std::vector<float> >);

/*Declare set and get functions for the three private variables.*/

		void setGrid(std::vector< std::vector<float> >);
		std::vector< std::vector<float> > getGrid();
		std::vector<int>::size_type getRows();
		std::vector<int>::size_type getCols();

 /*Declare the matrix functions*/  
		Matrix matrix_transpose();
		Matrix matrix_addition(Matrix);
		void matrix_print();
    
};

#endif /*MATRIX_H*/