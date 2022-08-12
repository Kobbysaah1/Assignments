#include<iostream>
#include<cmath>
int main(){
    float arr[10];
    float sum;
    float mean;
    float sum2;
    float input;
    
    for (int i=0;i<10;i++){
        sum+=arr[i];
    }
    mean = sum/10
    for (int i =0;i<10;i++){
        sum2+=(arr[i]-mean)*(arr[i]-mean)
    }
    cout<<sqrt(sum2/10)

}