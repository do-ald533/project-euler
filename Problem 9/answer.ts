function is_triplet(a:number, b:number, c:number):boolean {
    if(a**2 + b**2 == c**2 && a < b){
        return true;
    }else{
        return false;
    }
}

var sum_total:number = 1000

for (let a = 1; a < sum_total; a++) {
    for (let b = 1; b < sum_total; b++) {
        for (let c = 1; c < sum_total; c++) {
            if (a + b + c == sum_total){
                if(is_triplet(a, b, c) == true){
                    console.log(a * b * c);
                }
            }
        }
    }
}