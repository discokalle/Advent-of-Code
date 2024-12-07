#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

bool search(const std::vector<long long>& nums, const long long& total) { //recursive search
    if (nums.size() == 1) return nums[0] == total; //Base case: last number
    auto try_operation = [&](const auto& op) { //tries * and +
        std::vector<long long> new_nums{nums};
        new_nums[1] = op(nums[0], nums[1]); //apply operation
        if (new_nums[1] > total) return false; //early termination check
        new_nums.erase(new_nums.begin()); //first 2 numbers replaced with result
        return search(new_nums, total); //recursive call 
    };
    return try_operation(std::multiplies<long long>()) || try_operation(std::plus<long long>());//* first, + second.
}

int main() {
    std::ifstream file{"input.txt"};
    std::string line{};
    long long res{0};

    while (std::getline(file, line)) {
        std::istringstream str{line};
        long long total{};
        long long num{};
        std::vector<long long> nums;
        
        str >> total;
        str.ignore();
        while (str >> num) {
            nums.push_back(num);
        }

        if (search(nums, total)) {
            res += total;
        }
    }
    
    std::cout << res << std::endl;
    return 0;
}
