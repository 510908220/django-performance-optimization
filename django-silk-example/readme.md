# **django-silk**使用整理

silk可以实时记录django里http、数据库的访问,帮助分析和改进django程序性能.



## 安装

基本的安装可以看说明: https://github.com/jazzband/django-silk

## 配置

#### 元数据

`SILKY_META = True`可以看到`silk`保存数据库耗时, 这样在页面上就能看到总耗时以及silk本身耗费的时间.

#### request/response 内容大小



#### 限制request/response数据

为了避免silk_requests和silk_response表数据持续增长,可以通过下面两个配置项控制记录的数量:

```python
SILKY_MAX_RECORDED_REQUESTS = 1000
SILKY_MAX_RECORDED_REQUESTS_CHECK_PERCENT = 10
```

清除逻辑当满足下面条件时才会触发 ：

```python
check_percent = SilkyConfig().SILKY_MAX_RECORDED_REQUESTS_CHECK_PERCENT
check_percent /= 100.0
if check_percent < random.random() and not force:
	return
```

所以如果想让记录是一旦达到`SILKY_MAX_RECORDED_REQUESTS`就清除的话可以设置`SILKY_MAX_RECORDED_REQUESTS_CHECK_PERCENT=100`



## 实践 

这里以一个例子,

## 