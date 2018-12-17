for file in `ls combined_PD/*_corrected.nii.gz`
do
	echo "Calculating data for $file"
	brainFile="${file%.nii.gz}_brain_mask.nii.gz"
	outName="${file%_corrected.nii.gz}" 
	bvalFile="${file%_corrected.nii.gz}.bval"
	bvecFile="${file%_corrected.nii.gz}.bvec"
	dtifit -V -k $file -o $outName -m $brainFile -r $bvecFile -b $bvalFile
done
