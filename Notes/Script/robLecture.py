import time
import requests
import re
from datetime import datetime,timedelta


headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.wjx.top',
    'Pragma': 'no-cache',
    'Referer': 'https://www.wjx.top/vm/QdBlr7J.aspx',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def decode_id(input):
    return input ^ 2130030173

def dataenc(e, ktimes):
    t = ktimes % 10
    if t == 0:
        t = 1
    i = []
    for a in range(len(e)):
        n = ord(e[a]) ^ t
        i.append(chr(n))
    return ''.join(i)

# atcivityid = decode_id(1873795034)
ktimes=25

def qiangke(start_time,cst,xuehao,name,link):
    headers1 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(link, headers=headers1).text
    pattern = r'var jqnonce="([^"]+)"'
    match = re.search(pattern, response).group(1)
    if match:
        jqsign = dataenc(match,ktimes)
        jcn = dataenc(name, ktimes)
        params = {
            "shortid": link.split(".")[-2].split("/")[-1],
            "starttime": start_time,
            "cst": str(cst),
            "submittype": "1",
            "ktimes": ktimes,
            "hlv": "1",
            "rn": "2031553352.50912392",  ##首页获取
            "jcn": jcn,
            "nw": "1",
            "jwt": "4",
            "jpm": "27",
            "t": str(cst + 5),
            "wxfs": "100",
            "jqnonce": match,  ##首页获取
            "jqsign": jqsign
        }
        response = requests.post(
            'https://www.wjx.top/joinnew/processjq.ashx?',
            headers=headers,
            data={
                'submitdata': f'1${xuehao}{"}"}2${name}',
            },
            params=params
        )

        print(response.text)


def run_task_at(target_time, *args):
    """
    死循环检测时间，在指定时间执行函数。

    参数:
    - target_time: 目标时间 (datetime 对象)
    - func: 要执行的函数
    - *args: 传递给函数的参数
    - **kwargs: 传递给函数的关键字参数
    """
    print(args)
    print(f"开始检测时间，目标时间为：{target_time}")
    while True:
        current_time = datetime.now()
        if current_time >= target_time:
            print(f"到达指定时间：{current_time}")
            qiangke(str((datetime.now() - timedelta(seconds=1)).strftime("%Y/%m/%d %H:%M:%S")),int(time.time() * 1000),*args)  # 执行指定任务
            break
        time.sleep(0.1)  # 减少 CPU 占用

if __name__ == '__main__':
    target_time="2024/12/04 19:43:01"
    xingming="王宪"
    xuehao="2024025441"
    link="https://www.wjx.top/vm/tOexPKH.aspx"
    run_task_at(datetime.strptime(target_time, "%Y/%m/%d %H:%M:%S"),*[xuehao,xingming,link])

