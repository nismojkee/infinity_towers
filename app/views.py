"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.urls import reverse

import os
import requests

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
        }
    )

def apartments(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/apartments.html',
        {
            'title':'Apartments',
        }
    )

def gallery(request):
    assert isinstance(request, HttpRequest)

    path = "./app/static/app/images/gallery/full/"
    img_list = os.listdir(path)   
    paththumb = "./app/static/app/images/gallery/thumbs/"
    thumb_list = os.listdir(paththumb)

    return render_to_response(
        'app/gallery.html',
        {
            'title': 'Gallery Page',
            'images': img_list,
            'thumbs': thumb_list,
        }
    )

def location(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/location.html',
        {
            'title':'Location Page',
        }
    )

def level(request):
    assert isinstance(request, HttpRequest)

    title = ''
    message = ''
    
    level = request.COOKIES['level']
    tower = request.COOKIES['tower']
    levelcookie = tower + level
    
    coord_left = ''
    coord_mid_left = ''
    coord_mid = ''
    coord_mid_right = ''
    coord_right = ''

    #room coordinates for Tower A
    if levelcookie == 'A1':
        coord_left = '868,626,780,744,363,555,383,131,519,90,720,86,871,201'
        coord_mid_left = ''
        coord_mid = '871,312,1138,324,1133,857,866,830'
        coord_mid_right = ''
        coord_right = '1138,357,1449,377,1439,854,1133,850'
    elif levelcookie == 'A2':
        coord_left = '687,80,682,336,581,344,567,661,177,394,307,28'
        coord_mid_left = '683,317,861,314,931,508,924,852,713,862,564,659,582,339'
        coord_mid = '931,502,1160,485,1150,889,923,854'
        coord_mid_right = '1158,586,1261,588,1401,618,1411,902,1147,882'
        coord_right = '1256,583,1197,535,1188,394,1258,291,1427,316,1544,427,1630,570,1672,704,1663,820,1612,877,1522,907,1412,912,1406,618'
    elif levelcookie == 'A3':
        coord_left = '687,80,682,336,581,344,567,661,177,394,307,28'
        coord_mid_left = '683,317,861,314,931,508,924,852,713,862,564,659,582,339'
        coord_mid = '931,502,1160,485,1150,889,923,854'
        coord_mid_right = '1158,586,1261,588,1401,618,1411,902,1147,882'
        coord_right = '1256,583,1197,535,1188,394,1258,291,1427,316,1544,427,1630,570,1672,704,1663,820,1612,877,1522,907,1412,912,1406,618'
    elif levelcookie == 'A4':
        coord_left = '687,80,682,336,581,344,567,661,177,394,307,28'
        coord_mid_left = '683,317,861,314,931,508,924,852,713,862,564,659,582,339'
        coord_mid = '931,502,1160,485,1150,889,923,854'
        coord_mid_right = '1158,586,1261,588,1401,618,1411,902,1147,882'
        coord_right = '1256,583,1197,535,1188,394,1258,291,1427,316,1544,427,1630,570,1672,704,1663,820,1612,877,1522,907,1412,912,1406,618'
    elif levelcookie == 'A5':
        coord_left = '687,80,682,336,581,344,567,661,177,394,307,28'
        coord_mid_left = '683,317,861,314,931,508,924,852,713,862,564,659,582,339'
        coord_mid = '931,502,1160,485,1150,889,923,854'
        coord_mid_right = '1158,586,1261,588,1401,618,1411,902,1147,882'
        coord_right = '1256,583,1197,535,1188,394,1258,291,1427,316,1544,427,1630,570,1672,704,1663,820,1612,877,1522,907,1412,912,1406,618'
    elif levelcookie == 'A6':
        coord_left = '687,80,682,336,581,344,567,661,177,394,307,28'
        coord_mid_left = '683,317,861,314,931,508,924,852,713,862,564,659,582,339'
        coord_mid = '931,502,1160,485,1150,889,923,854'
        coord_mid_right = '1158,586,1261,588,1401,618,1411,902,1147,882'
        coord_right = '1256,583,1197,535,1188,394,1258,291,1427,316,1544,427,1630,570,1672,704,1663,820,1612,877,1522,907,1412,912,1406,618'
    elif levelcookie == 'A7':
        coord_left = '846,78,838,502,820,525,820,664,849,678,846,817,155,405,310,45'
        coord_mid_left = ''
        coord_mid = '823,517,1180,512,1182,595,1266,595,1268,928,843,812,846,674,816,661'
        coord_mid_right = ''
        coord_right = '1183,591,1172,294,1369,292,1647,648,1562,885,1266,927,1263,593'
    elif levelcookie == 'A8':
        coord_left = '338,100,742,106,745,756,300,581'
        coord_mid_left = ''
        coord_mid = '745,754,1128,845,1122,457,1009,455,1009,289,742,287'
        coord_mid_right = ''
        coord_right = '1128,842,1550,811,1525,435,992,25,1011,453,1125,455'
    elif levelcookie == 'A9':
        coord_left = '570,633,587,307,690,304,697,12,225,13,233,510'
        coord_mid_left = ''
        coord_mid = '569,629,931,834,936,251,590,299'
        coord_mid_right = ''
        coord_right = '936,458,1273,234,1685,571,1587,918,933,839'
    elif levelcookie == 'A10':
        coord_left = '737,663,750,334,856,331,861,38,365,47,443,473'
        coord_mid_left = ''
        coord_mid = '738,661,1104,862,1110,314,753,332'
        coord_mid_right = ''
        coord_right = '1105,864,1479,942,1496,488,1109,478'
    elif levelcookie == 'A11':
        coord_left = '737,663,750,334,856,331,861,38,365,47,443,473'
        coord_mid_left = ''
        coord_mid = '738,661,1104,862,1110,314,753,332'
        coord_mid_right = ''
        coord_right = '1105,864,1479,942,1496,488,1109,478'
    elif levelcookie == 'A12':
        coord_left = '737,663,750,334,856,331,861,38,365,47,443,473'
        coord_mid_left = ''
        coord_mid = '738,661,1104,862,1110,314,753,332'
        coord_mid_right = ''
        coord_right = '1105,864,1479,942,1496,488,1109,478'
    elif levelcookie == 'A13':
        coord_left = '737,663,750,334,856,331,861,38,365,47,443,473'
        coord_mid_left = ''
        coord_mid = '738,661,1104,862,1110,314,753,332'
        coord_mid_right = ''
        coord_right = '1105,864,1479,942,1496,488,1109,478'
    elif levelcookie == 'A14':
        coord_left = '737,663,750,334,856,331,861,38,365,47,443,473'
        coord_mid_left = ''
        coord_mid = '738,661,1104,862,1110,314,753,332'
        coord_mid_right = ''
        coord_right = '1105,864,1479,942,1496,488,1109,478'
    elif levelcookie == 'A15':
        coord_left = '737,663,750,334,856,331,861,38,365,47,443,473'
        coord_mid_left = ''
        coord_mid = '738,661,1104,862,1110,314,753,332'
        coord_mid_right = ''
        coord_right = '1105,864,1479,942,1496,488,1109,478'
    elif levelcookie == 'A16':
        coord_left = '737,663,750,334,856,331,861,38,365,47,443,473'
        coord_mid_left = ''
        coord_mid = '738,661,1104,862,1110,314,753,332'
        coord_mid_right = ''
        coord_right = '1105,864,1479,942,1496,488,1109,478'
    elif levelcookie == 'A17':
        coord_left = '737,663,750,334,856,331,861,38,365,47,443,473'
        coord_mid_left = ''
        coord_mid = '738,661,1104,862,1110,314,753,332'
        coord_mid_right = ''
        coord_right = '1105,864,1479,942,1496,488,1109,478'
    elif levelcookie == 'A18':
        coord_left = '737,663,750,334,856,331,861,38,365,47,443,473'
        coord_mid_left = ''
        coord_mid = '738,661,1104,862,1110,314,753,332'
        coord_mid_right = ''
        coord_right = '1105,864,1479,942,1496,488,1109,478'
    elif levelcookie == 'A19':
        coord_left = '737,663,750,334,856,331,861,38,365,47,443,473'
        coord_mid_left = ''
        coord_mid = '738,661,1104,862,1110,314,753,332'
        coord_mid_right = ''
        coord_right = '1105,864,1479,942,1496,488,1109,478'
    elif levelcookie == 'A20':
        coord_left = '878,791,876,659,848,644,864,95,291,78,336,691'
        coord_mid_left = ''
        coord_mid = ''
        coord_mid_right = ''
        coord_right = '854,510,1253,294,1589,628,1444,902,881,789,878,663,848,646'
    elif levelcookie == 'A21':
        coord_left = '622,135,164,144,157,689,625,820,622,621,607,613'
        coord_mid_left = ''
        coord_mid = '624,819,622,621,604,608,620,229,1089,244,1310,865'
        coord_mid_right = ''
        coord_right = '1170,8,1200,493,1715,538,1720,35'

    #room coodinates for Tower B
    elif levelcookie == 'B1':
        coord_left = '429,344,747,334,751,856,394,852'
        coord_mid_left = ''
        coord_mid = '751,856,1015,803,1011,308,746,319'
        coord_mid_right = ''
        coord_right = '1008,301,1099,67,1490,67,1481,790,1010,800'
    elif levelcookie == 'B2':
        coord_left = '473,613,626,611,703,543,701,267,188,295,173,911,473,943'
        coord_mid_left = '654,588,724,591,726,935,472,940,477,622'
        coord_mid = '719,465,950,465,943,901,722,931'
        coord_mid_right = '943,897,1320,728,1294,330,950,310'
        coord_right = '1320,724,1750,340,1674,22,1169,13,1184,314,1302,319'
    elif levelcookie == 'B3':
        coord_left = '473,613,626,611,703,543,701,267,188,295,173,911,473,943'
        coord_mid_left = '654,588,724,591,726,935,472,940,477,622'
        coord_mid = '719,465,950,465,943,901,722,931'
        coord_mid_right = '943,897,1320,728,1294,330,950,310'
        coord_right = '1320,724,1750,340,1674,22,1169,13,1184,314,1302,319'
    elif levelcookie == 'B4':
        coord_left = '473,613,626,611,703,543,701,267,188,295,173,911,473,943'
        coord_mid_left = '654,588,724,591,726,935,472,940,477,622'
        coord_mid = '719,465,950,465,943,901,722,931'
        coord_mid_right = '943,897,1320,728,1294,330,950,310'
        coord_right = '1320,724,1750,340,1674,22,1169,13,1184,314,1302,319'
    elif levelcookie == 'B5':
        coord_left = '473,613,626,611,703,543,701,267,188,295,173,911,473,943'
        coord_mid_left = '654,588,724,591,726,935,472,940,477,622'
        coord_mid = '719,465,950,465,943,901,722,931'
        coord_mid_right = '943,897,1320,728,1294,330,950,310'
        coord_right = '1320,724,1750,340,1674,22,1169,13,1184,314,1302,319'
    elif levelcookie == 'B6':
        coord_left = '473,613,626,611,703,543,701,267,188,295,173,911,473,943'
        coord_mid_left = '654,588,724,591,726,935,472,940,477,622'
        coord_mid = '719,465,950,465,943,901,722,931'
        coord_mid_right = '943,897,1320,728,1294,330,950,310'
        coord_right = '1320,724,1750,340,1674,22,1169,13,1184,314,1302,319'
    elif levelcookie == 'B7':
        coord_left = '616,599,703,591,701,251,204,515,219,877,611,929'
        coord_mid_left = ''
        coord_mid = '616,598,722,595,719,482,1058,498,1056,659,1015,823,610,921'
        coord_mid_right = ''
        coord_right = '1023,780,1652,438,1648,99,1176,1,1053,332'
    elif levelcookie == 'B8':
        coord_left = '759,464,835,462,834,86,326,329,342,811,759,834'
        coord_mid_left = ''
        coord_mid = '759,830,1131,724,1128,295,835,342,839,460,752,465'
        coord_mid_right = ''
        coord_right = '133,719,1586,483,1586,66,1216,89,1128,295'
    elif levelcookie == 'B9':
        coord_left = '945,402,943,845,387,916,140,739,294,337,726,204'
        coord_mid_left = ''
        coord_mid = '1294,290,942,282,945,843,1319,626'
        coord_mid_right = ''
        coord_right = '1320,624,1681,371,1657,56,1515,13,1171,13,1182,278,1300,288'
    elif levelcookie == 'B10':
        coord_left = '776,472,782,892,392,932,390,465'
        coord_mid_left = ''
        coord_mid = '1134,317,777,307,782,888,1148,682'
        coord_mid_right = ''
        coord_right = '1149,680,1508,339,1506,31,993,25,1018,305,1136,317'
    elif levelcookie == 'B11':
        coord_left = '776,472,782,892,392,932,390,465'
        coord_mid_left = ''
        coord_mid = '1134,317,777,307,782,888,1148,682'
        coord_mid_right = ''
        coord_right = '1149,680,1508,339,1506,31,993,25,1018,305,1136,317'
    elif levelcookie == 'B12':
        coord_left = '776,472,782,892,392,932,390,465'
        coord_mid_left = ''
        coord_mid = '1134,317,777,307,782,888,1148,682'
        coord_mid_right = ''
        coord_right = '1149,680,1508,339,1506,31,993,25,1018,305,1136,317'
    elif levelcookie == 'B13':
        coord_left = '776,472,782,892,392,932,390,465'
        coord_mid_left = ''
        coord_mid = '1134,317,777,307,782,888,1148,682'
        coord_mid_right = ''
        coord_right = '1149,680,1508,339,1506,31,993,25,1018,305,1136,317'
    elif levelcookie == 'B14':
        coord_left = '776,472,782,892,392,932,390,465'
        coord_mid_left = ''
        coord_mid = '1134,317,777,307,782,888,1148,682'
        coord_mid_right = ''
        coord_right = '1149,680,1508,339,1506,31,993,25,1018,305,1136,317'
    elif levelcookie == 'B15':
        coord_left = '776,472,782,892,392,932,390,465'
        coord_mid_left = ''
        coord_mid = '1134,317,777,307,782,888,1148,682'
        coord_mid_right = ''
        coord_right = '1149,680,1508,339,1506,31,993,25,1018,305,1136,317'
    elif levelcookie == 'B16':
        coord_left = '776,472,782,892,392,932,390,465'
        coord_mid_left = ''
        coord_mid = '1134,317,777,307,782,888,1148,682'
        coord_mid_right = ''
        coord_right = '1149,680,1508,339,1506,31,993,25,1018,305,1136,317'
    elif levelcookie == 'B17':
        coord_left = '776,472,782,892,392,932,390,465'
        coord_mid_left = ''
        coord_mid = '1134,317,777,307,782,888,1148,682'
        coord_mid_right = ''
        coord_right = '1149,680,1508,339,1506,31,993,25,1018,305,1136,317'
    elif levelcookie == 'B18':
        coord_left = '776,472,782,892,392,932,390,465'
        coord_mid_left = ''
        coord_mid = '1134,317,777,307,782,888,1148,682'
        coord_mid_right = ''
        coord_right = '1149,680,1508,339,1506,31,993,25,1018,305,1136,317'
    elif levelcookie == 'B19':
        coord_left = '776,472,782,892,392,932,390,465'
        coord_mid_left = ''
        coord_mid = '1134,317,777,307,782,888,1148,682'
        coord_mid_right = ''
        coord_right = '1149,680,1508,339,1506,31,993,25,1018,305,1136,317'
    elif levelcookie == 'B20':
        coord_left = '1025,436,618,303,262,599,312,856,817,904,1025,791'
        coord_mid_left = ''
        coord_mid = ''
        coord_mid_right = ''
        coord_right = '1023,786,1599,469,1584,81,1016,98'
    elif levelcookie == 'B21':
        coord_left = '668,559,704,22,189,15,121,520'
        coord_mid_left = ''
        coord_mid = '1266,417,844,306,628,685,794,854,1269,756'
        coord_mid_right = ''
        coord_right = '1264,413,1354,127,1706,116,1714,463,1269,755'

    #reset coordinates
    else:
        coord_left = ''
        coord_mid_left = ''
        coord_mid = ''
        coord_mid_right = ''
        coord_right = ''
    return render(
        request,
        'app/level.html',
        {
            'title': 'Level '+ tower + str(int(level) + 2),
            'bgimage': levelcookie,
            'coord_left': coord_left,
            'coord_mid_left': coord_mid_left,
            'coord_mid': coord_mid,
            'coord_mid_right': coord_mid_right,
            'coord_right': coord_right,
        }
    )

def room(request):
    assert isinstance(request, HttpRequest)
    level = request.COOKIES['level']
    tower = request.COOKIES['tower']
    room = request.COOKIES['room']
    if room == '1':
        side = 'left'
    elif room == '2':
        side = 'mid_left'
    elif room == '3':
        side = 'mid'
    elif room == '4':
        side = 'mid_right'
    else:
        side = 'right'
    return render(
        request,
        'app/room.html',
        {
            'title': 'Room',
            'bgimage': './static/app/images/level/room/room_'+tower+level+'_'+side,
            'level': 'Level '+ tower + str(int(level) + 2),
        }
    )