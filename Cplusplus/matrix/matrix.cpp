#include "matrix.h"
using namespace std;
Matrix::Matrix()
{
	vector< vector<float> > initial_grid(4, vector<float>(4,0));
	grid = initial_grid;
	rows = initial_grid.size();
	cols = initial_grid[0].size();
}

Matrix::Matrix(vector< vector<float> > initial_grid)
{
	grid = initial_grid;
	rows = initial_grid.size();
	cols = initial_grid[0].size();

}


void Matrix::setGrid(vector< vector<float> > new_grid)
{
	grid = new_grid;
	rows = new_grid.size();
	cols = new_grid[0].size();

}
std::vector< std::vector<float> > Matrix::getGrid()
{
	return grid;
}
vector<int>::size_type Matrix::getRows()
{
	return rows;

}
vector<int>::size_type Matrix::getCols()
{
	return cols;
}

Matrix Matrix::matrix_transpose() 
{
    std::vector< std::vector<float> > new_grid;
    std::vector<float> row;

    for (int i = 0; i < cols; i++) 
    {
        row.clear();

        for (int j = 0; j < rows; j++) 
        {
            row.push_back(grid[j][i]); 
        }
        new_grid.push_back(row);
    }

    return Matrix(new_grid);
}
Matrix Matrix::matrix_addition(Matrix other)
{
	vector< vector<float> > matrixsumresult(rows, vector<float>(cols, 0));
	if ((rows != other.getRows()) || (cols != other.getCols()))
	{
		throw invalid_argument("matrices are not the same size");
	}
	else
	{
		for (int row = 0; row < rows; ++row)
		{
			for (int col = 0; col < cols; ++col)
			{
				matrixsumresult[row][col] = grid[row][col]+other.getGrid()[row][col];
			}
		}
	}

	return Matrix(matrixsumresult);

}
void Matrix::matrix_print()
{
	cout << endl;
	for (int row = 0; row < rows; row++) 
	{
		for (int column = 0; column < cols; column++) 
		{
			cout << grid[row][column] << " ";
		}
		cout << endl;
	}
	cout << endl;
}