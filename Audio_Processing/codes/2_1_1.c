#include <stdio.h>

int main() {
    int i;
    double x[6] = {1.0, 2.0, 3.0, 4.0, 2.0, 1.0};
    
    FILE *fp = fopen("2_1_1.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    for (i = 0; i < 6; i++) {
        fprintf(fp, "%d,%lf\n", i, x[i]);
    }
    
    fclose(fp);
    
    return 0;
}
