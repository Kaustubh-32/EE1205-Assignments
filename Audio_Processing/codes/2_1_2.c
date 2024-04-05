#include<stdio.h>
double x[6] = {1.0,2.0,3.0,4.0,2.0,1.0};
double y(int n)
{
    if(n<0)
        return 0;
    else if(n ==0)
        return x[0];
    else if (n<6)
        return x[n] + x[n-2] - 0.5*y(n-1);
    else if (n>7)
        return -0.5*y(n-1);
    else 
        return x[n-2]-0.5*y(n-1);
    
}
int main()
{
    FILE *fp = fopen("2_1_2.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    int i;
    
    for (i = 0; i < 15; i++) {
        fprintf(fp, "%d,%lf\n", i, y(i));
    }
    
    
    fclose(fp);
    
    return 0;
}
