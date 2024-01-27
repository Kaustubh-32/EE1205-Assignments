#include <stdio.h>
int main() {
    FILE *file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    int i;
    fprintf(file,"n \t First \t Second\n");
    for(i=0;i<51;i++)
    {
        fprintf(file ,"%d \t %f \t %f",i , 7 + 6*i, 18 - 2.5*i)  ;
    }
    fclose(file);
    return 0;
}
