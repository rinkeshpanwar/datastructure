#include<stdio.h>
int position(int a[],int key,int size);


int n =1000;
int main(){
    int a[n],size,i;
    printf("\nEnter number of element you want to enter in array");
    scanf("%d",&size);
    printf("enter elements now\n");
    for (i=0;i<size;i++){
        scanf("%d",&a[i]);
    }
    int key;
    printf("\nwhich no you want to search?");
    scanf("%d",&key);
    int c;
    c = position(a,key,size);
    printf("found value at position %d",c);
}

int position(int ar[] , int key,int size){

    int i;
    for (i =0;i<size;i++){
        if (ar[i] == key){
            return i+1;
        }
    }
    return 0;
}