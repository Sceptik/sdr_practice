#include <cstdint>
#include <vector>
#include <random>
#include <iostream>
#include <cmath>
#include <fstream>
#include <complex>

using namespace std;
vector<int16_t> generate_bits(int size);
vector<vector<int16_t>> coder(vector<int16_t> generated_bits);
vector<int16_t> qpsk_modulation(vector<vector<int16_t>>& bits);
vector<int16_t> filter(vector<int16_t> qpsk_symbols, int L, int size);
vector<int16_t> my_ready_samples();