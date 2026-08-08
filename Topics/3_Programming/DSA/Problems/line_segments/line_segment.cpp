#include <cmath>

const double PI = 3.14159265358979323846;

double get_angle(double x, double y) {
    double angle = std::atan2(x,y);
    return angle * (180.0 / PI);
}

