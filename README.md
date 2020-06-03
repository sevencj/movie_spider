# movie_spider
80s电影网站爬虫及简单的电影列表页面制作

![Image](https://raw.githubusercontent.com/sevencj/movie_spider/master/movie_display1.png)
![Image](https://raw.githubusercontent.com/sevencj/movie_spider/master/movie_display2.png)



总体流程：
        
        一、爬取80s电影信息 （电影名，封面，简介，下载链接）

        二、应用Django开发电影列表页

===============================================================================

一、爬取80s电影信息 （电影名，封面，简介，下载链接）

1. pycharm 创建项目目录 movie_80s

2. 配置venv 安装scrapy框架

3. 创建项目 scrapy startproject movie_80s

4. cd 项目所在路径 创建爬虫 scrapy genspider spider_movie www.80s.tw/movie/list

5. 编写 items.py 设置字段

6. 编写 yf_spider 爬虫

7. 编写 pipeline 保存字段（异步写入数据库）

8. 设置setting 提高爬虫速度

===============================================================================

二、应用Django开发电影列表页

1. pycharm创建Django项目 movie_display

2. 创建app应用 python manage.py startapp movie

3. 配置根路由，子路由，views.py 返回电影列表html

4. 编写views.py 创建index2_view 返回电影列表 movie.html (使用Django分页）

5. 数据库逆向模型类   python manage.py inspectdb>movie/models.py

6. objec.all() 获取数据库数据 传入html 通过django的Paginator进行分页
