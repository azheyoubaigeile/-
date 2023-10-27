import requests
from optparse import OptionParser
import threading
import queue
import sys

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
urls = []
result = []
lock = threading.Lock()  # 用于线程安全的访问 result 列表

class WEB_DIR(threading.Thread):
    def __init__(self, url_queue):
        threading.Thread.__init__(self)
        self._queue = url_queue

    def run(self):
        while not self._queue.empty():
            url = self._queue.get()
            try:
                response = requests.get(url, headers=head, timeout=1)
                if response.status_code in [200, 302, 403]:
                    with lock:
                        result.append(url)
                        print('[*]' + url)
            except:
                pass

def run(domain, path, count):
    with open(path, mode='r+') as f1:
        for line in f1.readlines():
            subdomain = line.strip()
            url = subdomain + '.' + domain
            url = 'http://' + url if not url.startswith('http://') else url
            urls.append(url)
        f1.close()

    url_queue = queue.Queue()
    for url in urls:
        url_queue.put(url)

    threads = []
    thread_count = int(count)
    for i in range(thread_count):
        threads.append(WEB_DIR(url_queue))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

def main():
    print("爆破结果如下:")
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="你要扫描的url")
    parser.add_option("-f", "--fil", dest="filename", help="你字典的路径")
    parser.add_option("-t", "--thread", dest="count", type="int", default=10, help="扫描威胁系数")
    (options, args) = parser.parse_args()
    if options.url and options.filename:
        run(options.url, options.filename, options.count)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
