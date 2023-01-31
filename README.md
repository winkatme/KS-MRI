# KS-MRI
Kolmogorov-Smirnov matrix on MRI data

This code standardizes MRI ROI image slice intensity values on the mean intensity of a specified region, concatenates the files so that all standardized files of the same patient are in one single file, then calculates a Kolmogorov-Smirnov matrix on the standardized, concatenated files.

For example, say you want to average the the entire pixel intensity across multiple slices for a patient's liver.  Since the intensity can vary per slice, you also want to standardize each slice by dividing each liver pixel intensity value by the mean intensity of a region of muscle from the same slice, for each slice. Then concatenate all the standardized values together.

## Preprocessing
1. Place each DICOM file in its own folder.
2. Load the DICOM files into imagej
3. Outline ROIs for the necessary regions first (ie - liver), making sure that each slice with an ROI shows up in the ROI Manager.
4. Then outline ROIs for the neccesary reference region to standardize on (ie - muscle)
5. Make sure that all slices that have the desired region also have the region to standardize on.  For example, if you outline slices 1-6 for the liver, make sure that only slices 1-6 also have outlines for the muscle, if you want to standardize on the mean muscle pixel intensity. There should be 12 slices total in the ROI Manager. 
6. Save the ROI Manager ROIs as an RoiSet.zip file in the same folder as the DICOM file (this step is recommended but not necessary).
7. Select all ROIs in ROI manager and click 'Measure' to view results.  Results window will pop up.  Make sure that Area, Mean, and Slice columns are all visible.
8. Select all rows in Results window and save file as Results.csv in same folder as the DICOM file.
9. Create a new folder called 'Slice_ROI_pixel_intensity_values' inside the same folder as each DICOM file.
10. Select each primary ROI region slice in the ROI Manager and click Analyze->Tools->Save XY Coordinates from the main ImageJ window.
11. Append 'slice_#' to each coordinate file and save each coordinate file in the Slice_ROI_pixel_intensity_values folder.  ie - for slice 5, one would save it as Patient_Dicom_slice5.csv.  Do this only for the primary region ROIs, not the region to standardize on.


Once the data has been preprocessed in this manner, a Kolmogorov-Smirnov matrix can be calculated by pointing the code to the correct folder.




