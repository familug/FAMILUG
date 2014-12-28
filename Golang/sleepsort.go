// by Viet Hung Nguyen <hvn@familug.org>
// at Sun Dec 28 10:55:19 SGT 2014
package main
import (
    "flag"
    "fmt"
    "os"
    "strconv"
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
    flag.Parse()
    numbs := make([]int, len(flag.Args()))
    var err error
    for i, v := range flag.Args() {
        numbs[i], err = strconv.Atoi(v)
        if err != nil {
            fmt.Println("Bad argument %v", err)
            os.Exit(2)
        }
    }
    fmt.Println("Numbers to sort: ", numbs)
    SleepSort(numbs)
    fmt.Println("Done magically sleepsort algorithm")
}
