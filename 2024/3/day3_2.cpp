#include <string>
#include <regex>
#include <iostream>
#include <fstream>
int main() {
    std::ifstream file("input.txt");
    std::string input((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>()); //Reads file into string.
    std::regex reg("mul\\((\\d+),(\\d+)\\)|do\\(\\)|don't\\(\\)"); //double '\' due to c++ literal escaping.
    int n1{}, n2{}, res{};
    bool enabled{true};

    //Basically stolen from regex cppref. :)
    auto begin{std::sregex_iterator(input.begin(), input.end(), reg)};
    auto end{std::sregex_iterator()};
    for (auto i = begin; i != end; ++i) {
        std::smatch match{*i};
        enabled = (match.str() == "do()") ? true : (match.str() == "don't()") ? false : enabled;
        if (enabled && match.str().substr(0, 3) == "mul"){
            n1 = std::stoi(match[1]);
            n2 = std::stoi(match[2]);
            res += n1 * n2;
        }
    }
    std::cout << res << std::endl;

    return 0;
}