#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <map>
//NOT SOLVED. I GIVE UP.
//I tried different approaches but I seem to be missing some cases whatever I do :)
//Can't quite figure out what else could lead to loops.
int main() {
    std::ifstream file{"input.txt"};
    std::vector<std::string> grid{};
    std::string line{};
    
    while (std::getline(file, line)) {
        grid.push_back(line);
    }

    std::pair<int, int> curr{52, 36}; //Start pos: 6,4 for ex; 52,36 for input
    std::pair<int, int> next{};
    int dir{}; //0-N, 1-E, 2-S, 3-W
    std::set<std::pair<int, int>> visited{};
    std::map<std::pair<int, int>, std::set<int>> visited_dir{}; //the dir when we visited
    std::set<std::pair<int, int>> obstructions{};
    std::pair<int, int> tmp{};
    int tmp_dir{};
    std::map<std::pair<int, int>, std::set<int>> tmp_visited_dir{};
    
    while(1) {
        if(visited.insert(curr).second) { //set.insert(x).second returns false if x already in set. unvisited pos.
            visited_dir[curr].insert(dir);
        }
        tmp = curr;
        tmp_dir = (dir + 1) % 4; //right of facing.
        tmp_visited_dir = visited_dir;
        
        std::cout << "curr: " << curr.first << ", " << curr.second << std::endl;
        while(1) { //check if turning right would lead to previous part of path
            
            std::cout << "tmp: " << tmp.first << ", " << tmp.second << " char: " << grid[tmp.first][tmp.second] << std::endl;
            tmp = {tmp.first + (tmp_dir == 2) - (tmp_dir == 0),  //N: -1, S: +1
                    tmp.second + (tmp_dir == 1) - (tmp_dir == 3)}; //E: +1, W: -1
            
            if (!tmp_visited_dir[tmp].insert(tmp_dir).second) { //loop.
                std::cout << "-----------------------loop------------------" << std::endl;
                obstructions.insert({tmp.first + (tmp_dir == 2) - (tmp_dir == 0), 
                                    tmp.second + (tmp_dir == 1) - (tmp_dir == 3)});
                break;
            }

            if ((tmp.first == -1) || (tmp.first == grid.size()) //out of bounds
                ||(tmp.second == -1) || (tmp.second == grid.size())) {
                std::cout << "out of bounds" << std::endl;
                break;
            } else if(grid[tmp.first][tmp.second] == '#') {
                tmp_dir = (tmp_dir + 1) % 4;
            }

        }
        next = {curr.first + (dir == 2) - (dir == 0),  //N: -1, S: +1
                curr.second + (dir == 1) - (dir == 3)}; //E: +1, W: -1

        if ((next.first == -1) || (next.first == grid.size()) //out of bounds; done.
        ||(next.second == -1) || (next.second == grid.size())) {
            break;
        }
        
        switch(grid[next.first][next.second]) {
            case '#':
                dir = (dir + 1) % 4; //rotate
                break;
            case '.':
            case '^':
                curr = next;
                break;
        }
    }
    std::cout << obstructions.size() << std::endl;
    std::cout << visited.size() << std::endl;
    return 0;
}