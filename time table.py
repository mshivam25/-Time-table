import datetime
now = datetime.datetime.now()
today=now.strftime("%A")
print(today)


Monday={"AMB":["08:29","09:28"],"BEDE":["09:29","10:28"],"BMS":["10:29","11:28"],"PE":["11:29","12:28"],"LUNCH":["12:29","13:28"],"BIL":["13:29","15:30"]}
Tuesday={"OE":["08:29","09:28"],"AMB":["09:29","10:28"],"PE":["10:29","11:28"],"BI":["11:29","12:28"],"LUNCH":["12:29","13:28"],"BIL":["13:29","15:30"]}
Wednesday={"BI":["08:29","09:28"],"OE":["09:29","10:28"],"BEDE":["10:29","11:28"],"AMB":["11:29","12:28"],"LUNCH":["12:29","13:28"],"BWTL":["13:29","15:30"]}
Thursday={"BMS":["08:29","09:28"],"BI":["09:29","10:28"],"OE":["10:29","11:28"],"BEDE":["11:29","12:28"],"LUNCH":["12:29","13:28"],"BWTL":["13:29","15:30"]}
Friday={"FREE":["08:29","09:28"],"BMS":["09:29","10:28"],"BI":["10:29","11:28"],"PE":["11:29","12:28"],"LUNCH":["12:29","13:28"],"MINOR_PROJECT":["13:29","15:30"]}

meet_link={"AMB":"https://www.youtube.com/watch?v=4hoiwi3tE6w&ab_channel=DharmaProductions",
"BEDE":"meet.google.com/iht-oaih-cmv",
"BMS":"meet.google.com/vhe-djbn-guu",
"PE":"meet.google.com/ade-hres-tas",
"OE":"https://www.youtube.com/watch?v=4hoiwi3tE6w&ab_channel=DharmaProductions",
"BI":"https://www.youtube.com/watch?v=4hoiwi3tE6w&ab_channel=DharmaProductions",
"BIL":"meet.google.com/jgk-ofpk-meb",
"BWTL":"meet.google.com/xvf-kudt-fqo",
"MINOR_PROJECT":"https://www.youtube.com/watch?v=4hoiwi3tE6w&ab_channel=DharmaProductions",
"LUNCH":"https://www.youtube.com/watch?v=HC3-gSNbx00&ab_channel=RecordMill",
"FREE":"https://www.youtube.com/watch?v=4hoiwi3tE6w&ab_channel=DharmaProductions"
}
import datetime
now = datetime.datetime.now()
early_morning=now.replace(hour=8, minute=27)
evening=now.replace(hour=15, minute=31)
for key ,value  in (eval(today)).items():

    my_time_string1 = value[0]
    my_time_string2 = value[1]

    my_datetime1 = datetime.datetime.strptime(my_time_string1, "%H:%M")
    my_datetime2 = datetime.datetime.strptime(my_time_string2, "%H:%M")

    #converting time type for comparison
    my_datetime1 = now.replace(hour=my_datetime1.time().hour, minute=my_datetime1.time().minute)
    my_datetime2 = now.replace(hour=my_datetime2.time().hour, minute=my_datetime2.time().minute)


    if now>my_datetime1 and now<my_datetime2:
        url=(meet_link[key])
        # Open google in python - Windows.
        import webbrowser
        url = (meet_link[key])
        webbrowser.open(url)
if now<early_morning :
        import webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=A4WW9ezwazc&ab_channel=VidhiSharma")
if now>evening :
        import webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=iFLPKjReU20&ab_channel=SMCreations")








