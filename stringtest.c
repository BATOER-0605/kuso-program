#include <stdio.h>

int main(){

    char *charact = "ABCD";

    printf("変換前: %s\n",charact);

    //charact[0] = "B";

    //printf("変換後: %s\n",charact);
    printf("%c\n",charact[0]);

    char charact_array[10] = "EFGH";
    printf("%s¥n",charact_array);
    charact_array[0] = "A";
    printf("%s¥n",charact_array);
}