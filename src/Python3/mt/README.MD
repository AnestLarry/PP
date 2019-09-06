# My Tool
<hr>
## Listlib

### 1.List_Sort_Same(klist=[],r=True)
#### Sort the list

### 2.List_to_Str(keylist=[],mode=0)
#### (["56",56,65,65],0)  -->  56566565
#### (["56",56,65,65],1)  -->  56\n56\n65\n65\n

<hr>

## Threadinglib

### 1.Multithreading_Run(function=[],functionkey=[])
#### ([print,print],["123","321"]) --> 123\n321

### 2.Delay_Threading_To_Exit(subthreadinglist=[],Delaytime=0,tips=False)
#### Delaytime is a number of seconds,tips when it finished

### 3.Check_Threading_isalive(subthreadinglist=[])
#### return a list which has "True" or "False"

<hr>

## Filelib
### 1.Get_Files_Name(path="")
#### return full path list

## 2.Var_List_to_Bytes(keylist=[],change_code="utf-8")
### encode elements to bytes

<hr>

## url_lib
### Class url_lib
#### ub=url_lib.url_lib()

#### 1.Get([['key','value']],url=None)   --> return Page from Get

#### 2.Post(self,data={"keyname":"keyword",},url=None)   --> return Page File from Post

#### 3.Add_header(self,key=("key","value"))  --> Add one header

#### 4.Del_header(self,key=[])  --> Delete one header

<hr>

## timelib
### 1.Showtime(key="$ + year/mon/f_mon/week/day/f_day/hour/min/sec/time/apm/b_time")
#### ("$year-$mon-$day")  -->  "2018-07-24"

### 2.Timelog(func)
<textarea cols=30 rows=3>@timelib.Timelog
def test():
    print("temp")</textarea>

#### result:

<textarea cols=50 rows=7>function name: test  --time: 2018-07-24 20:00:43
--------------------------------------------------
temp

--------------------------------------------------
function name: test  --time: 2018-07-24 20:00:43
Cost time: 0.0029990673065185547</textarea>

### 3.Simple_timelog(func)
<textarea cols=30 rows=3>@timelib.Simple_timelog
def test():
    print("temp")</textarea>

#### result:

<textarea cols=50 rows=2>temp
0.023983001708984375</textarea>






--------------------------------------------------
