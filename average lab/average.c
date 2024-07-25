#include <stdio.h>
int main(){
    int len;
    printf("Enter number of elements in array: ");
    scanf("%d", &len);
    int arr[len];
    printf("Enter elements of array: ");
    int sum = 0;
    for(int i = 0;i<len;i++){
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    float avg = (float)sum/len;
    printf("%f", avg);
    return 0;
}
