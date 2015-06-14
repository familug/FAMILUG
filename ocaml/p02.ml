(* L99.02 *)
let rec last_two = function
    | []|[_] -> None
    | [x; y] -> [x; y]
    | _ :: t -> last_two t;;
