package main

import "fmt"

func isDivisible(num int) bool{
    for i := 2; i < 21; i++ {
        if (num % i != 0) {
            return false
        }
    }
    return true
}


func main(){
    var x int = 2520
    var found bool = false
    for found == false {
        if (isDivisible(x) == true){
            fmt.Printf("%d", x)
            found = true
        } else {
            x++
        }
    }
}

