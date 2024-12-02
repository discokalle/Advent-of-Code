#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>

int is_safe(const std::vector<int>& data) {
    bool increases{}, decreases{};
    int n1{}, n2{};
    for (size_t i = 0; i < data.size() - 1; ++i) {
            n1 = data[i];
            n2 = data[i+1];
            if (abs(n1 - n2) < 1 || abs(n1 - n2) > 3 || //diff outside accepted limits.
            (n1 < n2 && decreases) || (n1 > n2 && increases)) { //pattern has changed
                return 0; //unsafe
            }
            if (n1 < n2) increases = true;
            else if (n1 > n2) decreases = true;
        }
    return 1; //safe
}

int main() {
    std::ifstream file("input.txt");
    std::string line{};
    int res{};

    while (std::getline(file, line)) {
        std::istringstream str{line};
        int n1{}, n2{};
        bool increases{}, decreases{}, dampened{};
        std::vector<int> data{};

        while (str >> n1) {
            data.push_back(n1);
        }

        if(is_safe(data)) res += 1; //safe
        else {
            for(int i = 0; i < data.size(); ++i) {//Try removing every number.
                std::vector<int> new_data{data};
                new_data.erase(new_data.begin() + i); 
                if (is_safe(new_data)){
                    res += 1;
                    break;
                }
            }
        }
    }
    std::cout << res << std::endl;
    return 0;
}