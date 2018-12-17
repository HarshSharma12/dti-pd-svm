for file in `ls combined_PD/*_corrected.nii.gz`
do
	echo "Extracting for $file"
	outName="${file%.nii.gz}_brain.nii.gz"
	bet "$file" "$outName" -o -m -R
done
