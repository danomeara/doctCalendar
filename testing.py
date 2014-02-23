import datetime
import re
import calendar
import sys


def main():
    #open file for output
    sys.stdout = open("/home/dan/webDevelopment/calendar/index.html", 'w')
    #Monday is index 0; calendar defaults to Monday being the first day of the
    #week but this can be changed using calendar.setfirstweekday(index_integer)

    firstday = '0'
    year = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'November', 'December']

    #splitting up the current date
    today = datetime.datetime.date(datetime.datetime.now())
    current = re.split('-', str(today))
    current_no = int(current[1])
    current_month = year[current_no - 1]
    current_day = int(re.sub('\A0', '', current[2]))
    current_year = int(current[0])

    print '''

     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN" >
     <HTML>
     <head>

     <title>February 2007</title >
     <style type="text/css">
     html, body { margin: 0; padding: 0 }
     body { background-color:#060; }
     #container { margin: 3em auto 0 3em; padding-bottom: 3em;
                  background-color: #fff; }
     #month { border-collapse: collapse; margin-left: 2em; }
     #month th, #month td { border: 1px solid #000; }
     #month thead { background-color:#9c9; }
     #month td { width: 7em; height: 7em; padding: .2em; vertical-align: top;
                 overflow: auto; }
     td .day { width: 7em; height: 6em; overflow:auto; margin-top: 0; }
     #month tbody .weekend { background-color:#ded; }
     #month tbody .next, #month tbody .previous { background-color:#ddd; }
     .rtop { display:block; background:#060; }
     .rtop * { display: block; height: 1px; overflow: hidden; background:#fff; }
     .r1{margin: 0 0 0 5px}
     .r2{margin: 0 0 0 3px}
     .r3{margin: 0 0 0 2px}
     .r4{margin: 0 0 0 1px; height: 2px}
     #container h1 { margin: 0 0 .5em .5em;
                     font: 2em Arial, Helvetica, sans-serif;
                     color: #060; }
     #month th { font: 1em bold Arial, Helvetica, sans-serif; }
     p {margin-top: 0; }
     </style >
     </head>

     <body>

     <div id="container" >
     <b class="rtop" >
         <b class="r1" ></b >
         <b class="r2" ></b >
         <b class="r3" ></b >
         <b class="r4" ></b >
     </b >
     '''

    print '<h1> %s %s </h1 >' % (current_month, current_year)

    if firstday == '0':
        print '''
         <table id="month" >
         <thead >
         <tr >
         <th >Monday</th >
         <th >Tuesday</th >
         <th >Wednesday</th >
         <th >Thursday</th >
         <th >Friday</th >
         <th class="weekend" >Saturday</th >
         <th class="weekend" >Sunday</th >
         </tr >
         </thead >
         <tbody >
         '''
    else:
    ## Here we assume a binary switch, a decision between '0' or not '0';
    ## therefore, any non-zero argument will cause the calendar to start
    ## on Sunday.
        print '''
         <table id="month" >
         <thead >
         <tr >
         <th class="weekend" >Sunday</th >
         <th >Monday</th >
         <th >Tuesday</th >
         <th >Wednesday</th >
         <th >Thursday</th >
         <th >Friday</th >
         <th class="weekend" >Saturday</th >
         </tr >
         </thead >
         <tbody >
         '''

    month = calendar.monthcalendar(current_year, current_no)
    nweeks = len(month)

    for w in range(0, nweeks):
        week = month[w]
        print "<tr>"
        for x in xrange(0, 7):
            day = week[x]
            if x == 5 or x == 6:
                classtype = 'weekend'
            else:
                classtype = 'day'

            if day == 0:
                classtype = 'previous'
                print '<td class="%s"></td>' % (classtype)
            elif day == current_day:
                print '''<td class="%s"><strong>%s</strong></span><div class="%s">
                         </div></td>''' % (classtype, day, classtype)
            else:
                print ('''<td class="%s">%s</span><div class="%s"></div></td>''' %
                       (classtype, day, classtype))
        print "</tr>"

    print ''' </tbody>
        </table>
        </div>
        </body>
        </html>'''

if __name__ == "__main__":
    main()

