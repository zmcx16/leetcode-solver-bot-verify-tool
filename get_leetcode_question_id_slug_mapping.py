import logging
import argparse
import json
import requests


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "-log-level", dest="log_level", default="INFO")
    parser.add_argument("-o", "-output-path", dest="output_path", default="./leetcode_question_id_slug_mapping.json")
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    res = requests.get("https://leetcode.com/api/problems/all/")
    problems = res.json()
    output = {"question_id_mapping": []}
    question_id_list = []

    for p in problems["stat_status_pairs"]:
        question_id = p["stat"]["question_id"]
        frontend_question_id = p["stat"]["frontend_question_id"]
        slug = p["stat"]["question__title_slug"]

        question_id_list.append(
            {
                "question_id": question_id,
                "frontend_question_id": frontend_question_id,
                "slug": slug,
                "is_mapped": question_id == frontend_question_id,
            }
        )

    output["question_id_mapping"] = sorted(
        question_id_list, key=lambda d: d["question_id"]
    )

    logging.info(output)

    with open(args.output_path, "w") as f:
        json.dump(output, f, indent=2)
