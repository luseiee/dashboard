
from . import main
from flask import render_template, abort, flash, redirect, url_for, request
import re, json
from flask import current_app
import requests

# @main.route('/test', methods=['GET'])
# def test():
#     return render_template('newdash/test.html', name = 'phil')

@main.route('/', methods=['GET'])
def index():
    return render_template('newdash/index.html')

# Passing JSON files

@main.route('/traffic-data.json', methods=['GET'])
def traffic_data():
    # content = urllib2.urlopen(current_app.config['TRAFFIC_DATA_URL']).read(300)
    # r = requests.get(current_app.config['TRAFFIC_DATA_URL'])
    # if (r.status_code != 200):
    #     return json.dumps({'Error': 10})
    # content = r.text[0:500]
    # traffic_www = re.findall('origin\.www[\s\S]*?origin',content)[0]
    # pod = re.findall('weight.*www',traffic_www)
    # ratio = {}
    # for p in pod:
    #     num = int(re.findall(':.*\.', p)[0][2:-1])
    #     podid = 'POD' + re.findall('lvs.*-', p)[0][3:-1] # + ': %' + str(num)
    #     ratio[podid] = num
    # return json.dumps(ratio)
    return json.dumps({"POD01": 50, "POD02": 50})

@main.route('/disk-space-data.json', methods=['GET'])
def disk_space_data():
    # top_n = current_app.config['DISK_SPACE_TOP_N']
    # with current_app.open_resource('static/newdash/phil/disk_space.txt') as f:
    #     content = f.readlines()
    # d = []
    # for c in content:
    #     blade = re.findall('lvsp.*]', c)[0][:-1]
    #     percent = int(re.findall('\d+%', c)[0][:-1])
    #     disk = c.split()[-1]
    #     d.append([blade, percent, disk])
    # # d = [['lvsp05pay003',39,'/boot'], ...]
    # d = sorted(d, key=lambda d : d[1], reverse = True)[0:top_n]
    # # e.g.:i[0] = 'lvsp05pay003', i[1] = 39, i[2] = /boot'
    # rank = {i[0] + ':' + i[2] : i[1] for i in d}
    # return json.dumps(rank)
    return json.dumps({'lvsp05pay003/boot': 92, 'lvsp05pay103/boot': 91, 'lvsp05pay006/boot': 83, 'lvsp05pay005/boot': 80, 'lvsp05jos002/boot': 76, 'lvsp05pay102/boot': 72, 'lvsp05jos001/boot': 66, 'lvsp05pay104/boot': 50, 'lvsp05pay101/boot': 39, 'lvsp05pay002/boot': 45})


