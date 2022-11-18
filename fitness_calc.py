from tkinter import *
# default GUI class for the calculator
class FitnessCalculator:
    def __init__(self):
        calculator=Tk()
        calculator.title('Fitness Calculator')
        calculator.resizable(0,0)
        #main label
        Label(calculator,text='Fitness',bg='black',fg='white',width=30).grid(row=0,column=1,ipadx=5)

        #name and age entry fields
        name=StringVar()
        age=IntVar()
        Label(calculator,text='Name: ',width=10).grid(row=1,column=1)
        Entry(calculator,width=25,relief='ridge',bd=2,textvariable=name).grid(row=1,column=2)
        Label(calculator,text='Age : ',width=10).grid(row=1,column=3)
        Entry(calculator,width=25,relief='ridge',bd=2,textvariable=age).grid(row=1,column=4)

        #The Gender Radio Button

        v=IntVar()
        Label(calculator,text='Gender : ').grid(row=2,column=1)
        Radiobutton(calculator,text='Male',variable=v,value=1).grid(row=2,column=2,padx=30)
        Radiobutton(calculator,text='Female',variable=v,value=2).grid(row=2,column=4,padx=100)

        #Generating the fields for Entry Fields

        fields=('Weight (Kg)','Height (Mts)','BP Low (Systolic) mm/Hg','BP High (Diastolic) mm/Hg','Pulse Rate','RBC Count (trillion Cells/L)','WBC Count (billions cells/L)','Platelets','HB','Uric Acid (mg/dL)','Cholestrol (mg/dL)')
        r=3
        entries=[]
        for field in fields:
            Label(calculator,text=field+' : ',width=30,bg='grey',fg='white').grid(row=r,column=1,sticky='NWSWSE')
            en=Entry(calculator,width=30,relief='ridge',bd=2)
            en.grid(row=r,column=2,sticky='NWSWSE')
            entries.append(en)
            r+=1
         #Report Label
        Label(calculator,text='Report Of',width=30,bg='black',fg='white').grid(row=14,column=1,sticky='NWSWSE') 
        Label(calculator,text='BMI (High/Medium/Low)',width=30,fg='black',bg='gainsboro',textvariable=name).grid(row=14,column=2,sticky='NWSWSE') 
    
        #Results TextVariables
        bmi_calculated=StringVar()
        bp_calc=StringVar()
        pulse_calulated=StringVar()
        cholestrol_calculated=StringVar()
        wbc_final=StringVar()
        rbc_final=StringVar()
        platelets_final=StringVar()
        uric_acid=StringVar()
        haemoglobin_calc=StringVar()

         #Final_Labels
        Label(calculator,text='BMI (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=15,column=1,sticky='NWSWSE')
        Label(calculator,text='BP (Normal/High)',width=30,bg='grey',fg='white').grid(row=16,column=1,sticky='NWSWSE')
        Label(calculator,text='Pulse Rate (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=17,column=1,sticky='NWSWSE')
        Label(calculator,text='RBC Count (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=18,column=1,sticky='NWSWSE')
        Label(calculator,text='WBC Count (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=19,column=1,sticky='NWSWSE')
        Label(calculator,text='Platelets (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=20,column=1,sticky='NWSWSE')
        Label(calculator,text='HB (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=21,column=1,sticky='NWSWSE')
        Label(calculator,text='Uric Acid (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=22,column=1,sticky='NWSWSE')
        Label(calculator,text='Cholestrol (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=23,column=1,sticky='NWSWSE')

        Label(calculator,text='BMI (High/Medium/Low)',width=30,fg='black',bg='gainsboro',textvariable=bmi_calculated).grid(row=15,column=2,sticky='NWSWSE')
        Label(calculator,text='BP (High/Normal)',width=30,fg='black',bg='gainsboro',textvariable=bp_calc).grid(row=16,column=2,sticky='NWSWSE')
        Label(calculator,text='Pulse Rate (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=pulse_calulated).grid(row=17,column=2,sticky='NWSWSE')
        Label(calculator,text='RBC Count (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=rbc_final).grid(row=18,column=2,sticky='NWSWSE')
        Label(calculator,text='WBC Count (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=wbc_final).grid(row=19,column=2,sticky='NWSWSE')
        Label(calculator,text='Platelets (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=platelets_final).grid(row=20,column=2,sticky='NWSWSE')
        Label(calculator,text='HB (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=haemoglobin_calc).grid(row=21,column=2,sticky='NWSWSE')
        Label(calculator,text='Uric Acid (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=uric_acid).grid(row=22,column=2,sticky='NWSWSE')
        Label(calculator,text='Cholestrol (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=cholestrol_calculated).grid(row=23,column=2,sticky='NWSWSE')

        #making the bottom Label
        Label(calculator,bg='black',fg='white',width=30).grid(row=25,column=1,ipadx=5)       
        def get_entries():
            print(name.get())
            print(age.get())
            for entry in entries:
                print(entry.get())

         #BMI calculator
        def calculate_bmi():
            weight=float(entries[0].get())
            height=float(entries[1].get())
            bmi=(weight/height)/height
            if bmi < 15:
                value='Low'
            elif bmi >15 and bmi<20:
                value='Medium'
            else:
                value='High'
            bmi_calculated.set(value)

         #BP monitor
        def blood_pressure():
            bpl=int(entries[2].get())
            bph=int(entries[3].get())
            if bpl<120 and bph <80:
                value='Normal'
            elif bph >=140 and bph >=90:
                value='High'
            bp_calc.set(value) 

         #Pulse Monitor
        def pulse_rate():
            pulse=int(entries[4].get())
            if pulse <72:
                value='Low'
            elif pulse >72 and pulse <90:
                value='Medium'
            elif pulse > 90:
                value='High'
            pulse_calulated.set(value)

        #urine Monitor
        def urine_monitor():
            urine=float(entries[9].get())
            if urine > 4 and urine <8.5:
                value='Medium'
            elif urine <4:
                value='Low'
            elif urine > 8.5:
                value='High'
            uric_acid.set(value)

         #get Cholestrol
        def get_cholestrol():
            cholestrol=float(entries[10].get())
            if cholestrol <200:
                value='Low (Good)'
            elif cholestrol >200 and cholestrol<239:
                value='Medium'
            elif cholestrol>240:
                value='High'
            cholestrol_calculated.set(value)
        
        # calculating rbc levels 
        def rbc():
            rbc=float(entries[5].get())
            if rbc > 4.32 and rbc < 5.72:
                r_value='Medium'
            elif rbc < 4.32:
                r_value='Low'
            elif rbc>5.72:
                r_value='High'
            rbc_final.set(r_value)
        #calculating wbc values 
        def wbc_k():
            wbc=float(entries[6].get())
            if wbc >3 and wbc<10:
                w_value='Medium'
            elif wbc<3:
                w_value='Low'
            elif wbc>10:
                w_value='High'
            wbc_final.set(w_value)

         #calculating platelets levels 

        def platelet():
            platelets=float(entries[7].get())
            if platelets >150 and platelets <450:
               p_value='Medium'
            elif platelets<150:
                p_value='Low'
            elif platelets>450:
                p_value='High'
            platelets_final.set(p_value)

        #calculating Haemoglobin Levels
        def haemo():
            haemoglobin=float(entries[8].get())
            if haemoglobin >13 and haemoglobin <16:
                h_value='Medium'
            elif haemoglobin >16:
                h_value='High'
            elif haemoglobin <13:
                h_value='Low'
            haemoglobin_calc.set(h_value) 






        def show_results():
            name.set(name.get())
            get_entries()
            calculate_bmi()
            blood_pressure()
            pulse_rate()
            rbc()
            wbc_k()
            haemo()
            urine_monitor()
            get_cholestrol()
            platelet()

        #Button to Show the results of the report 
        Button(calculator,text="Show Report",relief='ridge',bg='grey',fg='white',bd=2,command=show_results).grid(row=14,column=4,ipadx=4)

        # Initiating the GUI mainloop Instance (event loop)
        calculator.mainloop()

#calling the default constructor to create the GUI
FitnessCalculator()
