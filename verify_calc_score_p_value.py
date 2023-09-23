import logging
import argparse
import json
import scipy.stats as stats


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "-log-level", dest="log_level", default="INFO")
    parser.add_argument("-p1", "-score1-path", dest="score1_path", default="./leetcode_summary/p-value/score_readable1.json")
    parser.add_argument("-p2", "-score2-path", dest="score2_path", default="./leetcode_summary/p-value/score_readable2.json")
    parser.add_argument("-o", "-output-path", dest="output_path", default="./leetcode_summary/p-value/score_p_value.json")
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    score1 = {}
    score2 = {}
    with open(args.score1_path, 'r', encoding='utf-8') as fi:
        score1 = json.loads(fi.read())
    with open(args.score2_path, 'r', encoding='utf-8') as fi:
        score2 = json.loads(fi.read())

    score1_summary = {"total": score1["total"], "success": score1["success"], "failed": score1["failed"],
                      "fold_success": []}
    for fold in score1["fold"]:
        score1_summary["fold_success"].append(fold["success"])

    score2_summary = {"total": score2["total"], "success": score2["success"], "failed": score2["failed"],
                      "fold_success": []}
    for fold in score2["fold"]:
        score2_summary["fold_success"].append(fold["success"])

    statistic, p_value = stats.ttest_rel(score1_summary["fold_success"], score2_summary["fold_success"])
    output = {"p-value": p_value, "statistic": statistic,
              args.score1_path: score1_summary, args.score2_path: score2_summary}
    logging.info(output)
    with open(args.output_path, 'w', encoding='utf-8') as fo:
        fo.write(json.dumps(output, indent=4))
