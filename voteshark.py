from selenium import webdriver
from tkinter import *
import sys, os

window = Tk()
window.geometry("700x300")
window.title("VoteShark Wildx3West")
ln = StringVar()
var = StringVar()
var.set("Selecteaza, man")

def getName():
    numar = ln.get()
    litera = options[var.get()]
    ##########################################################################

    def program(numar, litera):
        for i in range(int(numar)):
            if getattr(sys, 'frozen', False):
                # executed as a bundled exe, the driver is in the extracted folder
                chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
                driver = webdriver.Chrome(chromedriver_path)
            else:
                # executed as a simple script, the driver should be in `PATH`
                driver = webdriver.Chrome()

            #driver = webdriver.Chrome("C:\\chromedriver.exe")
            driver.get("https://www.browserling.com/tools/random-ip")
            numarip = driver.find_element_by_id("random-ip-how-many")
            numarip.clear()
            numarip.send_keys(1)
            butoip = driver.find_element_by_id("random-ip-submit")
            butoip.click()
            textarea = driver.find_element_by_id('random-ip-text')
            adresaip = textarea.get_attribute("value")
            driver.quit()

            if getattr(sys, 'frozen', False):
                # executed as a bundled exe, the driver is in the extracted folder
                chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
                driver = webdriver.Chrome(chromedriver_path)
            else:
                # executed as a simple script, the driver should be in `PATH`
                driver = webdriver.Chrome()

            #driver = webdriver.Chrome("C:\\chromedriver.exe")
            driver.get("https://docs.google.com/forms/d/e/1FAIpQLScRQVZ6asnBtfBTLghGlOLZqNVED55APEz9Jf6xlH9ordQ2kQ/viewform")
            buton = driver.find_element_by_xpath("//div[@data-value='{}']".format(litera))
            buton.click()
            ip = driver.find_element_by_xpath("//textarea[@jsname='YPqjbf']")
            ip.send_keys(adresaip)
            trimitere = driver.find_element_by_xpath("//div[@role='button']")
            trimitere.click()
            driver.quit()

    ############################################################################
    program(numar, litera)




titlu = Label(window, text = "Vrei sa castigi balul? ;)",  font = ("impact", 14)).place(x = 260, y = 20)
label = Label(window, text = "a Magy production", font = ("verdana", 5, "bold")).place(x = 0, y = 0)
label1 = Label(window, text = "Introdu numele concurentului", font = ("verdana", 10)).place(x = 120, y = 90)
label2 = Label(window, text = "Introdu numarul de voturi dorit", font = ("verdana", 10)).place(x = 120, y = 140)
text2 = Entry(window, textvar = ln).place(x = 380, y = 143)
label3 = Label(window, text = "* In functie de cat imi dai de lucru, va dura mai mult sau mai putin. So sit down and have a biscuit while I do the hard work...", font = ("verdana", 7)).place(x = 20, y = 270)
buttonApp = Button(window, text = "Hai cu voturile!", relief = "solid", bg = "brown", fg = "white", font = ("verdana", 9), command = getName).place(x = 300, y = 200)
options = {"Name1" : 'a', "Name2" : 'b', "Name3" : 'c', "Name4" : 'd', "Name5" : 'e', "Name6" : 'f', "Name7" : 'g',
    "Name8" : 'A', "Name9" : 'B', "Name10" : 'C', "Name11" : 'D', "Name12" : 'E', "Name13" : 'F', "Name14" : 'G'}
dropdown = OptionMenu(window, var, *options.keys())
dropdown.place(x = 375, y = 88)
dropdown.config(width = 20)

window.mainloop()
