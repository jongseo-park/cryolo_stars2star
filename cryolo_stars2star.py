import os
import argparse

parser = argparse.ArgumentParser (description="merging crYOLO star files")

parser.add_argument("--star", required=False, default="./STAR/", help="Path to star files")
parser.add_argument("--prefix", required=False, default="", help="Path to mrcs (inputs of crYOLO ptcl picking)")
parser.add_argument("--output", required=False, default="picks.star", help="output file name")

args = parser.parse_args()



if args.prefix == "":
    pfx = args.prefix
else:
    pfx = args.prefix + '/'


check = os.listdir('./')


if args.output in check:
    print (f"Please remove the '{args.output}' from this path")

else:

    path = args.star + '/'
    file_list = os.listdir (path)
    file_list_star = [file for file in file_list if file.endswith('.star')]



    with open (f'{args.output}', 'a') as file:
        file.write('\n')
        file.write('data_\n')
        file.write('\n')
        file.write('loop_\n')
        file.write('_rlnMicrographName #1\n')
        file.write('_rlnCoordinateX #2\n')
        file.write('_rlnCoordinateY #3\n')

        for i in file_list_star:
            n = 0
            f = open (f'{args.star}/{i}')
            j = f.readlines()
            num = len(j) - 7
            # print (num)
            for m in range(num):
                mrc = i.replace('.star','.mrc')
                file.writelines(pfx + mrc + ' ')
                file.writelines(j[n+6:n+7])
                n = n + 1


