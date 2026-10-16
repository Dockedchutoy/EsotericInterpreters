proc bbtos*(p: string) =
    for chr in p:
        if chr == 'R':
            echo "BRING BACK THE OLD SANDBOX"

if isMainModule:
    while true:
        bbtos(stdin.readLine())