import numpy as np
import pandas as pd
import os

# Standardize the ROI Pixel values by dividing by the slice muscle mean.
# Concat all slice standardized pixel values for each aniamal into one csv file.

dicom_folder_path='Y:\DICOM_Files'
save_file_path='Y:\Path\{i}_concat.csv'

def create_and_populate_ROI_Group_column(df):
    # Create empty 'ROI_Group' column:
    df['ROI_Group']=0
    
    ROI_Group = ['liver', 'muscle']
    
    index=0
    # Manually set value for first item, since code compares i to i-1
    df.loc[0, 'ROI_Group']=ROI_Group[index]
    # continue populating ROI_Group column with correct ROI_Group variables
    for i in range(1, len(df.Slice)):
        if  df.Slice[i] > df.Slice[i-1]:
            df.loc[i, 'ROI_Group']=ROI_Group[index]
        else:
            index+=1
            df.loc[i, 'ROI_Group']=ROI_Group[index]
        # print statement for debugging:
        #print(df.Slice[i], df.Slice[i-1], index)  



def standardize_and_concat_slices(df):
    # input: df_results (dataframe with 'muscle' and 'liver' slices labeled)
    # output: 
    global standardized_slice
    standardized_slice=pd.DataFrame()

    for i in df_results.query('ROI_Group=="muscle"').Slice:
        for j in os.listdir(path):
            muscle_mean=int(df.query(f'Slice=={i} and ROI_Group=="muscle"').Mean)
            if 'slice'+str(i)+'.csv' in j: 
                df_test = pd.read_csv(path+os.sep+j)
                df_test=df_test.Value/muscle_mean
                standardized_slice=pd.concat([standardized_slice, df_test], ignore_index=True)
        del muscle_mean


def standardize_and_concat(folder_name):
    os.chdir(f'dicom_folder_path\{folder_name}')
    for i in os.listdir():
        print(i)
        animal_dir = os.getcwd()+os.sep+i
        global df_results
        df_results = pd.read_csv(animal_dir+os.sep+'Results.csv', header=0)
        global path
        path = animal_dir+os.sep+'Slice_ROI_pixel_intensity_values'
        
        create_and_populate_ROI_Group_column(df_results)
        standardize_and_concat_slices(df_results)
    
        # save file
        standardized_slice.to_csv(save_file_path, header=None)    
    
        #print(len(standardized_slice))
        #print(standardized_slice.head())
        
        del path
        del df_results


        
  
standardize_and_concat(folder_where_DICOM_files_are)      
   
