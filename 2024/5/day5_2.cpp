#include <vector>
#include <fstream>
#include <sstream>
#include <map>
#include <unordered_set>
#include <algorithm>
#include <iostream>

int main() {
    std::ifstream file{"input.txt"};
    std::string line{};
    std::map<int, std::unordered_set<int>> relations; //Maps numbers that should follow each number; no repeats.
    auto compare = [&](int left, int right) {
        return relations[left].find(right) != relations[left].end();
    };
    int res{};
    while(std::getline(file, line)) {
        int num{};
        std::vector<int> numbers{};
        std::istringstream str{line};
        if(line.find('|') != std::string::npos) { //first section
            int left{}, right{};
            char bar_{};
            str >> left;
            str.ignore(); //bar
            str >> right;
            relations[left].insert(right);
        } else if(line.find(',') != std::string::npos) { //second section
            while (str >> num) {
                numbers.push_back(num);
                str.ignore(); //comma
            }
            if (!(std::is_sorted(numbers.begin(), numbers.end(), compare))) {
                std::sort(numbers.begin(), numbers.end(), compare);
                res += numbers[numbers.size()/2];
            }
        }
    }
    std::cout << res << std::endl;
    return 0;
}