# leetcode-solver-bot-verify-tool


This is a command-line tool for automating verify your coding bot performance by LeetCode problem database.

## Usage

### Prerequisites

Before using this tool, make sure you have the following:

- Python 3.9 or higher installed
- Your OPENAI API KEY (if you want to use default bot, you need update OPENAI_API_KEY in ./leetcode_solver_bot/default_chatgpt_bot.py)
- Firefox installed (log in to LeetCode and obtain cookies and the CSRF token)
- Required Python libraries (install with `pip install -r requirements.txt`):
  - langchain
  - tqdm
  - openai
  - requests
  - scipy
  - webdriver-manager (log in to LeetCode and obtain cookies and the CSRF token)
  - selenium (log in to LeetCode and obtain cookies and the CSRF token)

If you don't want to auto login LeetCode by username and password, you can prepare your own LeetCode cookies and CSRF token and put them in `./leetcode_cookies_csrftoken.json`.
```
{"cookies": {your cookies}, "csrf_token": {your csrf token}}
```

### Command Line Arguments

You can run the tool main.py with the following command line arguments:
```
`-l`,   `--log-level`: Set the log level (default: INFO).
`-d`,   `--dataset-path`: Set the path to the LeetCode dataset (default: ./leetcode_dataset).
`-q`,   `--questions-path`: Set the path to store generated questions (default: ./leetcode_questions).
`-a`,   `--solver-bot-path`: Set the path to the solver bot script (default: ./leetcode_solver_bot/default_chatgpt_bot.py). 
         - IMPORTANT: If you want to use default_chatgpt_bot.py, you MUST set up OPENAI_API_KEY and MODEL_NAME in default_chatgpt_bot.py by yourself.
`-s`,   `--solutions-path`: Set the path to store generated solutions (default: ./leetcode_solutions).
`-v`,   `--verify-path`: Set the path to store verification results (default: ./leetcode_verify).
`-sum`, `--summary-path`: Set the path to store summary results (default: ./leetcode_summary).
`-sve`, `--skip-verify-exist`: Skip verification if verify result already exist (default: False).
`-u`,   `--username`: Set your LeetCode username.
`-p`,   `--password`: Set your LeetCode password.
`-r`,   `--run-steps`: Set the steps to run (default: 01111).
         - 1: Generate questions from the dataset.
         - 2: Generate solutions using the solver bot.
         - 3: How to get LeetCode cookies and CSRF token. 
              (0: Use ./leetcode_cookies_csrftoken.json, 1: Auto login to LeetCode by username and password)
         - 4: Verify solutions on the LeetCode website.
         - 5: Calculate verification results and output a summary.
`-f`,   `--fold`: Set the fold for cross-validation (default: 2).
```

## Verfiy result on LeetCode No.1-100

| Default ChatGPT bot | Accepted | Wrong Answer | Runtime Error | Time Limit Exceeded | Memory Limit Exceeded | Generate Solution Failed |
|---------------------|----------|--------------|---------------|---------------------|-----------------------|--------------------------|
| Fold1               | 79       | 2            | 16            | 1                   | 1                     | 0                        |
| Fold2               | 80       | 4            | 14            | 1                   | 0                     | 0                        |
| Avg                 | 79.5     | 3            | 15            | 1                   | 0.5                   | 0                        |


## LeetCode problem dataset

LeetCode Problem 1-2574 (https://huggingface.co/datasets/BoyuanJackchen/leetcode_free_questions_labeled)

## Output

The tool will generate the following files:
- leetcode_questions/*.txt (parse the questions from the dataset)
  ```
  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
  You may assume that each input would have exactly one solution, and you may not use the same element twice.
  You can return the answer in any order.
  Example 1:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
  Example 2:
  Input: nums = [3,2,4], target = 6
  Output: [1,2]
  Example 3:
  Input: nums = [3,3], target = 6
  Output: [0,1]
  
  Write a function:
  
   class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
  ```
- leetcode_solutions/fold*/*.py (generate solutions using the solver bot)
  ```
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          complement_map = {}
          for i, num in enumerate(nums):
              complement = target - num
              if complement in complement_map:
                  return [complement_map[complement], i]
              complement_map[num] = i
          return []
  ```
- leetcode_verify/fold*/*.json (verify solutions on the LeetCode website)
  ```
  {
     "status_code":10,
     "lang":"python3",
     "run_success":true,
     "status_runtime":"53 ms",
     "memory":17580000,
     "question_id":"1",
     "elapsed_time":77,
     "compare_result":"111111111111111111111111111111111111111111111111111111111111",
     "code_output":"",
     "std_output":"",
     "last_testcase":"",
     "expected_output":"",
     "task_finish_time":1695428729602,
     "task_name":"judger.judgetask.Judge",
     "finished":true,
     "total_correct":60,
     "total_testcases":60,
     "runtime_percentile":97.76090000000002,
     "status_memory":"17.6 MB",
     "memory_percentile":48.132,
     "pretty_lang":"Python3",
     "submission_id":"1056710682",
     "status_msg":"Accepted",
     "state":"SUCCESS"
  }
  ```
- leetcode_summary/*.json (calculate verification results and output a summary)
  - score_summary_readable.json
  ```  
  {
      "success": 5,
      "failed": 1,
      "avg_success": 2.5,
      "avg_failed": 0.5,
      "detail": {
          "Accepted": 5,
          "Runtime Error": 1
      }
  }
  ```
  - score_readable.json
  ```
  {
      "total": 6,
      "success": 5,
      "failed": 1,
      "avg_success": 2.5,
      "avg_failed": 0.5,
      "fold": [
          {
              "total": 3,
              "success": 2,
              "failed": 1,
              "status_group": {
                  "Accepted": [
                      "1",
                      "53"
                  ],
                  "Runtime Error": [
                      "24"
                  ]
              },
              "detail": {
                  "1": {
                      "status_code": 10,
                      "lang": "python3",
                      "run_success": true,
                      "status_runtime": "55 ms",
                      "memory": 17564000,
                      "question_id": "1",
                      "elapsed_time": 95,
                      "compare_result": "111111111111111111111111111111111111111111111111111111111111",
                      "code_output": "",
                      "std_output": "",
                      "last_testcase": "",
                      "expected_output": "",
                      "task_finish_time": 1695424400877,
                      "task_name": "judger.judgetask.Judge",
                      "finished": true,
                      "total_correct": 60,
                      "total_testcases": 60,
                      "runtime_percentile": 95.35950000000001,
                      "status_memory": "17.6 MB",
                      "memory_percentile": 48.132,
                      "pretty_lang": "Python3",
                      "submission_id": "1056687771",
                      "status_msg": "Accepted",
                      "state": "SUCCESS"
                  },
                  "24": {
                      "status_code": 15,
                      "lang": "python3",
                      "run_success": false,
                      "runtime_error": "Line 27: NameError: name 'Solution' is not defined",
                      "full_runtime_error": "NameError: name 'Solution' is not defined\n    ret = Solution().swapPairs(param_1)\nLine 27 in _driver (Solution.py)\n    _driver()\nLine 38 in <module> (Solution.py)",
                      "status_runtime": "N/A",
                      "memory": 16288000,
                      "question_id": "24",
                      "elapsed_time": 56,
                      "compare_result": "0000000000000000000000000000000000000000000000000000000",
                      "code_output": "",
                      "std_output": "",
                      "last_testcase": "[1,2,3,4]",
                      "expected_output": "[2,1,4,3]",
                      "task_finish_time": 1695424440498,
                      "task_name": "judger.judgetask.Judge",
                      "finished": true,
                      "total_correct": 0,
                      "total_testcases": 55,
                      "runtime_percentile": null,
                      "status_memory": "N/A",
                      "memory_percentile": null,
                      "pretty_lang": "Python3",
                      "submission_id": "1056687998",
                      "status_msg": "Runtime Error",
                      "state": "SUCCESS"
                  },
                  "53": {
                      "status_code": 10,
                      "lang": "python3",
                      "run_success": true,
                      "status_runtime": "631 ms",
                      "memory": 30472000,
                      "question_id": "53",
                      "elapsed_time": 663,
                      "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                      "code_output": "",
                      "std_output": "",
                      "last_testcase": "",
                      "expected_output": "",
                      "task_finish_time": 1695424472163,
                      "task_name": "judger.judgetask.Judge",
                      "finished": true,
                      "total_correct": 210,
                      "total_testcases": 210,
                      "runtime_percentile": 23.93769999999992,
                      "status_memory": "30.5 MB",
                      "memory_percentile": 73.93380000000002,
                      "pretty_lang": "Python3",
                      "submission_id": "1056688147",
                      "status_msg": "Accepted",
                      "state": "SUCCESS"
                  }
              }
          },
          {
              "total": 3,
              "success": 3,
              "failed": 0,
              "status_group": {
                  "Accepted": [
                      "1",
                      "24",
                      "53"
                  ]
              },
              "detail": {
                  "1": {
                      "status_code": 10,
                      "lang": "python3",
                      "run_success": true,
                      "status_runtime": "62 ms",
                      "memory": 17404000,
                      "question_id": "1",
                      "elapsed_time": 78,
                      "compare_result": "111111111111111111111111111111111111111111111111111111111111",
                      "code_output": "",
                      "std_output": "",
                      "last_testcase": "",
                      "expected_output": "",
                      "task_finish_time": 1695424486254,
                      "task_name": "judger.judgetask.Judge",
                      "finished": true,
                      "total_correct": 60,
                      "total_testcases": 60,
                      "runtime_percentile": 77.6787,
                      "status_memory": "17.4 MB",
                      "memory_percentile": 56.1438,
                      "pretty_lang": "Python3",
                      "submission_id": "1056688213",
                      "status_msg": "Accepted",
                      "state": "SUCCESS"
                  },
                  "24": {
                      "status_code": 10,
                      "lang": "python3",
                      "run_success": true,
                      "status_runtime": "35 ms",
                      "memory": 16416000,
                      "question_id": "24",
                      "elapsed_time": 58,
                      "compare_result": "1111111111111111111111111111111111111111111111111111111",
                      "code_output": "",
                      "std_output": "",
                      "last_testcase": "",
                      "expected_output": "",
                      "task_finish_time": 1695424525233,
                      "task_name": "judger.judgetask.Judge",
                      "finished": true,
                      "total_correct": 55,
                      "total_testcases": 55,
                      "runtime_percentile": 79.52919999999997,
                      "status_memory": "16.4 MB",
                      "memory_percentile": 5.137399999999996,
                      "pretty_lang": "Python3",
                      "submission_id": "1056688456",
                      "status_msg": "Accepted",
                      "state": "SUCCESS"
                  },
                  "53": {
                      "status_code": 10,
                      "lang": "python3",
                      "run_success": true,
                      "status_runtime": "553 ms",
                      "memory": 30544000,
                      "question_id": "53",
                      "elapsed_time": 594,
                      "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                      "code_output": "",
                      "std_output": "",
                      "last_testcase": "",
                      "expected_output": "",
                      "task_finish_time": 1695424556609,
                      "task_name": "judger.judgetask.Judge",
                      "finished": true,
                      "total_correct": 210,
                      "total_testcases": 210,
                      "runtime_percentile": 96.50309999999993,
                      "status_memory": "30.5 MB",
                      "memory_percentile": 38.51220000000002,
                      "pretty_lang": "Python3",
                      "submission_id": "1056688663",
                      "status_msg": "Accepted",
                      "state": "SUCCESS"
                  }
              }
          }
      ]
  }
  ```
- leetcode_summary/p-value/score_p_value.json (using verify_calc_score_p_value.py to calculate p-value by two score.json)
  ```
  {
      "p-value": 0.20483276469913345,
      "statistic": 3.0,
      "./leetcode_summary/p-value/score_readable1.json": {
          "total": 6,
          "success": 6,
          "failed": 0,
          "fold_success": [
              3,
              3
          ]
      },
      "./leetcode_summary/p-value/score_readable2.json": {
          "total": 6,
          "success": 3,
          "failed": 3,
          "fold_success": [
              1,
              2
          ]
      }
  }
  ```


# License
This project is licensed under the terms of the MIT license.
