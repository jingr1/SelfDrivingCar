#include <iostream>
#include <vector>

using namespace std;


// function to print an integer matrix
void matrixprint(vector < vector <int> > inputmatrix) {

	for (int row = 0; row < inputmatrix.size(); row++) {
		for (int column = 0; column < inputmatrix[0].size(); column++) {
			cout << inputmatrix[row][column] << " ";
		}
		cout << endl;

	}
}

//function to add two matrices together
vector < vector <int> > matrixsum(vector < vector <int> > matrix1, vector < vector <int> > matrix2) {

	// declare a matrix with the same size as matrix1 and matrix2
	vector < vector <int> > matrixsumresult (matrix1.size(), vector <int> (matrix1[0].size(), 0));

	// iterate through matrix1 and assign the sum of each element to the results matrix
	for (int row = 0; row < matrix1.size(); row++) {
		for (int column = 0; column < matrix1[0].size(); column++) {
			matrixsumresult[row][column] = matrix1[row][column] + matrix2[row][column];
		}

	}

	return matrixsumresult;


}

vector <vector <int> > matrixT (vector <vector <int> > matrix)
{
	vector <vector <int> > matrixt (matrix[0].size(), vector <int> (matrix.size(), 0));
	for (int i = 0; i < matrix[0].size(); ++i)
	{
		for (int j = 0; j < matrix.size(); ++j)
		{
			matrixt[i][j] = matrix[j][i];
		}
	}
	return matrixt;
}

vector <vector <int> > matrixmul (vector <vector <int> > matrix1,vector <vector <int> > matrix2)
{
	// declare a matrix with the same row size as matrix1 and same colume size as matrix2
	vector < vector <int> > matrixmulresult (matrix1.size(), vector <int> (matrix2[0].size(), 0));
	if (matrix1[0].size() == matrix2.size())
	{
		for (int i = 0; i < matrix1.size(); ++i)
		{
			for (int j = 0; j < matrix2[0].size(); ++j)
			{
				for (int k = 0; k < matrix2.size(); ++k)
				{
					matrixmulresult[i][j] += matrix1[i][k]*matrixT(matrix2)[j][k];
				}
			}
		}

	}
	else
	{
		cout << "Multiplication of Matrix A with matrix B is only possible if the width of A is equal to the height of B" << endl;
	}

	return matrixmulresult;
}


int main(int argc, char const *argv[])
{
	vector < vector <int> > matrix1 (5, vector <int> (3, 1));
	vector < vector <int> > matrix2 (3, vector <int> (3, 5));
	//matrixprint(matrix1);
	//matrixprint(matrixT(matrix2));
	matrixprint(matrixmul(matrix1,matrix2));
	return 0;
}