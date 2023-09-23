import logging
import sys
import time
import argparse
import json
import requests


def send_leetcode_check(url, cookies, csrf_token, referer):
    try:
        headers = {
            'content-type': 'application/json',
            'cookie': cookies,
            'x-csrftoken': csrf_token,
            'origin': 'https://leetcode.com',
            'referer': referer,
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        res.raise_for_status()
    except Exception as ex:
        logging.error('Generated an exception: {ex}'.format(ex=ex))
        return -1, ex

    return 0, res.json()


def send_leetcode_submit(url, req_data, cookies, csrf_token):
    try:
        headers = {
            'content-type': 'application/json',
            'cookie': cookies,
            'x-csrftoken': csrf_token,
            'origin': 'https://leetcode.com',
            'referer': url.replace("submit/", ""),
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        res = requests.post(url, req_data, headers=headers)
        res.raise_for_status()
    except Exception as ex:
        logging.error('Generated an exception: {ex}'.format(ex=ex))
        return -1, ex

    return 0, res.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "-log-level", dest="log_level", default="INFO")
    parser.add_argument("-o", "-output-path", dest="output_path", default="verify_result.json")
    parser.add_argument("-u", "-url", dest="url", default="https://leetcode.com/problems/minimum-cost-to-merge-stones/")
    parser.add_argument("-t", "-csrf-token", dest="csrf_token", default="")
    parser.add_argument("-c", "-cookies", dest="cookies", default="")
    parser.add_argument("-s", "-source", dest="code", default='{"lang":"python3","question_id":"1","typed_code":"class Solution:\\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\\n        for i in range(len(nums)):\\n            for j in range(i + 1, len(nums)):\\n                if (i \u0021= j and nums[i] + nums[j] == target):\\n                    return [i, j]\\n        return []"}')
    parser.add_argument("-i", "-input-path", dest="input_path", default="./leetcode_solutions/1000.txt")
    parser.add_argument("-q", "-question-id", dest="question_id", default="1000")  # Note. the question is not the same as the number id
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    code = args.code
    if args.input_path != "" and args.question_id != "":
        with open(args.input_path, 'r', encoding='utf-8') as fi:
            code = json.dumps({"lang": "python3", "question_id": args.question_id, "typed_code": fi.read()})

    logging.info(code)
    ret, resp = send_leetcode_submit(args.url+"submit/", code, args.cookies, args.csrf_token)
    if ret != 0:
        logging.error("send_leetcode_submit failed")
        sys.exit(-1)

    logging.info(resp)
    submission_id = resp["submission_id"]
    while True:
        ret, resp = send_leetcode_check(
            "https://leetcode.com/submissions/detail/"+str(submission_id)+"/check/",
            args.cookies, args.csrf_token, args.url)
        logging.info(resp)
        if ret == 0 and 'state' in resp and resp['state'] == 'SUCCESS':
            with open(args.output_path, 'w', encoding='utf-8') as fo:
                fo.write(json.dumps(resp, separators=(',', ':')))
            sys.exit(0)
        elif ret != 0:
            logging.error("send_leetcode_check failed")
            break
        time.sleep(1)

