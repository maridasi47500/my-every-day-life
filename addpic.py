from country import Country
from urllib.request import Request, urlopen
from chercherimage import Chercherimage
from bs4 import BeautifulSoup
from fichier import Fichier
from pics import Pics
from somescaffold import Scaffold

class Addpic():
      def __init__(self):
            self.paysdb=Country()
            self.picdb=Pics()
            self.URL = "https://www.enchantedlearning.com/wordlist/jobs.shtml"
            self.req = Request(self.URL , headers={'User-Agent': 'Mozilla/5.0'})
            self.webpage = urlopen(self.req).read()
            self.soup = BeautifulSoup(self.webpage, "html.parser")
            self.results = {"rue ville ":"is zer a place u go to more often","solo music player femme homme ":"is zer music u listen to","ecole musique ":"music u play"}
            self.results1 = {"terrain sport ":"sport u practice","soldiers femme homme ":"sports you are watching most often","store next to work ":"store u go to"}
            print(self.results)
      def getbycountryid(self,myid):
            name=None
            pic=None
            country=self.paysdb.getbyid(myid)
            for link in self.results:
                    name=link+" "+country["name"]
                    pic=Chercherimage("woman man "+name).dlpic()["nom"]
                    self.picdb.create({"country_id": country["id"],"name":name,"pic":pic})
                    if "place u go" in self.results[link]:
                        Scaffold("placego",["name","user_id"]).wrotetofile()
                        Fichier("./","addplacego.py").ecrire("""import sys\nfrom placego import Placego\nPlacego().addnewplacego(sys.argv[2])\n""")
                    elif "music u listen" in self.results[link]:
                        Scaffold("musiclisten",["name","user_id"]).wrotetofile()
                        Fichier("./","addmusiclisten.py").ecrire("""import sys\nfrom musiclisten import Musiclisten\nMusiclisten().addnewmusiclisten(sys.argv[2])\n""")
                    elif "music u play" in self.results[link]:
                        Scaffold("musicplay",["name","user_id"]).wrotetofile()
                        Fichier("./","addmusicplay.py").ecrire("""import sys\nfrom musicplay import Musicplay\nMusicplay().addnewmusicplay(sys.argv[2])\n""")
            for link in self.results1:
                    name=link+" "+country["name"]
                    pic=Chercherimage("woman man "+name).dlpic()["nom"]
                    self.picdb.create({"country_id": country["id"],"name":name,"pic":pic})
            return ""
      def getallcountry(self):
            name=None
            pic=None
            for country in self.paysdb.getall():
                 for link in self.results:
                         name=link+" "+country["name"]
                         pic=Chercherimage("woman man "+name).dlpic()["nom"]
                         self.picdb.create({"country_id": country["id"],"name":name,"pic":pic})
                 for link in self.results1:
                         name=link+" "+country["name"]
                         pic=Chercherimage("woman man "+name).dlpic()["nom"]
                         self.picdb.create({"country_id": country["id"],"name":name,"pic":pic})
