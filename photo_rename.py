# -*- coding:utf8 -*-
 
import os
class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    '''
    def __init__(self):
        self.path = 'E:\Pictures\Saved Pictures\美图'     #存放图片的文件夹路径
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            if item.endswith('.jpg'):  #指定选取的图片格式为jpg
 
                src = os.path.join(os.path.abspath(self.path), item)
                # 2018-11-20_bqb00  2018-11-20_hzw00
                dst = os.path.join(os.path.abspath(self.path), '2018-11-20_hzw' + str(i) + '.png')      #设置新的图片名称
                try:
                    os.rename(src, dst)
                    print ("转换图片 %s 成为 %s ..." % (src, dst))
                    i = i + 1	    
                except:
                    continue
 
        print ("共 %d 张图片重命名和转换成 %d jpgs" % (total_num, i-1))
if __name__ == '__main__':
    demo = BatchRename()
 
    demo.rename()
