import json
import requests
from django.http import HttpResponse


def lists(requset):
    with open('app/static/json/leetcode_conf.json', 'rb') as f:
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
        if question_id in titles_dict.keys():
            item['stat']['title_cn'] = titles_dict[question_id]
        else:
            item['stat']['title_cn'] = item['stat']['question__title']

    return HttpResponse(json.dumps(response), content_type="application/json")

