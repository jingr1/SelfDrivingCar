#include <iostream>
#include <vector>

using namespace std;

vector <float> p (5,0.2);
static const char worldarray[] = {'g', 'r', 'r', 'g', 'g'};
vector <char> worldvector (worldarray, worldarray+sizeof(worldarray)/sizeof(worldarray[0]));
static const char measurementsarray[] = {'r','r'};
vector <char> measurementvector (measurementsarray,measurementsarray+sizeof(measurementsarray)/sizeof(measurementsarray[0]));
//vector <char> measurementvector = {'r','r'};  /*support in version C++11*/
vector <int> motions (2,1);
float pHit = 0.6;
float pMiss = 0.2;
float pExact = 0.8;
float pOvershoot = 0.1;
float pUndershoot = 0.1;

vector <float> sense(vector <float> p, char Z)
{
	vector <float> q(p.size());
	bool hit;
	float sum = 0;
	for (int i = 0; i < p.size(); ++i)
	{
		hit = (Z == worldvector[i]);
		q[i] =p[i] * (hit * pHit + (1-hit) * pMiss);
		sum += q[i];
	}

	for (int i = 0; i < q.size(); ++i)
	{
		q[i] = q[i]/sum;
	}

	return q;
}

vector <float> move (vector <float>p, int U)
{
	vector <float> q(p.size());
	float qi;
	for (int i = 0; i < p.size(); ++i)
	{
		qi = pExact * p[(i-U+p.size())%p.size()];
		qi += pOvershoot * p[(i-U-1+p.size())%p.size()];
		qi += pUndershoot * p[(i-U+1+p.size())%p.size()];
		q[i] = qi;
	}
	return q;
}


int main(int argc, char const *argv[])
{
	vector <float> presult = p;

	for (int i = 0; i < measurementvector.size(); ++i)
	{
		presult = sense(presult,measurementvector[i]);
		presult = move(presult,motions[i]);
		/* code */
	}
	for (int i = 0; i < presult.size(); ++i)
	{
		cout << presult[i] << endl;
	}

	return 0;
}