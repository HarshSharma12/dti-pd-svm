dirName="placeholder"
fileName="~/Data/MM803-2018/Project/pd_combine_list.txt"
while read -r line
do
    part1=`dirname "$line"`
    part2=`basename "$line"`
    if [ "$part1" != "$dirName" ]
    then
        "~/Data/MM803-2018/Project/mricrogl_linux/mricrogl_lx/dcm2niix" -b y -z y -f "%b" -o "~/Data/MM803-2018/Project/combined_PD" $part1
        dirName=`dirname "$line"`
    fi
done < "$fileName"
