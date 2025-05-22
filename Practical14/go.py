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
        is_as=term.getElementsByTagName("is_a")
        biopro[id]=len(is_as)

    if namespace=='molecular_function':
        id=term.getElementsByTagName('id')[0].firstChild.nodeValue
        is_as=term.getElementsByTagName("is_a")
        molfun[id]=len(is_as)

    if namespace=='cellular_component':
        id=term.getElementsByTagName('id')[0].firstChild.nodeValue
        is_as=term.getElementsByTagName("is_a")
        cellcom[id]=len(is_as)                


max_biopro=max(biopro,key=biopro.get)
max_molfun=max(molfun,key=molfun.get)
max_cellcom=max(cellcom,key=cellcom.get)

end_time_dom= time.time()

print("DOM parsing took:", end_time_dom-start_time_dom, "seconds")
print('The term of biological process with the greatest number of <is_a> elements:',max_biopro,',',biopro[max_biopro])
print('The term of molecular function with the greatest number of <is_a> elements:',max_molfun,',',molfun[max_molfun])
print('The term of cellular component with the greatest number of <is_a> elements:',max_cellcom,',',cellcom[max_cellcom])


class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.tag=''
        self.namespace=''
        self.id=''
        self.isa=0
        self.max_biopro=0
        self.max_id_biopro=''
        self.max_cellcom=0
        self.max_id_cellcom=''
        self.max_molfun=0
        self.max_id_molfun=''

    def startElement(self,tag,attr):
        self.tag=tag 
        if tag =='term':
            self.namespace=''
            self.id=''
            self.isa=0
        elif self.tag=='is_a':
            self.isa+=1

    def characters(self,content):
        if self.tag=='id':
            self.id+=content.strip() #strip:cancel space or /n
        elif self.tag=='namespace':
            self.namespace+=content.strip()


    def endElement(self,tag):
        if tag =='term':
            if self.namespace=='biological_process':
                if self.isa > self.max_biopro:
                    self.max_biopro=self.isa
                    self.max_id_biopro=self.id
                    self.tag=''
            if self.namespace=='molecular_function':
                if self.isa > self.max_molfun:
                    self.max_molfun=self.isa
                    self.max_id_molfun=self.id
                    self.tag=''
            if self.namespace=='cellular_component':
                if self.isa > self.max_cellcom:
                    self.max_cellcom=self.isa
                    self.max_id_cellcom=self.id
                    self.tag=''

start_time_sax= time.time()

parser=xml.sax.make_parser()

handler=GOHandler()
parser.setContentHandler(handler)

parser.parse('go_obo.xml')

end_time_sax= time.time()

print("\nSAX parsing took:", end_time_sax-start_time_sax,"seconds")

print('The term in biological process with the greatest number of <is_a> is',handler.max_id_biopro)
print('It has',handler.max_biopro,'<is_a>s.')

print('The term in molecular function with the greatest number of <is_a> is',handler.max_id_molfun)
print('It has',handler.max_molfun,'<is_a>s.')

print('The term in cellular component with the greatest number of <is_a> is',handler.max_id_cellcom)
print('It has',handler.max_cellcom,'<is_a>s.')
