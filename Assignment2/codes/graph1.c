#include <stdio.h>
#include<math.h>
int main() {
    FILE *file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    float first_term = 729;

    float common_ratio = 2.0 / 3.0 ;     

    int n ; // sum of n terms of series
    float s;
    
    for(n=1;n<22;n++)
    {
        s = first_term * ((pow(common_ratio,n)-1)/(common_ratio - 1));
        fprintf(file ,"%d \t %e \n",n-1 , s);
    }
    fclose(file);
    return 0;
}
