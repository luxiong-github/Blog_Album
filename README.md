# Blog_Album
(1) 存放的是相册照片资源，内含`photos`、`min_photos`两个目录以及一个`tool.py`脚本

(2) photos存放的是照片，把想要上传的照片资源按照`2019-02-02_XXX.png`的命名规范放在此处

(3) min_photos存放的是执行`tool.py`后根据`photos`中照片生成的压缩图，自动生成，无需添加任何东西

(4) tool.py是执行脚本，内部包含了四个方法，分别是：  
- `cut_photo()`裁剪图片，裁剪成正方形，去中间部分;
- `compress_photo()`压缩图片，并保存到mini_photos文件夹下;
- `git_operation()`提交到github仓库;
- `handle_photo()`将文件处理成json格式，存到博客仓库中 