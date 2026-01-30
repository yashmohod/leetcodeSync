bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {

    

    for(int i=0; i < flowerbedSize; i++){
        if(i == 0){
            if(flowerbed[i] == 0 && flowerbed[i+1] == 0){
                n--;
            }
        }else if(i == flowerbedSize -1){
            if(flowerbed[i] == 0 && flowerbed[i-1] == 0){
                n--;
            }
        }else{
            int r = flowerbed[i-1] + flowerbed[i] + flowerbed[i+1];
           if(r == 0){
                n--;
           } 
        }
    }

    if(n>0){
        return 0;
    }else{
        return 1;
    }

}
