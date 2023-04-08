from tkinter import *
import numpy as np

#constants
pi = np.pi
i = complex(0,1)
DEG2RAD = pi/180

L2D = lambda R1,R2,alpha: -R1*np.cos(alpha) + np.sqrt((R1*np.cos(alpha))**2-R1**2+R2**2)
spoke_len = lambda R1,R2,alpha,Coff: np.sqrt(L2D(R1,R2,alpha)**2+Coff**2)

def spoke_length(**kwargs):
    alpha = float(kwargs['alpha'])*DEG2RAD
    R2 = float(kwargs['ERD'])/2
    R1 = float(kwargs['PCD'])/2
    Coff = float(kwargs['FTF'])/2 + float(kwargs['offset'])
    kwargs['resultField'].set(str(round( spoke_len(R1,R2,alpha,Coff) ,2)))
    return None

#blank window
root = Tk()
root.title('spoke lenght calculator')

###
frame1 = Frame(root)
frame1.grid()

crow = 0
ERDLabel = Label(frame1, text='ERD')
ERDVal = Entry(frame1,width=5)
EUnits = Label(frame1, text='mm')
ERDLabel.grid(row=crow,column=0, sticky=W)
ERDVal.grid(row=crow,column=1, sticky=E)
EUnits.grid(row=crow,column=2, sticky=E)
#ERDVal.get()

crow +=1
PCDLabel = Label(frame1, text='PCD')
PCDVal = Entry(frame1,width=5)
PUnits = Label(frame1, text='mm')
PCDLabel.grid(row=crow,column=0, sticky=W)
PCDVal.grid(row=crow,column=1, sticky=E)
PUnits.grid(row=crow,column=2, sticky=E)
#PCDVal.get()

crow +=1
FTFLabel = Label(frame1, text='FTF')
FTFVal = Entry(frame1,width=5)
FUnits = Label(frame1, text='mm')
FTFLabel.grid(row=crow,column=0, sticky=W)
FTFVal.grid(row=crow,column=1, sticky=E)
FUnits.grid(row=crow,column=2, sticky=E)
#FTFVal.get()

crow +=1
offsetLabel = Label(frame1, text='offset')
offsetVal = Entry(frame1,width=5)
offsUnits = Label(frame1, text='mm')
offsetLabel.grid(row=crow,column=0, sticky=W)
offsetVal.grid(row=crow,column=1, sticky=E)
offsUnits.grid(row=crow,column=2, sticky=E)
#offsetVal.get()

crow +=1
alphaLabel = Label(frame1, text='alpha')
alphaVal = Entry(frame1,width=5)
alpUnits = Label(frame1, text='mm')
alphaLabel.grid(row=crow,column=0, sticky=W)
alphaVal.grid(row=crow,column=1, sticky=E)
alpUnits.grid(row=crow,column=2, sticky=E)
#alphaVal.get()

crow +=1
submit_row = crow

###
frame2 = Frame(root)
frame2.grid()

crow +=1
resultLabel = Label(frame2, text='spoke length')
SpokeLength = StringVar()
resultField = Label(frame2, textvariable=SpokeLength, width=5)
resultUnits = Label(frame2, text='mm')
resultLabel.grid(row=crow,column=0, sticky=W)
resultField.grid(row=crow,column=1, sticky=E)
resultUnits.grid(row=crow,column=2, sticky=E)


submit = Button(frame1, text='calculate', command = 
	lambda: spoke_length(ERD=ERDVal.get(),PCD=PCDVal.get(),alpha=alphaVal.get(),FTF=FTFVal.get(),offset=offsetVal.get(),resultField=SpokeLength))
submit.grid(row=submit_row,columnspan=5)

#keep window open
root.mainloop()