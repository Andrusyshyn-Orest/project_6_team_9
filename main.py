"""
Main module of a project. Runs a program.
"""

import closures
import transitive
import read_and_write
import equivalence_classes



def main():
    '''
    This function runs a program.
    '''
    while True:
        print('Choose what to do:\n' +
            '1 - Find reflexive closure\n' +
            '2 - Find symmetric closure\n' +
            '3 - Find transitive closure\n' +
            '4 - Check if relation is transitive\n' +
            '5 - Get equivalence classes\n' +
            '6 - Count transitive relations\n' +
            '7 - End program')
        action = int(input())
        if action == 7:
            break
        elif action == 6:
            n = int(input('Enter n: '))
            print(transitive.find_number_of_transitives(n))
        else:
            path = input('Enter path to file: ')
            relation, n = read_and_write.read_file(path)
            if action == 5:
                print(equivalence_classes.find_classes(relation, n))
                input('Press enter to continue')
                continue
            elif action == 4:
                print(transitive.check_if_transitive(relation))
                input('Press enter to continue')
                continue
            print('Do you want to write results in file?\n' +
                '1 - Yes\n' + '2 - No')
            save = int(input())
            if save == 1:
                save_path = input('Enter path where to save: ')
            else:
                save_path = ''
            if action == 1:
                print(closures.reflexive_closure(relation, n, save_path))
                input('Press enter to continue')
                continue
            elif action == 2:
                print(closures.symmetric_closure(relation, n, save_path))
                input('Press enter to continue')
                continue
            elif action == 3:
                result = closures.find_transitive_closure(relation, n)
            if save == 1:
                read_and_write.write_file(result, n, save_path)
            print(result)
        input('Press enter to continue')


if __name__ == "__main__":
    main()
