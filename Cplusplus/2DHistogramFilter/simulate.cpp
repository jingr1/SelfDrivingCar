/**
	simulate.cpp

	Purpose: implements a Simulation class which
	simulates a robot living in a 2D world. Relies 
	on localization code from localizer.py 

	This file is incomplete! Your job is to make 
	this code work. 
*/

#include "localizer.cpp"
#include <algorithm>
#include <time.h>
// #include "helpers.cpp"

class Simulation {
	
private:
	vector <char> get_colors() {
		vector <char> all_colors;
		char color;
		int i,j;
		for (i=0; i<height; i++) {
			for (j=0; j<width; j++) {
				color = grid[i][j];
				/*InputIt find( InputIt first, InputIt last, const T& value ); 
				find value from[first, last),if no value in [first, last), return last*/
				if(std::find(all_colors.begin(), all_colors.end(), color) != all_colors.end()) {
				    /* v contains x */
				} else {
					all_colors.push_back(color);
					cout << "adding color " << color << endl;
				    /* v does not contain x */
				}
			}
		}
		colors = all_colors;
		num_colors = colors.size();
		return colors;
	}

	char get_observed_color()
	{

		int y = true_pose[0];
		int x = true_pose[1];

        char true_color = grid[y][x];
        char color;
        vector<char> possible_colors;
        srand(time(0));
        if (((float)rand() / RAND_MAX) < incorrect_sense_prob)
        {
        	colors = get_colors();
        	for (int i = 0; i < colors.size(); ++i)
        	{
        		color = colors[i];

	        	if(std::find(possible_colors.begin(), possible_colors.end(), color) != possible_colors.end()) 
	        	{
					/* v contains x */
				} 
				else if(color != true_color)
				{
					possible_colors.push_back(color);
					cout << "adding color " << color << endl;
				    /* v does not contain x */
				}
			}
			srand(unsigned(time(0)));
            color = possible_colors[rand()%possible_colors.size()];
        }
        else
        {
        	color = true_color;
        }
        return color;
	}

public: 
	vector < vector <char> > grid;
	vector < vector <float> > beliefs;

	float blur, p_hit, p_miss, incorrect_sense_prob;

	int height, width, num_colors;
	
	std::vector<int> true_pose;
	std::vector<int> prev_pose;

	vector <char> colors;
	Simulation(vector < vector<char> >, float, float, vector <int>);
	void Sense();
	void Move(int, int);

};

/**
Constructor for the Simulation class.
*/
Simulation::Simulation(vector < vector <char> > map, 
	float blurring,
	float hit_prob, 
	std::vector<int> start_pos
	) 
{
	grid = map;
	blur = blurring;
	p_hit = hit_prob;
	p_miss = 1.0;
	beliefs = initialize_beliefs(map);
	incorrect_sense_prob = p_miss / (p_hit + p_miss);
	true_pose = start_pos;
	prev_pose = true_pose;
	height = map.size();
	width = map[0].size();
}

void Simulation::Sense()
{
	char color = get_observed_color();
	beliefs = sense(color,grid,beliefs,p_hit,p_miss);
}

void Simulation::Move(int dy, int dx)
{
	int new_y = (true_pose[0] + dy + height) % height;
	int new_x = (true_pose[1] + dx + width) % width;
	prev_pose = true_pose;
	true_pose[0] = new_y;
	true_pose[1] = new_x;
	beliefs = move(dy, dx, beliefs, blur);
}
/**
You can test your code by running this function. 

Do that by first compiling this file and then 
running the output.
*/
// int main() {
	
// 	vector < vector <char> > map;
// 	vector <char> mapRow;
// 	int i, j, randInt;
// 	char color;
// 	std::vector<int> pose(2);

// 	for (i = 0; i < 4; i++)
// 	{
// 		mapRow.clear();
// 		for (j=0; j< 4; j++)
// 		{
// 			randInt = rand() % 2;
// 			if (randInt == 0 ) {
// 				color = 'r';
// 			} 
// 			else {
// 				color = 'g';
// 			}
// 			mapRow.push_back(color);
// 		}
// 		map.push_back(mapRow);
// 	}
// 	cout << "map is\n";
// 	Simulation simulation (map, 0.1, 0.9, pose);
// 	// simulation = Simulation(map, 0.1, 0.9, pose);
// 	cout << "initialization success!\n";
// 	show_grid(map);
// 	show_grid(simulation.beliefs);
// 	cout << "x, y = (" << simulation.true_pose[0] << ", " << simulation.true_pose[1] << ")" << endl;
// 	simulation.Sense();
// 	show_grid(simulation.beliefs);
// 	simulation.Move(1,1);
// 	show_grid(simulation.beliefs);
// 	return 0;
// }
