import concurrent.futures
import queue

from download import download


def task_function(url, encode, temp_dir, output_dir):
    # 这里写需要并发执行的任务逻辑
    download(url, encode, temp_dir, output_dir)


def download_threadpool(urls, encode, temp_dir, output_dir, workers):
    # 创建线程池，设置最大线程数为3
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
    # 创建队列，用于存储任务
    q = queue.Queue()

    # 向队列中添加任务
    for url in urls:
        q.put((url, encode, temp_dir, output_dir))  # 假设每个任务的参数为i和i+1

    # 启动线程处理队列中的任务
    while not q.empty():
        item = q.get()
        executor.submit(task_function, *item)  # 提交任务到线程池

    # 等待所有任务完成
    executor.shutdown(wait=True)
    print("全部任务已完成")
