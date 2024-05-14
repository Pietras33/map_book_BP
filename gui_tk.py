from tkinter import *


root= Tk()
root.geometry('800x700')
root.title('MapBook')


ramka_lista_uzytkownikow =Frame(root)
ramka_formlularz= Frame(root)
ramka_szczegolyobiektu= Frame(root)

ramka_lista_uzytkownikow.grid(row=0, column=0)
ramka_formlularz.grid(row=0, column=1)
ramka_szczegolyobiektu.grid(row=1, column=0)
# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_uzytkownikow, text='Lista znajomych')
listbox_lista_obiektow=Listbox(ramka_lista_uzytkownikow)
button_pokaz_szczegoly=Button(ramka_lista_uzytkownikow, text='Pokaz szczegoly')
button_usun_uzytkownika=Button(ramka_lista_uzytkownikow, text="usun")
button_edytuj_uzytkownika=Button(ramka_lista_uzytkownikow, text="edytuj")

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_uzytkownika.grid(row=2, column=1)
button_edytuj_uzytkownika.grid(row=2, column=2)


label_formularz=Label(ramka_formlularz, text="formularz edycji")
label_formularz.grid(row=0, column=0, columnspan=3)



root.mainloop()


