import pandas as pd
import matplotlib.pyplot as plt
import os

def listConvert(ls,whc):
    for z in ls:
        if whc==1:  #int
            a=int(z)
        elif whc==2:    #float
            a=float(z)
    return a

def searchData(sno,sgpa,df):
    userInfo={
        "exam_no":0,
        "name":"NA",
        "sgpa":0,
        "credits":0,
    }

    if(sno<10):
        sno="0"+str(sno)
    seatno="T1502942"+str(sno)

    mydata=df.loc[df['exam_no'] == seatno]

    name=mydata['name'].tolist()
    credits=mydata['credits'].tolist()

    userInfo['exam_no']=seatno
    userInfo['name']=name
    userInfo['sgpa']=sgpa
    userInfo['credits']=credits

    return userInfo


df=pd.read_csv('sgpa_data.csv')
sgpaAll=df['sgpa'].tolist()


xs=[]
for x in range(1,len(df)+1):
    xs.append(x)

mappedvals=dict(zip(xs,sgpaAll))
th=7.76 # threshold

# x and y values for ATKT
xs_atkt=[]
ys_atkt=[]

# x and y values above threshold
xs_ath=[]
ys_ath=[]

# x and y values below threshold
xs_bth=[]
ys_bth=[]

for z in range(1,len(df)+1):
    if mappedvals[z]==0:
        xs_atkt.append(z)
        ys_atkt.append(mappedvals[z])
    elif mappedvals[z]<th:
        xs_bth.append(z)
        ys_bth.append(mappedvals[z])
    else:
        xs_ath.append(z)
        ys_ath.append(mappedvals[z])

# ------------GRAPH-----------------------

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title('Results of passed students')

line1 = ax.plot(xs_ath,ys_ath, 'bo', picker=5, label="sgpa > "+str(th))  # 5 points tolerance
line2 = ax.plot(xs_bth,ys_bth, 'yo', picker=5, label="sgpa < "+str(th))
# line3 = ax.plot(xs_atkt,ys_atkt, 'ro', picker=5)  # ATKT STUDENTS DATA

def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind

    seatno=listConvert(xdata[ind].tolist(),1)
    sgpa=listConvert(ydata[ind].tolist(),2)

    os.system('cls')

    mydata=searchData(seatno,sgpa,df)
    print(mydata)

fig.canvas.mpl_connect('pick_event', onpick)

plt.legend()
plt.show()
