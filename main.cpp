#include <iostream>
#include <vector>

// Este codigo lo aprendi en la clase pasada de Estructuras de Datos y Algoritmos, el profe menciono en clase que podiamos utilizar ese codigo si lo habiamos implementado antes en esa clase.
void merge(std::vector<double>& leftArray,std::vector<double>& rightArray,std::vector<double>& arr){
    int leftSize=leftArray.size();
    int rightSize=rightArray.size();

    //indices
    int i=0;
    int l=0;
    int r=0;

    //main while
    while(l<leftSize && r<rightSize){
        if(leftArray[l]>rightArray[r]){
            arr[i]=leftArray[l];
            l++;
        }
        else{
            arr[i]=rightArray[r];
            r++;
        }
        i++;
    }

    //leftovers whiles
    while(l<leftSize){
        arr[i]=leftArray[l];
        i++;
        l++;
    }
    while(r<rightSize){
        arr[i]=rightArray[r];
        i++;
        r++;
    }
}

void mergeSort(std::vector<double>& arr){
    int n=arr.size();
    if(n<=1) return;
    int center=n/2;
    std::vector<double> leftArray(center);
    std::vector<double> rightArray(n-center);
    for(double i=0;i<n;i++){
        if(i<center){
            leftArray[i]=arr[i];
        }
        else{
            rightArray[i-center]=arr[i];
        }
    }

    //divide
    mergeSort(leftArray);
    mergeSort(rightArray);

    //conquer
    merge(leftArray,rightArray,arr);
}

int main(){
    int N;
    std::cin>> N;
    std::vector<double>arr(N);
    for(int i = 0; i < N; i++){
        std::cin>> arr[i];
    }

    mergeSort(arr);
    for(int i = 0; i < arr.size(); i++){
        std::cout<<arr[i];
        if(i <arr.size() - 1){
            std::cout << ",";
        }
    }
    std::cout<< std::endl;
    
    return 0;
}