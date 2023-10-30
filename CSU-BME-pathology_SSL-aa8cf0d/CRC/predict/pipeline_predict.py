import os
import time

#data path
input_base_path='/media/disk1/pathology_data_process/'
group_dirs=['group20']   #WSI directory

#output dirs of predict and heatmaps data as so on
output_base_path = '/media/disk4/pathology_model-0.1-SSL-0/'
model_path='../Model-0.1-SSL-0.hdf5'    #model name and path
input_real_file='/media/disk2/pathology_data_process/CRC_labels.txt'    #label file of patient level

for group in group_dirs:
    input_group_path=input_base_path+group+'/'
    output_group_path=output_base_path+group+'/'

    if not os.path.exists(input_group_path):
        print('wrong input path')
        continue

    if os.path.exists(output_group_path):
        print('group output path has existed, continue proceed...')

        #if output_base_path != input_base_path:
         #   continue
    else:
        os.mkdir(output_group_path)

    print('Processing ' + group + ' ******************** at ' + time.asctime(time.localtime(time.time())))
    print('Building prediction *************')
    basecommand = 'python3 predict_bigdata_casedirs.py '+input_group_path+' '+output_group_path+' '+model_path
    os.system(basecommand)
    print('\n')

    #handle V3
    print('Begining create heatmap V3*************')
    basecommand='python3 create_heatmap_casedirs_V3.py '+input_group_path+' '+output_group_path
    os.system(basecommand)
    print('\n')

    print('Begining heatmap to images V3')
    basecommand='python3 heatmap-to-image-casedirs_V3.py '+input_group_path+' '+output_group_path   #+' True'  #True only for 5X
    os.system(basecommand)
    print('\n')

    #handle V2
    print('Begining create heatmap *************')
    basecommand='python3 create_heatmap_casedirs.py '+input_group_path+' '+output_group_path
    os.system(basecommand)
    print('\n')

    print('Begining create heatmap *************')
    basecommand = 'python3 create_heatmap_casedirs_3x3.py ' + input_group_path + ' ' + output_group_path
    os.system(basecommand)
    print('\n')

    print('Begining heatmap to images')
    basecommand='python3 heatmap-to-image-casedirs.py '+input_group_path+' '+output_group_path   #+' True'  #True only for 5X
  #  os.system(basecommand)
    print('\n')

