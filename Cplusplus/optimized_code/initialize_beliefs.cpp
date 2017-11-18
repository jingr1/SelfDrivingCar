#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector< vector <float> > initialize_beliefs(vector< vector <char> > &grid) {
	// initialize variables for new grid
	// OPTIMIZATION: Which of these variables are necessary?
	// OPTIMIZATION: Reserve space in memory for vectors
    int height = grid.size();
	int width = grid[0].size();
	int i, j;
	float prob_per_cell;
  	vector< vector <float> > newGrid;
  	newGrid.reserve(height);
	vector<float> newRow;
	newRow.reserve(width);
	// calculate initial grid values
	prob_per_cell = 1.0 / ( (float) (height * width)) ;
	// store initial values in a new 2D grid with same size as grid
  	// OPTIMIZATION: Is there a way to get the same results 	// without nested for loops?

	for (j=0; j<width; j++) 
	{
		newRow.push_back(prob_per_cell);
	}
	for (i=0; i<height; i++) 
	{
		newGrid.push_back(newRow);
	}
	return newGrid;
}