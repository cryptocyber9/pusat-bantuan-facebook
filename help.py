import mechanize
from bs4 import BeautifulSoup
import requests as r
import argparse

class report:
	def __init__(self):
		self.br=mechanize.Browser()
		self.br.set_handle_robots(False)
		self.br.set_handle_referer(True)
		self.r=r.get
		self.url="https://m.facebook.com/help/contact/283958118330524?ref=u2u"
		self.url2="https://m.facebook.com/help/contact/179049432194862"

	def title(self):
		soup=BeautifulSoup(self.r(self.url).content, "html5lib")
		find_title=soup.find("h3").get_text()
		print(find_title)

	def process(self, email, operator, nope, negara, tambahan):
		self.br.open(self.url)
		self.br._factory.is_html=True
		self.br.select_form(nr=0)
		self.br.form["email"]=email
		self.br.form["textField1"]=operator
		self.br.form["textField2"]=nope
		self.br.form["textField3"]=negara
		self.br.form["customField1"]=["That phone was recently used to verify another account"]
		self.br.form["details"]=tambahan
		soup=BeautifulSoup(self.br.submit().read(), features="html5lib")
		find=soup.find("span", class_="cj").get_text()
		print(find)

	def login_problem(self, email, deskrip, files):
		self.br.open(self.url2)
		self.br._factory.is_html=True
		self.br.select_form(nr=0)
		self.br.form["email"]=email
		self.br.form["Details"]=deskrip
		self.br.set_all_readonly(False)
		self.br.form.add_file(open(files, "rb"))
		soup=BeautifulSoup(self.br.submit().read(), features="html5lib")
		find=soup.find("span", class_="cj").get_text()
		print(find)

main=report()
parser = argparse.ArgumentParser()
parser.add_argument('-l','--login', action="store_true", help='Jika akun kalian mendapatkan masalah login')
parser.add_argument('-v','--verifikasi', action="store_true",help='Jika akun kalian mendapatkan masalah verifikasi')
args = parser.parse_args()
if args.verifikasi:
	try:
		print("")
		main.title()
		email=input("\n[?]Email kamu? ")
		operator=input("[?]Operator?(cth:telkomsel): ")
		nope=str(input("[?]Nomor Hp? "))
		negara=input("[?]Negara? ")
		tambahan=str(input("[?]Info tambahan? "))
	except KeyboardInterrupt:
		exit("\nGoodbye")
	main.process(email,operator,nope,negara,tambahan)
if args.login:
	try:
		email=input("\n[?]Email kamu? ")
		deskrip=input("[?]Deskripsi masalah: ")
		files=str(input("[?]Screenshot masalah akun kamu: "))
	except (FileNotFoundError):
		exit("\nfile tidak ada")
	except	KeyboardInterrupt:
		exit("\ngoodbye")
	main.login_problem(email, deskrip, files)
