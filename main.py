from guizero import App,Box,TextBox, PushButton, ListBox, Text, Picture, Drawing, TextBox, Window

store = []
list_names = []
temp = None
patient = None
x = None


def menu():
    global store

    def edit():

        def save():
            global store, list_names, temp, patient


            temps = temp.value

            float_temps = float(temps)
            if float_temps > 37.5 or float_temps < 36:
                patient.info("Warning", "Iregular temperature, temperature falls out within the range of  36.0°C to 37.5°C.")


            int_temps = float(temps)
            item["temperature"].append(int_temps)
            item["current_temperature"] = int_temps

            print(item["temperature"])


            """""
            list_names.append(names)

            store.append(item)
            list.clear()
            print(store)
            for x in list_names:
                list.append(x)
            """







        def patient_i():
            global temp, store, patient

            patient = Window(app, title = "patient")
            patient.bg = "white"
            patient.show(wait=True)

            header_pt = Box(patient, width="1000", height=100, layout="grid")
            header_pt.bg = "White"
            name_label_pt = Text(header_pt, text="patient", grid=[2,0], font="Dosis", size=35)
            picture_pt = Picture(header_pt, image="chuvr.gif", grid=[1,0], width=200, height=100)
            mover_pt = Box(header_pt, width=30, height=80, grid=[3,0])
            back_pt = Picture(header_pt, image="back.gif", grid=[4,0], width=50, height=40)
            line_pt = Box(patient, width=1000, height=5)
            line_pt.bg = "#62bbc1"

            back_pt.when_clicked = patient.destroy

            main_pt = Box(patient, layout="grid", align="right")
            main_pt.bg = "White"


            n = item["baby_name"]
            d = item["date_of_birth"]
            t = item["temperature"]
            tt = item["current_temperature"]
            photo = item["photo"]


            max_temp = max(t)
            print(max_temp)

            min_temp = min(t)
            print(min_temp)

            dif_temp = max_temp - min_temp



            name_pt = TextBox(main_pt, grid=[3,0], width=21, align = "top", text="name: " + str(n) )
            date_of_birth_pt = TextBox(main_pt, grid=[3,1], align = "top", width=21, text="Date of birth: " + str(d) )
            temp_pt = TextBox(main_pt, grid=[3,2], align = "top", width=21, text="Past temps : " + str(t) )
            cur_pt = TextBox(main_pt, grid=[3,3], align = "top", width=21, text="current temp : " + str(tt) )
            crz_pt = TextBox(main_pt, grid=[3,4], align = "top", width=21, text="Max temp: " + str(max_temp))
            rrz_pt = TextBox(main_pt, grid=[3,5], align = "top", width=21, text="Min temp: " + str(min_temp))
            rz_pt = TextBox(main_pt, grid=[3,6], align = "top", width=21, text="Temp dif: " + str(dif_temp))
            temp = TextBox(main_pt, grid=[3,7], align = "top", width=21)

            button = PushButton(main_pt, text="Add patient", command=save, grid=[3,8])





            photo_pt = Box(patient, width=210, height=400, align="left")
            add_photo = Picture(photo_pt, image=photo, height=350, width=200)
            photo_pt.bg = "white"







        global store, list_names


        baby_name = list.value

        for item in store:
            search = item["baby_name"]
            if search == baby_name:
                print("found")
                patient_i()

        print(baby_name)



    def add_patient():

        def add_image():
            global x

            add_patient.hide()

            user_image=(app.select_file(title="Select file", folder=".", filetypes=[["All files", "*.*"]], save=False, filename=""))

            x = user_image

            add_patient.show()

            add_pat.image = user_image

        def save():
            global store, list_names, x


            names = name.value
            date = date_of_birth.value
            temps = temp.value

            float_temps = float(temps)
            if float_temps > 37.5 or float_temps < 36:
                add_patient.info("Warning", "Iregular temperature, temperature falls out within the range of  36.0°C to 37.5°C.")



            item = {}



            cool_temps = float(temps)


            item["temperature"] = []

            item["baby_name"] = names
            item["date_of_birth"] = date
            item["temperature"].append(cool_temps)
            item["current_temperature"] = cool_temps
            item["photo"] = x

            list_names.append(names)

            store.append(item)
            list.clear()
            print(store)
            for x in list_names:
                list.append(x)


        add_patient = Window(app, title = "SECOND WINDOW")
        add_patient.show(wait=True)

        header_pat = Box(add_patient, width="1000", height=100, layout="grid")
        header_pat.bg = "White"
        name_label_pat = Text(header_pat, text="Add patient", grid=[2,0], font="Dosis", size=35)
        picture_pat = Picture(header_pat, image="chuvr.gif", grid=[1,0], width=200, height=100)
        mover_pat = Box(header_pat, width=30, height=80, grid=[3,0])
        back_pat = Picture(header_pat, image="back.gif", grid=[4,0], width=50, height=40)
        line_pat = Box(add_patient, width=1000, height=5)
        line_pat.bg = "#62bbc1"

        back_pat.when_clicked = add_patient.destroy

        main_pat = Box(add_patient, width=1000, height=400, layout="grid")
        main_pat.bg = "white"


        add_pat = Picture(main_pat, image="Add_photo.gif", height=350, width=200, grid=[1,0,1,3] )
        add_pat.when_clicked = add_image




        name_text = Text(main_pat, text="Name: ", grid=[3,0], font="Dosis", size=15, align = "left")
        birth_text = Text(main_pat, text="Date of Birth", grid=[3,1], font="Dosis", size=15, align = "left")
        temp_text = Text(main_pat, text="Temperature ", grid=[3,2], font="Dosis", size=15, align = "left")

        name = TextBox(main_pat, grid=[4,0], width=21, align = "left")
        date_of_birth = TextBox(main_pat, grid=[4,1], width=21, align = "left")
        temp = TextBox(main_pat, grid=[4,2], width=21, align = "left")

        button = PushButton(main_pat, text="Add patient", command=save, grid=[4,3], align = "top")



        #app.hide()

    def instructons():
            instruction = Window(app, title = "Instructions")
            instruction.show(wait=True)
            instruction.bg = "white"

            header_inst = Box(instruction, width="1000", height=100, layout="grid")
            header_inst.bg = "White"
            name_label_inst = Text(header_inst, text="Instructions", grid=[2,0], font="Dosis", size=35)
            picture_inst = Picture(header_inst, image="chuvr.gif", grid=[1,0], width=200, height=100)
            mover_inst = Box(header_inst, width=30, height=80, grid=[3,0])
            back_inst = Picture(header_inst, image="back.gif", grid=[4,0], width=50, height=40)
            line_inst = Box(instruction, width=1000, height=5)
            line_inst.bg = "#62bbc1"

            app.show()
            back_inst.when_clicked = instruction.destroy



            main_inst = Box(instruction, width=1000, height=400)
            main_inst.bg = "white"
            name = Text(main_inst, text="", font="Dosis", size=15)
            name1 = Text(main_inst, text="1) Turn on the thermomture.", font="Dosis", size=25)
            name2 = Text(main_inst, text="2) insert thermometure into babys rectum ", font="Dosis", size=25)
            name3 = Text(main_inst, text="3) remove thermoeture once it beeps ", font="Dosis", size=25)
            name4 = Text(main_inst, text="4) click on add patient, ", font="Dosis", size=25)
            name45 = Text(main_inst, text="or if its an existing click on the patients name", font="Dosis", size=25)
            name5 = Text(main_inst, text="5) enter patients informtation", font="Dosis", size=25)
            name6 = Text(main_inst, text="6) click save information/or add patient", font="Dosis", size=25)








    app = App(width="600")

    header = Box(app, width="1000", height=100, layout="grid")
    header.bg = "White"
    name_label = Text(header, text="BABY TEMPERATURE", grid=[2,0], font="Dosis", size=35)
    picture = Picture(header, image="chuvr.gif", grid=[1,0], width=200, height=100)
    line = Box(app, width=1000, height=5)
    line.bg = "#62bbc1"

    main = Box(app, width=1000, height=1000, layout="grid")
    main.bg = "White"

    mover = Box(main, width=30, height=80, grid=[0,0])
    mover2 = Box(main, width=40, height=90, grid=[2,0])
    mover3 = Box(main, width=200, height=90, grid=[3,0], align="top")
    #mover.bg = "blue"
    #mover2.bg = "blue"
    #mover3.bg = "blue"
    list = ListBox(main, items=store, scrollbar=True, grid=[1,1], command=edit)
    text = TextBox(main, grid=[1,0], align="bottom", width=21)

    button = Picture(main, image="button1.gif", grid=[3,1], width=260, height=75, align="top")
    button1 = Picture(main, image="button2.gif", grid=[3,2], width=260, height=70)

    button.when_clicked = instructons
    button1.when_clicked = add_patient

    app.display()









menu()

