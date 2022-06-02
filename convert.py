#!/usr/bin/python3

print("hi")

with open("Result.json", "w") as r:
    with open('Comments.json') as f:
        for index, line in enumerate(f):
            line = list(line)
            
            # first line, we need to append ']' at the end
            if(line[0] == '['):
                line[-1] = ']'
                line.append('\n')
            
            #all lines in between -> remove the first comma and add everything in between [ .... ]
            elif(line[0] == ',' and line[-2] == '}'):
                line[0] = '['
                line[-1] = ']'
                line.append('\n')

            #the last line only has a ']' -> remove it
            elif(line[0] == ']'):
                continue
            else:
                print("problem detected!!!!")
                print(f"{line=}")
                print(f"{index=}")
                raise Exception("we should never be here")
            r.write("".join(line))

print("finito")