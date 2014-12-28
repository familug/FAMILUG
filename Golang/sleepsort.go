// by Viet Hung Nguyen <hvn@familug.org>
// at Sun Dec 28 10:55:19 SGT 2014
package main
import (
    "fmt"
    "sync"
    "time"
)

func f(x int, wg *sync.WaitGroup) {
    time.Sleep(time.Duration(x) * time.Second)
    fmt.Println(x)
    wg.Done()
}


func SleepSort(xs []int) {
    var wg sync.WaitGroup
    wg.Add(len(xs))
    for _, x := range xs {
        go f(x, &wg)
    }
    wg.Wait()
}

func main() {
    numbs := []int{2, 1, 3}
    SleepSort(numbs)
    fmt.Println("Done magically sleepsort algorithm")
}
