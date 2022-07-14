# unittest UI自动化测试

## 📋 功能概述

* PO模式编写
* 对webdriver常用方法二次封装, 并增加日志记录
* 测试完成后, 自动发送邮件
* 支持chrome, Edge, Firefox, IE浏览器
* 数据库 mysql 线程池
* 使用 excel, yaml 收纳定位元素
* 封装 unittest 运行
* beautifulreport / HtmlTestrunner 测试报告

## 🌴 项目结构介绍

```
automated_ui
    |
    ├─ po
    │   │
    │   ├─ common
    │   │    | base_page        封装常用的元素定位方法
    │   │    │ do_excel.py      excel文件读取
    │   |    | do_yaml.py       yaml文件读写
    │   │    │ driver.py        封装实例化所有浏览器驱动
    │   │    │ log.py           生成记录日志
    │   │    │ send_mail.py     发送邮件
    │   │    │ myunit.py        封装单元测试依赖
    │   │    │ test_report.py   封装测试报告方法
    │   │
    │   ├─ core
    │   │    ├─ config.yaml     配置文件
    |   |    ├─ get_conf.py     读取配置
    │   │    └─ path_conf.py    相关路径配置
    │   │
    │   ├─ data                 
    │   │   └─test_data         
    │   |        ├─ *.yaml      存放测试元素数据
    │   │        └─ *.xlsx      存放测试元素数据
    │   │ 
    │   ├─ packages              
    │   |    | TestRunner       测试报告(HTML)
    │   | 
    │   ├─ report               
    │   │    ├─ image           截图存放目录
    │   |    |    ├─ fail       失败截图
    │   |    |    └─ pass       成功截图
    │   │    ├─ log             日志
    │   │    └─ test_report     测试报告
    │   │
    │   ├─ testcase             
    │   │    └─ *               测试项目目录
    │   │       ├─ *_page       测试用例类涉及的元素或通用操作封装
    │   |       └─ test_*.py    测试用例
    │   |
    │   ├─ utils                 
    │   |    └─ send_email.py   邮件发送
    │   |
    │   ├─ run_all.py           运行全部用例
    │   ├─ run_class.py         运行单个类文件所有用例
    │   ├─ run_function.py      运行单个方法用例
    |
    └─ requirements.txt         依赖包
```

## 👨‍💻 环境准备

~~手动安装浏览器驱动~~

🆕 已支持浏览器驱动自动安装

## 🚀 运行

### 安装依赖

```shell
pip install -r requirements.txt
```

### 命令行运行:

1. 进入 po 目录下
    ```shell
    cd po
    ```
2. 命令行运行规则: python 运行文件 测试用例目录名

    ```shell
    # 执行全部用例类的全部用例函数
    python run_all.py baidu
    ```

    ```shell
    # 执行指定用例类
    python run_class.py baidu
    ```

    ```shell
    # 执行指定类中的指定函数
    python run_function.py baidu
    ```

### pycahrm运行:

1. 指定测试运行程序为: Unittest

   ![](md_files/img.png)


2. 运行文件鼠标右键,选择修改运行配置

   ![](md_files/img_1.png)


3. 配置参数: 测试用例目录名

   ![](md_files/img_2.png)

## 🖼️ 效果图

**pycharm控制台:**

![](md_files/img_4.png)

**日志效果:**

![](md_files/img_5.png)

**HTML 测试报告（自定义）**

![](md_files/img_6.png)

**自动截取错误截图**

![](md_files/img_7.png)

**BeautifulReport 测试报告（原生第三方）**

![](md_files/img_3.png)
