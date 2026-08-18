#pragma once

#include <utility>
#include <vector>

struct Point {
    double x;
    double y;
};

using Line = std::pair<Point, Point>;
using Case = std::vector<Line>;

std::vector<Case> get_cases();
