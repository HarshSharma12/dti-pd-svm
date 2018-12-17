for file in `ls combined_Control/*.nii.gz`
do
	echo "Correcting for $file"
	outName="${file%.nii.gz}_corrected.nii.gz"
	eddy_correct "$file" "$outName" 1
done
