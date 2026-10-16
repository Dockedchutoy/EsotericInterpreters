import std/strutils

#[ 
END END => END END 
END INT => END INT
INT END => END INT
INT INT => INT END
]#

proc obqb*(program: var string): string =
    if program.len == 2 and program.allCharsInSet({'0','1'}):
        var pos: int = 0
        while true:
            if program[pos] == '0':
                return program
            elif program[pos] == '1':
                if pos == 1: pos = 0
                else: pos += 1
                if program[pos] == '0': program[pos] = '1'
                else: program[pos] = '0'
            
    else:
        return "FATAL ERROR: INVALID PROGRAM"

if isMainModule:
    while true:
        var p: string = stdin.readLine()
        echo obqb(p)