let sum m =
    let result = ref 0 in
    for i=1 to m do
        result := !result + i
    done;
    !result;;

let main () =
    print_int (sum 100000000);
    print_newline ();
    exit 0;;

main ();;
