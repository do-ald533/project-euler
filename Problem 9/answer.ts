function is_triplet(a:number, b:number, c:number):boolean {
    if(a**2 + b**2 == c**2 && a < b){
        return true;
    }else{
        return false;
    }
}

var sum_total:number = 1000

for (let a = 0; a < sum_total; a++) {
    for (let b = 0; b < sum_total; b++) {
        for (let c = 0; c < sum_total; c++) {
            if (a + b + c == sum_total){
                if(is_triplet(a, b, c) == true){
                    console.log(a * b * c);
                }
            }
        }
    }
}