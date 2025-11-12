#include <cstdint>
#include <vector>
#include <random>
#include <iostream>
#include <cmath>
#include <fstream>
#include <complex>
#include "head.h"

using namespace std;


void print_vector_bits(vector<int16_t> bits){
    ofstream file("generated_bits.txt");
    for(int16_t bit : bits){
        cout << static_cast<int>(bit) << " ";
        file << static_cast<int>(bit) << " ";
    }
    cout << endl;
    file << endl;
    file.close();
    return;
}

void print_vector_symbols(vector<int16_t> symbols){
    ofstream file("symbols.txt");
    for(int16_t symbol : symbols){
        cout << "sample: " << symbol << "\n";
        file << symbol << " ";
    }
    cout << endl;
    file << endl;
    file.close();
    return;
}

void print_vector_signal(vector<double> signal){
    ofstream file("signal.txt");
    for(double sign : signal){
        cout << sign << " ";
        file << sign << " ";
    }
    cout << endl;
    file << endl;
    file.close();
    return;
}


vector<int16_t> generate_bits(int size){
    vector <int16_t> bits;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, 1);
    for(int i = 0; i < size; i++){
        bits.push_back(dis(gen));
    }
    return bits;
}

vector<vector<int16_t>> coder(vector<int16_t> generated_bits){
    vector<vector<int16_t>> symbols;
    for(int i = 1; i < generated_bits.size(); i+=2){
        vector<int16_t> symbol = {generated_bits[i-1], generated_bits[i]};
        symbols.push_back(symbol);
    }

    return symbols;
}

vector<int16_t> qpsk_modulation(vector<vector<int16_t>>& bits){
    vector<int16_t> sample;
    for(vector<int16_t> bit : bits){
        sample.push_back(bit[0] * 2.0 - 1.0);
        sample.push_back(bit[1] * 2.0 - 1.0);
    }
    return sample;
}



vector<int16_t> filter(vector<int16_t> qpsk_symbols, int L, int size){
    int size_arr = L * size;
    vector<int16_t> g(L, 1);
    vector<int16_t> x(size_arr, 0);
    vector<int16_t> result(size_arr, 0);

    for(int i = 0; i < size_arr; i += L){
        int idx = i / L;
        x[i] = qpsk_symbols[idx];
    }
    
    for(int i = 0; i < size_arr; i++){
        int16_t tmp = 0;
        for(int m = 0; m < L; m++){
            if(i - m >= 0){                                 
                tmp += x[i - m] * g[m];
            }
        }
        result[i] = tmp;
    }
    return result;
}

vector<int16_t> my_ready_samples(){
    int size = 12;
    int sample_rate = 32;

    vector<int16_t> generated_bits = generate_bits(size);
    vector<vector<int16_t>> symbols = coder(generated_bits);
    vector<int16_t> qpsk_symbols = qpsk_modulation(symbols);

    vector<int16_t> timed = filter(qpsk_symbols, 10, size);
    vector<int16_t> ready_samples;
    for(int i = 10; i < timed.size(); i+=20){
        for(int j = 0; j < 10; j++){
            ready_samples.push_back(timed[i + j - 10]);
            ready_samples.push_back(timed[i + j]);
        }
    }
    return ready_samples;
}