import os
def Get_Files_Name(path=""):
	"""path:had message found path   """
	t=[]
	path=path.replace("\\","/")
	for dirpath,dirnames,filenames in os.walk(path):
		t+=[[str(dirpath).replace("\\",'/') , str(dirnames).replace('\\','/') , str(filenames).replace('\\','/')]]
	return t
	
def Var_List_to_Bytes(keylist=[],change_code="utf-8"):
	"""keylist: var list
	change_code: changed to code ,such as utf-8   """
	rlist=[]
	for i in keylist:
		rlist+=i.encode(change_code)
	return rlist

if __name__=="__main__":
	pass