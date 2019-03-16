open Printf

exception Invalid_input

let min_list xs = match xs with
| [] -> raise Invalid_input
| hd::tl -> List.fold_left min hd tl

let rec min_change money denomiations =
    let ans = max_int in
    if money <= 0 then 0
    else
        min_list
        (List.map (fun coin ->
            if money >= coin then
                min ans (1 + min_change (money-coin) denomiations) else
                    ans) denomiations
        )

let () =
    printf "%d" (min_change 10 [1;3;4])
