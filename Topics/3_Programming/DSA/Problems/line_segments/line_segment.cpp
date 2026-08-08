#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>
#include <vector>

namespace {
constexpr double kPi = 3.14159265358979323846;
using Point = std::array<double, 2>;
using Segment = std::array<Point, 2>;
using Case = std::vector<Segment>;

double get_angle(double x, double y) {
    const double angle = std::atan2(x, y);
    return angle * 180.0 / kPi;
}

bool can_draw_line(const Case& line_segments) {
    std::vector<std::array<double, 2>> angles;
    angles.reserve(line_segments.size() * 2);

    for (const auto& line : line_segments) {
        double start = get_angle(line[0][0], line[0][1]);
        double end = get_angle(line[1][0], line[1][1]);
        if (std::fmod((end - start) + 360.0, 360.0) > 180.0) {
            std::swap(start, end);
        }

        start = std::fmod(start, 180.0);
        end = std::fmod(end, 180.0);
        if (start < 0.0) {
            start += 180.0;
        }
        if (end < 0.0) {
            end += 180.0;
        }
        angles.push_back({start, end});
    }

    for (std::size_t i = 0; i < angles.size(); ++i) {
        const auto angle = angles[i];
        if (angle[0] > angle[1]) {
            angles[i] = {angle[0], 180.0};
            angles.push_back({0.0, angle[1]});
        }
    }

    std::sort(angles.begin(), angles.end());

    if (angles.front()[0] > 0.0 || angles.back()[1] < 180.0) {
        return true;
    }

    double mx = angles.front()[1];
    for (std::size_t i = 0; i + 1 < angles.size(); ++i) {
        if (angles[i][1] < angles[i + 1][0] && angles[i + 1][0] > mx) {
            return true;
        }
        mx = std::max(mx, angles[i][1]);
    }
    return false;
}
}  // namespace

int main() {
    const std::vector<Case> cases = {
        {
            Segment{{Point{{2, 5}}, Point{{5, 2}}}},
            Segment{{Point{{4, 4}}, Point{{6, 1}}}},
            Segment{{Point{{8, 1}}, Point{{8, -3}}}},
            Segment{{Point{{-3, 5}}, Point{{3, 5}}}},
            Segment{{Point{{-5, 1}}, Point{{6, -6}}}},
        },
        {
            Segment{{Point{{1, 8}}, Point{{9, -4}}}},
            Segment{{Point{{-8, -1}}, Point{{9, -3}}}},
        },
        {
            Segment{{Point{{2, -1}}, Point{{2, 1}}}},
            Segment{{Point{{-1, -1}}, Point{{-1, 1}}}},
        },
        {
            Segment{{Point{{2, 0}}, Point{{0, 2}}}},
        },
        {
            Segment{{Point{{2, 1}}, Point{{2, -1}}}},
            Segment{{Point{{-1, -1}}, Point{{-1, 1}}}},
        },
        {
            Segment{{Point{{0, 1}}, Point{{0.985, -0.174}}}},
            Segment{{Point{{-1, 0}}, Point{{0, 1}}}},
            Segment{{Point{{0.996, -0.087}}, Point{{0.866, -0.5}}}},
        },
    };

    for (const auto& line_case : cases) {
        std::cout << (can_draw_line(line_case) ? "True" : "False") << '\n';
    }
    return 0;
}
