import os

def get_dir_output_folder_information():
    '''输入目录统计目标目录，
    回车默认脚本所在目录'''
    global file_name,folder_name,input_dir
    input_dir = input('Please input goal folder:')
    if input_dir.strip() == '' :
        input_dir = os.path.abspath('.')
    file_name = []
    folder_name = []
    file_dir = []
    for root,dirs,files in os.walk(input_dir, topdown = False):
        for i in files:
            file_name.append(i)
        for j in dirs:
            folder_name.append(j)
        for k in files:
            file_dir.append(os.path.join(root,k))
    sum = 0
    volume = []
    for i in file_dir:
        volume.append(os.path.getsize(i))
        sum = sum + os.path.getsize(i)

    for i, j in enumerate(volume):
        # print(i,j)
        if j == max(volume):
            max_index = i
        elif j == min(volume):
            min_index = i
    print(max_index,min_index)


    print(f'该文件夹共有{len(file_name)}个文件{len(folder_name)}个文件夹！')
    print(f'该文件夹共计{sum}字节！')
    print(f'该文件夹最大的文件{volume[max_index]/1024/1024}Mb,路径为：{file_dir[max_index]},\
        该文件夹最小的文件{volume[min_index]/1024/1024}Mb，路径为{file_dir[min_index]}')








get_dir_output_folder_information()




