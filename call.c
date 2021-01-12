#include<stdio.h>
//void sum(int *i, int *j);
void sum(int *i,int *j){
    int temp =0;
    *i=temp;
    *j=*i;
}

int main(){

    int a,b;
    printf("Eter value");
    scanf("%d %d",&a,&b);
    printf("\na=>%d b=>%d",a,b);
    sum(&a,&b);
    printf("\na=>%d b=>%d",a,b);

    return 0;
}