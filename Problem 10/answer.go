package main

import "fmt"
 

func sieveOfEratosthenes(n int) []int {
    integers := make([]bool, n+1)
    for i := 2; i < n+1; i++ {
      integers[i] = true
    }
    for p := 2; p*p <= n; p++ {
        if integers[p] == true {
            for i := p * 2; i <= n; i += p {
              integers[i] = false
            }
        }
    }
    var primes []int
    for p := 2; p <= n; p++ {
        if integers[p] == true {
          primes = append(primes, p)
        }
    }
    return primes
}


func main(){
    n := 2000000
    var sum int
    primes := sieveOfEratosthenes(n)
    for _, prime := range primes{
        sum += prime
    }
    fmt.Println(sum)
}