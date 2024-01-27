#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("vals.txt", "w");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    float x[51], y1[51], y2[51];
    int i;

    for (i = 0; i < 51; i++) {
        x[i] = i - 25;

        if (x[i] < 0) {
            y1[i] = 0;
            y2[i] = 0;
            continue;
        }

        y1[i] = 7 + 6 * x[i];
        y2[i] = 18 - 2.5 * x[i];
    }

    for (i = 0; i < 51; i++) {
        fprintf(file, "%f ", y1[i]);
    }

    fprintf(file, "\n");

    for (i = 0; i < 51; i++) {
        fprintf(file, "%f ", y2[i]);
    }

    fclose(file);

    return 0;
}
