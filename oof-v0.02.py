#!/usr/python/env python
#
#################################################################################################################
# v 0.02 - orphan object finder by hubert.wisniewski@gmail.com (version with functions)
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
#  The script parses a file with network objects to see if there are entries which are not used by any network-object-group.
#  It doesn't support all features mentioned in Cisco documentation. In this version (0.01) it can analyze following
#  elements:
#
#  object-group network OBJECT-GROUP-NAME
#  |-network-object host IP
#  |-network-object IP Mask
#  |-network-object object OBJECT-NAME
#  |-group-object GROUP-OBJECT-NAME <-- not supported yet
#
#
#  object network OBJECT-NAME
#  |-subnet IP MASK
#  |-host IP
#  |-range IP IP
#  |-fqdn
#
#
##################################################################################################################
import sys, getopt

filename = sys.argv[1]
filename = str(filename)
debugmode = sys.argv[2:3]

if debugmode == ['-d']:
 debugmode = "on"

#table-object-network and one for function
tonf = ton = []

#table-object-group-network and one for function
tognf = togn = []

#table tmp in function
tabletmp = []

#function definition - open file
def openfile(p1,p2):
 f = open(p1, p2)
 return f

#function definition - read file
def readfile(filen,objecttype,objectstart,objectend,linelenght,tabletmp):
 for line in filen:
  eol = len(line)-1
  if line[objectstart:objectend] == objecttype:
   onn = line[linelenght:eol]
   tabletmp.append([onn])
   if debugmode == "on":
    print line[objectstart:objectend] + ' ->' + objecttype + ' ' + onn
 return tabletmp

#function definition - remove duplicates
def removeduplicates(tab1,tab2):
 for i in tab1:
  if debugmode == "on":
#  print (str(tab1) +" i\n")
   print i[0]+"\n"
  for j in tab2:
   if debugmode == "on":
#    print (str(tab2)+" j\n")
    print j[0]+"\n"
   if i[0] == j[0]:
    tab2.remove(j)
    if debugmode == "on":
     print('removed\n')
 return tab2

#main function start here:

#call function - open file and return f
f = openfile(filename,'r')
ton = readfile(f,'object network',0,14,15,tonf)

#call function - open file and return f
f = openfile(filename,'r')
togn = readfile(f,'network-object object',1,22,23,tognf)

if debugmode == "on":
 print '\n\nNetwork-object table:'
 for i in togn:
  print i

print("\n\n")

if debugmode == "on":
 print '\n\nObject network table:'
 for i in ton:
  print i

ton = removeduplicates(togn,ton)

print("Orphan objects:")
for i in ton:
 print i
