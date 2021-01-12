#include<stdio.h>
#include<math.h>

int binary_search(int low,int high, int arr[],int search);

int main(){

    int low = 0;
    int high = 9;
    int arr[10] = {0,1,2,3,4,5,6,7,8,9};
    int search = 0;
    printf("%d",binary_search(low,high,arr,search));

    return 0;
}

int binary_search(int low, int high, int arr[],int search){

    int mid = 0;
    //repeat until low<=high

    while (low<=high)
    {
        //compute mid value
        mid = (high + low) / 2;
        //check if middle index is search value
        if (search == arr[mid]){
            return mid;
        }

        //check for other condition
        if (search > arr[mid]){
            low = mid+1;
        }
        if(search < arr[mid]){
            high = mid -1;
        }
        
    }
    
    //if value is not found in array return -1
    return -1;
}