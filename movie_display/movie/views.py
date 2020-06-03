from django.shortcuts import render
from movie.models import *
import math
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def movie_view(request):

    # 接收当前页码
    num = request.GET.get('num', 1)
    # 查询所有的数据
    movies, n = page(num)

    # 上一页的页码
    pre_page_num = n - 1
    # 下一页的页码
    next_page_num = n + 1

    return render(request, 'movie.html', {'movies': movies, 'pre_page_num': pre_page_num, 'next_page_num': next_page_num})


# 原生分页
def page(num, size=24):
    # 接收当前页页码
    num = int(num)
    # 总记录数
    totalRecords = Movie.objects.count()
    # 总页数
    totalPages = math.ceil(totalRecords*1.0/size)

    # 判断是否越界
    if num < 1:
        num = 1

    elif num > totalPages:
        num = totalPages

    # 计算每页显示的记录
    moives = Movie.objects.all()[((num-1)*size):(num*size)]

    return moives, num


# Django分页
def index2_view(request):
    # 获取当前页码
    num = int(request.GET.get('num', 1))
    # 查询所有数据
    movies = Movie.objects.all()
    # 创建分页器对象
    pager = Paginator(movies, 24)

    # 获取当前页的数据
    try:
        per_page_data = pager.page(num)

    # 当前页码不是int 返回第一页数据
    except PageNotAnInteger:
        per_page_data = pager.page(1)

    # 当前页码大于总页码 返回最后一个数据
    except EmptyPage:
        per_page_data = pager.page(pager.num_pages)

    if num < 7:
        begin = 1
        end = begin + 9
    elif num >= 7 and num < pager.num_pages - 3:
        begin = num - 5
        end = num + 4

    elif num >=pager.num_pages - 3 and num <= pager.num_pages:
        end = pager.num_pages
        begin = end - 9

    elif num > pager.num_pages:
        end = pager.num_pages
        begin = end - 9

    page_range = range(begin, end+1)

    return render(request, 'movie.html', {'per_page_data': per_page_data, 'pager': pager,
                                          'page_range': page_range, 'current_page': num})