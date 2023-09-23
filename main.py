import os
import logging
import time
import argparse
import json
import copy
import glob
from datetime import datetime


def read_question_id_slug():
    with open("./leetcode_question_id_slug_mapping.json", 'r', encoding='utf-8') as f:
        question_id_slug_mapping = json.loads(f.read())
    for r in question_id_slug_mapping["question_id_mapping"]:
        id_map_table[r['frontend_question_id']] = {"question_id": r['question_id'], "slug": r['slug']}
    return 0


def generate_questions():
    question_i = 0
    for file_path in glob.iglob(args.dataset_path + '/**', recursive=True):
        if os.path.isfile(file_path) and ".json" in file_path:
            with open(file_path, 'r', encoding='utf-8') as fi:
                dataset = json.loads(fi.read())

            for row in dataset['rows']:
                r = row['row']
                id = r['number']
                difficulty = r['difficulty']
                question = r['question'].split('"""')
                code = question[0].replace("        ", "").strip()
                description = question[1].replace("        ", "").strip()
                # logging.info(r)
                question_template = "{description}\n\nWrite a function:\n\n {code}"
                question_output = question_template.format(description=description, code=code)
                with open(args.questions_path + "/" + str(id) + ".txt", 'w', encoding='utf-8') as fo:
                    fo.write(question_output)
                    logging.info("generate id:" + str(id) + " question done")
                    question_i += 1

    if question_i == 0:
        logging.warning("generate question files == 0, exit")
        return -1
    return 0


def generate_solution(question_path, solver_bot_path, solution_path):
    os.system(f"python \"{solver_bot_path}\" -i \"{question_path}\" -o \"{solution_path}\"")


def generate_solutions(fold, solver_bot_path, questions_path, solutions_path):
    logging.info("run solver_bot to generate all solution.py")
    for fi in range(1, int(fold) + 1):
        # create solution with fold path if not exist
        fold_path = solutions_path + "/fold" + str(fi)
        if not os.path.exists(fold_path):
            os.mkdir(fold_path)

        file_list = os.listdir(questions_path)
        # only keep txt
        file_list = [file for file in file_list if ".txt" in file]
        file_list.sort(key=lambda file: int(''.join(filter(str.isdigit, file))))
        for file in file_list:
            q_path = os.path.join(questions_path, file)
            generate_solution(q_path, solver_bot_path,
                              solutions_path + "/fold" + str(fi) + "/" + file.replace(".txt", ".py"))

    logging.info("run all ai main.py done")


def verify_solutions(fold, solutions_path, verify_path, skip_verify_exist):
    with open("./leetcode_cookies_csrftoken.json", 'r', encoding='utf-8') as fi:
        cookies_csrftoken = json.loads(fi.read())
        logging.info(cookies_csrftoken)

    cookies = cookies_csrftoken['cookies']
    csrf_token = cookies_csrftoken['csrf_token']

    for fi in range(1, int(fold) + 1):
        fold_sol_path = solutions_path + "/fold" + str(fi)
        fold_verify_path = verify_path + "/fold" + str(fi)
        if not os.path.exists(fold_verify_path):
            os.mkdir(fold_verify_path)

        sol_list = []
        for file_path in glob.iglob(fold_sol_path + '/**', recursive=True):
            if os.path.isfile(file_path) and ".py" in file_path:
                sol_list.append(file_path)

        if len(sol_list) == 0:
            logging.warning("verify solutions files == 0, exit")
            return -1

        for sol_file_path in sol_list:
            tid = os.path.basename(sol_file_path).replace(".py", "")
            if skip_verify_exist and os.path.exists(fold_verify_path + "/" + str(id) + ".py"):
                logging.info("id:" + str(id) + " verify result exist, skip")
                continue

            if int(tid) not in id_map_table:
                logging.warning("id:" + str(id) + " not in id_map_table, continue")
                continue

            # verify solution
            url = "https://leetcode.com/problems/" + id_map_table[int(tid)]["slug"] + "/"
            output_path = fold_verify_path + "/" + str(tid) + ".json"
            cmd = f"python ./verify_leetcode.py -u \"{url}\" -i \"{sol_file_path}\" -o \"{output_path}\"" \
                  f" -q \"{str(id_map_table[int(tid)]['question_id'])}\" -t \"{csrf_token}\" -c \"{cookies}\""
            os.system(cmd)
            logging.info("verify id:" + str(tid) + " solution done")

            if not os.path.exists(output_path):
                logging.warning("verify id:" + str(tid) + " solution failed")
                time.sleep(3)
                continue
            time.sleep(10)


def stat_solutions(fold, verify_path, summary_path):
    score_summary = {"success": 0, "failed": 0, "avg_success": 0, "avg_failed": 0, "detail": {}}
    for f_index in range(int(fold)):
        fold_verify_path = verify_path + "/fold" + str(f_index + 1)

        for file_path in glob.iglob(fold_verify_path + '/**', recursive=True):
            if os.path.isfile(file_path) and ".json" in file_path:
                title_id = os.path.basename(file_path).replace(".json", "")
                with open(file_path, 'r', encoding='utf-8') as fi:
                    verify_result = json.loads(fi.read())
                    final_score["fold"][f_index]["detail"][title_id] = verify_result
                    logging.info(verify_result)
                    if verify_result["status_msg"] == "Accepted":
                        final_score["fold"][f_index]["success"] += 1
                    else:
                        final_score["fold"][f_index]["failed"] += 1

                    if verify_result["status_msg"] not in final_score["fold"][f_index]["status_group"]:
                        final_score["fold"][f_index]["status_group"][verify_result["status_msg"]] = [title_id]
                    else:
                        final_score["fold"][f_index]["status_group"][verify_result["status_msg"]] += [title_id]

                    if verify_result["status_msg"] not in score_summary["detail"]:
                        score_summary["detail"][verify_result["status_msg"]] = 1
                    else:
                        score_summary["detail"][verify_result["status_msg"]] += 1

    # stat final score
    for f_index in range(int(fold)):
        final_score["success"] += final_score["fold"][f_index]["success"]
        final_score["failed"] += final_score["fold"][f_index]["failed"]
    final_score["avg_success"] = final_score["success"] / float(fold)
    final_score["avg_failed"] = final_score["failed"] / float(fold)

    score_summary["success"] = final_score["success"]
    score_summary["failed"] = final_score["failed"]
    score_summary["avg_success"] = final_score["avg_success"]
    score_summary["avg_failed"] = final_score["avg_failed"]

    logging.info("verify solutions done, score: " + str(final_score))
    with open(os.path.join(summary_path, "score.json"), 'w', encoding='utf-8') as fo:
        fo.write(json.dumps(final_score))
    with open(os.path.join(summary_path, "score_readable.json"), 'w', encoding='utf-8') as fo:
        fo.write(json.dumps(final_score, indent=4))

    with open(os.path.join(summary_path, "score_summary.json"), 'w', encoding='utf-8') as fo:
        fo.write(json.dumps(score_summary))
    with open(os.path.join(summary_path, "score_summary_readable.json"), 'w', encoding='utf-8') as fo:
        fo.write(json.dumps(score_summary, indent=4))


if __name__ == "__main__":
    # record time
    now = datetime.now()

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-l", "-log-level", dest="log_level", default="INFO")
    parser.add_argument("-d", "-dataset-path", dest="dataset_path", default="./leetcode_dataset")
    parser.add_argument("-q", "-questions-path", dest="questions_path", default="./leetcode_questions")
    parser.add_argument("-a", "-solver-bot-path", dest="solver_bot_path",
                        default="./leetcode_solver_bot/default_chatgpt_bot.py", help="""IMPORTANT:
  If you want to use default_chatgpt_bot.py, 
  you MUST to setup OPENAI_API_KEY & MODEL_NAME in default_chatgpt_bot.py by yourself.""")
    parser.add_argument("-s", "-solutions-path", dest="solutions_path", default="./leetcode_solutions")
    parser.add_argument("-v", "-verify-path", dest="verify_path", default="./leetcode_verify")
    parser.add_argument("-sum", "-summary-path", dest="summary_path", default="./leetcode_summary")
    parser.add_argument("-sve", "--skip-verify-exist", dest="skip_verify_exist", action='store_false')
    parser.add_argument("-u", "-username", dest="username", default="", help="leetcode username")
    parser.add_argument("-p", "-password", dest="password", default="", help="leetcode password")
    parser.add_argument("-r", "-run-steps", dest="run_steps", default="01111", help="""usage: 01111
  1: generate questions from dataset_path
  2: generate solutions by solver bot
  3: how to get leetcode cookies & csrf token 
  [0: use ./leetcode_cookies_csrftoken.json 1: auto login leetcode by username & password]
  4: verify solutions by leetcode website
  5: calculate verify result and output summary""")
    parser.add_argument("-f", "-fold", dest="fold", default="2", help="fold for cross validation")
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    id_map_table = {}
    read_question_id_slug()
    logging.info("read index_url done, id_map_table=" + str(id_map_table))
    if args.run_steps[0] == "1":
        logging.info("generate_questions start")
        generate_questions()
        logging.info("generate_questions done")
    else:
        logging.info("skip generate_questions")

    # init score
    score = {"total": 0, "success": 0, "failed": 0, "status_group": {}, "detail": {}}
    for f in os.listdir(args.questions_path):
        if ".txt" in f:
            qid = f.replace(".txt", "")
            score["detail"][qid] = {}
            score["total"] = len(score["detail"])

    # copy score to multi-fold
    final_score = {"total": score["total"]  * int(args.fold), "success": 0, "failed": 0, "avg_success": 0, "avg_failed": 0, "fold": []}
    for f_i in range(int(args.fold)):
        final_score["fold"].append(copy.deepcopy(score))

    if args.run_steps[1] == "1":
        logging.info("generate_solutions start")
        generate_solutions(args.fold, args.solver_bot_path, args.questions_path, args.solutions_path)
        logging.info("generate_solutions done")
    else:
        logging.info("skip generate_solutions")

    if args.run_steps[2] == "1":
        logging.info("get cookies & csrf_token start")
        os.system("python ./login_leetcode.py -u " + args.username + " -p " + args.password)
        logging.info("get cookies & csrf_token done")
    else:
        logging.info("skip get cookies & csrf_token")

    if args.run_steps[3] == "1":
        logging.info("verify_solutions start")
        verify_solutions(args.fold, args.solutions_path, args.verify_path, args.skip_verify_exist)
        logging.info("verify_solutions done")
    else:
        logging.info("skip verify_solutions")

    if args.run_steps[4] == "1":
        logging.info("stat_solutions start")
        stat_solutions(args.fold, args.verify_path, args.summary_path)
        logging.info("stat_solutions done")
    else:
        logging.info("skip stat_solutions")

    logging.info("total time: " + str(datetime.now() - now))
    logging.info("all done")
