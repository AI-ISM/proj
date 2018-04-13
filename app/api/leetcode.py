import json
import requests
from django.http import HttpResponse
import os


def question_all(requset):
    filename = 'app/static/json/questionsAll.json'
    confname = 'app/static/json/leetcode_conf.json'

    if os.path.exists(filename):
        with open(filename) as f:
            response = json.loads(f.read())
    else:
        with open(confname, encoding='utf-8') as f:
            conf = json.load(f)
        problem_url = conf['url']['problemAll']
        title_url = conf['url']['title_translations']

        response = requests.get(problem_url).json()['stat_status_pairs']
        titles = requests.get(title_url).json()['data']['translations']
        titles_dict = dict()
        for item in titles:
            titles_dict[item['question']['questionId']] = item['title']
        for item in response:
            question_id = item['stat']['question_id']
            if str(question_id) in titles_dict.keys():
                item['stat']['title_cn'] = titles_dict[str(question_id)]
            else:
                item['stat']['title_cn'] = item['stat']['question__title']
        # 若不存在list则生成该文件
        with open(filename, "w") as f:
            json.dump(response, f)
    return HttpResponse(json.dumps(response), content_type="application/json")


# 根据titile_slug检索返回数据
def question(request, title_slug):
    confname = 'app/static/json/leetcode_conf.json'
    with open(confname, encoding='utf-8') as f:
        conf = json.load(f)
        question_url = conf['url']['questionItem'] + '{"titleSlug": "' + title_slug + '"}'
        solution_url = conf['url']['solution'] + title_slug + "/solution/"

    response = requests.get(question_url).json()['data']['question']
    # response中添加solution
    response['solution'] = requests.get(solution_url).json()['solutionHTML']
    return HttpResponse(json.dumps(response), content_type="application/json")

