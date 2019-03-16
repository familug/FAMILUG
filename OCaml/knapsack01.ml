open Printf
(*
   f(idx) -> value
   if cond(idx) then take it
   else not take it

   take or not would need consider weight_left

   f(idx, weight_left) = max( f(idx + 1, weight_left), vals[idx] + f(idx+1, weight_left-weigths[idx]))
   value - weight
Input:
4 5
1 8
2 4
3 0
2 5
2 3


Output:
13

   *)

let solve bag =
  let weights = [1;2;3;2;2]
  and values = [8;4;0;5;3] in
  let rec max_value weight_left weights values = match weights with
    | [] -> 0
    | w::wtl ->
      let _ = printf "%d\n" weight_left in
      let valuetl = List.tl values in
      if w > weight_left then
        max_value weight_left wtl valuetl
      else
        max (max_value weight_left wtl valuetl) (
          List.hd values +  max_value (weight_left-w) wtl valuetl
        )

  in
  max_value bag weights values

let () =
  printf "%d" (solve 4)
