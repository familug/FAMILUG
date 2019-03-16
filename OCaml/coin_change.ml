open Printf

let rec min_list xs = match xs with
| [] -> 0
| [x] -> x
| [x; y] -> if x < y then x else y
| x :: y -> if x < min_list y then x else min_list y


let rec min_change n denomiations =
    let ans = 1000 in
    if n <= 0 then 0
    else
        min_list
        (List.map (fun i -> if n - i >= 0 then
            min ans (1 + min_change (n-i) denomiations)
    else
        ans
            ) denomiations
        )

let () =
    printf "%d" (min_change 10 [1;3;4])
