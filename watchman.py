import datetime
import requests
import sys
import time


COMPANY = ''
NAME = ''
PW = ''

FIRST_DOM = 25
LAST_DOM = FIRST_DOM - 1

COMING_TIME = '11:00'.split(':')
LEAVING_TIME = '20:00'.split(':')

if len(sys.argv) < 2 or ('run' not in sys.argv and 'show' not in sys.argv):
    print 'Usage: %s run/show <except_dates_separated_by_commas>' % sys.argv[0]
    print 'Ex.: %s run 30,31' % sys.argv[0]
    print 'Please notice weekends are skipped automatically.'
    sys.exit()

except_days = []
if len(sys.argv) == 3 and (',' in sys.argv[2] or sys.argv[2].isdigit()):
    except_days = sys.argv[2].split(',')

now = datetime.datetime.now()
first_date = datetime.datetime(now.year, now.month-1, FIRST_DOM)
last_date = datetime.datetime(now.year, now.month, LAST_DOM)
step = datetime.timedelta(days=1)


while first_date <= last_date:
    if int(first_date.strftime('%w')) < 5 and str(first_date.day) not in except_days:
        print first_date.date()
        if sys.argv[1] == 'run':
            login = requests.post('http://checkin.timewatch.co.il/punch/punch2.php', {'comp':COMPANY, 'name':NAME, 'pw':PW, 'B1.x':'31', 'B1.y':'12'})
            requests.post('http://checkin.timewatch.co.il/punch/editwh3.php', {
                            'e':'186951', 'tl':'186951', 'c':'2391', 
                            'd':first_date.strftime('%Y-%m-%d'), 
                            'jd':'2017-09-01', 'nextdate':'', 'atypehidden':'0', 'inclcontracts':'0', 'job':'0', 'allowabsence':'3', 'allowremarks':'1', 'task0':'0', 'taskdescr0':'', 'what0':'1',
                            'emm0':COMING_TIME[1],
                            'ehh0':COMING_TIME[0],
                            'xmm0':LEAVING_TIME[1],
                            'xhh0':LEAVING_TIME[0],
                            'task1':'0', 'taskdescr1':'', 'what1':'1', 'emm1':'', 'ehh1':'', 'xmm1':'', 'xhh1':'', 'task2':'0', 'taskdescr2':'', 'what2':'1', 'emm2':'', 'ehh2':'', 'xmm2':'', 'xhh2':'', 'task3':'0', 'taskdescr3':'', 'what3':'1', 'emm3':'', 'ehh3':'', 'xmm3':'', 'xhh3':'', 'task4':'0', 'taskdescr4':'', 'what4':'1', 'emm4':'', 'ehh4':'', 'xmm4':'', 'xhh4':'', 'excuse':'0', 'atype':'0', 'fhhh':'', 'fhmm':'', 'thhh':'', 'thmm':'', 'teken':'0', 'remark':'', 'speccomp':'', 'B1.x':'60', 'B1.y':'10'},
                             cookies=login.cookies)
    first_date += step
    time.sleep(2)
