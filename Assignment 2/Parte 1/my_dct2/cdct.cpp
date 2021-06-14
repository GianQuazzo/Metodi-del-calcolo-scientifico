#include "cdct.h"

vector<float> calculate_dct2(const vector<int> X, int n, int m) {
    vector<float> C;

    float alfa_k, alfa_q;

    for(int k = 0; k < n; k++) {
        for(int q = 0; q < m; q++) {
            if(k==0)  alfa_k = sqrt(n);
            else alfa_k = sqrt(n) / sqrt(2);

            if(q==0)  alfa_q = sqrt(m);
            else alfa_q = sqrt(m) / sqrt(2);

            float sum = 0, dct1 = 0;
            for(int i=0; i<n; i++) 
                for(int j=0; j<m; j++) {
                    dct1 = X[i*m+j] * cos(k * M_PI * (2*(i+1) - 1) / (2*n)) * cos(q * M_PI * (2*(j+1) - 1) / (2*m));
                    sum += dct1;
                }
            C.push_back(1 / (alfa_k * alfa_q) * sum);
        }
    }
    return C;
}