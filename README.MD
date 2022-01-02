# Flask-CheckStudent (大沥高中查人系统)
> 本 `base` 分支是 Flask 应用的基础框架！！ 
## 说明
1. 本程序基于 `Flask` 框架制作
2. 完善的项目结构.
3. .........
## 部署
1. **简易运行**
    > venv 默认在Python 3.3及更高版本中可用.  
    > virtualenv需要单独安装，但支持Python 2.7+和Python 3.3+，并且 pip， setuptools和 wheel默认情况下始终安装到创建的虚拟环境中（无论Python版本如何）。  
    > 虚拟环境的路径不要含有中文,
    - Linux
    ```shell
    python3 -m venv venv  # 创建虚拟环境
    source ./venv/bin/activate  # 激活它
    pip3 install -r ./requirements.txt  # 安装需求包
    flask deploy  # 初始化
    flask run  # 运行
    ```
   
    - Windows
    ```shell
    python -m venv venv  # 创建虚拟环境
    .\venv\Scripts\activate.bat  # 激活它(cmd中)
    .\venv\Scripts\Activate.ps1  # 激活它(powershell中)
    pip install -r ./requirements.txt  # 安装需求包
    flask deploy  # 初始化
    flask run  # 运行
    ```
