def main():
    '''
    Task 1
    Create a max level pakuri and check if each caught pakuri is 
    of a higher level
    '''

    '''
    Task 2
    Create a set to store all seen pakuri
    '''
    max_level = 0
    winner = None
    pakudex = set()

    with open("contest.txt", "r") as file, open("winner.txt", "w") as win, open("pakuri.txt", "w") as paku:
        for line in file:
            trainer_name = line.split(",")[0]
            trainer_catches = line.split(",")[1:]

            for pakuri in trainer_catches:
                pakuri_name = pakuri.split("-")[0]
                pakuri_level = int(pakuri.split("-")[1])

                if pakuri_name not in pakudex:
                    pakudex.add(pakuri_name)
                
                if pakuri_level > max_level:
                    max_level = pakuri_level
                    winner = trainer_name
            

        win.write(f"{winner}")

        for pakuri in sorted(pakudex):
            paku.write(f"{pakuri}\n")

main()