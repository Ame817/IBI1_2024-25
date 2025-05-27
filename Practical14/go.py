import xml.dom.minidom
import xml.sax
import time

start_time_dom= time.time()

go=xml.dom.minidom.parse('go_obo.xml')

terms=go.getElementsByTagName('term')

biopro={}
molfun={}
cellcom={}
for term in terms:
    namespace=term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    #firstchild.nodevalue:get the text. Otherwise it's gonna get an element
    if namespace=='biological_process':
        id=term.getElementsByTagName('id')[0].firstChild.nodeValue
        name=term.getElementsByTagName('name')[0].firstChild.nodeValue
        is_as=term.getElementsByTagName("is_a")
        biopro[id]=[len(is_as),name]

    if namespace=='molecular_function':
        id=term.getElementsByTagName('id')[0].firstChild.nodeValue
        name=term.getElementsByTagName('name')[0].firstChild.nodeValue
        is_as=term.getElementsByTagName("is_a")
        molfun[id]=[len(is_as),name]

    if namespace=='cellular_component':
        id=term.getElementsByTagName('id')[0].firstChild.nodeValue
        name=term.getElementsByTagName('name')[0].firstChild.nodeValue
        is_as=term.getElementsByTagName("is_a")
        cellcom[id]=[len(is_as),name]                


max_biopro=max(val[0] for val in biopro.values())
max_terms_biopro=[(id,value[1]) for id,value in biopro.items() if value[0]==max_biopro]
max_molfun=max(val[0] for val in molfun.values())
max_terms_molfun=[(id,value[1]) for id,value in molfun.items() if value[0]==max_molfun]
max_cellcom=max(val[0] for val in cellcom.values())
max_terms_cellcom=[(id,value[1]) for id,value in cellcom.items() if value[0]==max_cellcom]

end_time_dom= time.time()

print('DOM:')
print("DOM parsing took:", end_time_dom-start_time_dom, "seconds")
ontologies=['biological_process','molecular_function','cellular_components']
max_list=[max_terms_biopro,max_terms_molfun,max_terms_cellcom]
count_list=[max_biopro,max_molfun,max_cellcom]
for i in range(3):
    print(ontologies[i],':')
    for term_id, name in max_list[i]:
        print('GO ID:', term_id)
        print('name:', name)
    print('is_a count:', count_list[i])


#SAX
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.tag=''
        self.namespace=''
        self.id=''
        self.name=''
        self.isa=0
        self.biopro={}
        self.max_biopro=0
        self.max_id_biopro=''
        self.max_name_biopro=''

        self.cellcom={}
        self.max_cellcom=0
        self.max_id_cellcom=''
        self.max_name_cellcom=''

        self.molfun={}
        self.max_molfun=0
        self.max_id_molfun=''
        self.max_name_molfun=''

    def startElement(self,tag,attr):
        self.tag=tag 
        if tag =='term':
            self.namespace=''
            self.id=''
            self.name=''
            self.isa=0
        elif self.tag=='is_a':
            self.isa+=1

    def characters(self,content):
        if self.tag=='id':
            self.id+=content.strip() #strip:cancel space or /n
        elif self.tag=='name':
            self.name+=content.strip()
        elif self.tag=='namespace':
            self.namespace+=content.strip()


    def endElement(self,tag):
        if tag =='term':
            if self.namespace=='biological_process':
                if self.isa > self.max_biopro:
                    self.biopro={}
                    self.tag=''
                    self.max_biopro=self.isa
                    self.biopro[self.id]=[self.name]
                elif self.isa==self.max_biopro:
                    self.biopro[self.id]=[self.name]

            if self.namespace=='cellular_component':
                if self.isa > self.max_cellcom:
                    self.cellcom={}
                    self.tag=''
                    self.max_cellcom=self.isa
                    self.cellcom[self.id]=[self.name]
                elif self.isa==self.max_cellcom:
                    self.cellcom[self.id]=[self.name]

            if self.namespace=='molecular_function':
                if self.isa > self.max_molfun:
                    self.molfun={}
                    self.tag=''
                    self.max_molfun=self.isa
                    self.molfun[self.id]=[self.name]
                elif self.isa==self.max_molfun:
                    self.molfun[self.id]=[self.name]




start_time_sax= time.time()

parser=xml.sax.make_parser()

handler=GOHandler()
parser.setContentHandler(handler)

parser.parse('go_obo.xml')

IDbp=list(handler.biopro.keys())
IDcc=list(handler.cellcom.keys())
IDmf=list(handler.molfun.keys())

end_time_sax= time.time()
print('\nSAX:')
print("SAX parsing took:", end_time_sax-start_time_sax, "seconds")

ontologies=['biological_process','molecular_function','cellular_components']
count_list=[handler.max_biopro,handler.max_molfun,handler.max_cellcom]
name_list=[list(handler.biopro.values()),list(handler.molfun.values()),list(handler.cellcom.values())]
IDlist=[IDbp,IDmf,IDcc]

for i in range(3):
    print(ontologies[i],':')
    print('ID:',IDlist[i])
    print('name:', name_list[i])
    print('is_a count:', count_list[i])

#SAX parsing took less time 