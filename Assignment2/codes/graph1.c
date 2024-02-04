#include <stdio.h>
#include<math.h>
float y(int n); //recursive function to calculate the sum of GP : y(n) = sum of first (n+1) terms of the GP 

float first_term = 729;    //first term of the GP

float common_ratio = 2.0 / 3.0 ;  //common ratio of thr GP

int main() {
    FILE *file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int n ; // term number 
    float x ; // stores the term x(n) of the GP in the loop 
    
    for(n=0;n<=21;n++)
    {
        x = first_term*(pow(common_ratio,n));
        fprintf(file ,"%d \t %e \t %e\n",n , x , y(n));
    }
    fclose(file);
    return 0;
}
float y(int n)
{
    if(n==0)
        return first_term;
    else
        return y(n-1) + (float)pow(common_ratio,n)*(first_term);  //sum of n terms  = sum of n-1 terms + nth term
}
