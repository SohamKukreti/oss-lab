#include <stdio.h>

int main(){
    int len;
    printf("enter number of characters in string: ");
    scanf("%d", &len);
    char str[len];
    for(int i = 0;i<len;i++){
        scanf(" %c", &str[i]);
    }
    str[len] = '\0';
    int start = 0;
    int end = len - 1;
    while(start <= end){
        char temp = str[start];
        str[start] = str[end];
        str[end] = temp;
        start++;
        end--;
    }
    for(int i = 0;i<len;i++){
        printf("%c", str[i]);
    }
    printf("\n");
    return 0;
}