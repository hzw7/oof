#!/usr/python/env python
#
#################################################################################################################
# v 0.01 - orphan object finder by hubert.wisniewski@gmail.com
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

f = open(filename, 'r')
id = 0

#table-object-network
ton = []

#table-object-group-network
togn = []


for line in f:
 id = id + 1
 eol = len(line)-1


 if line[0:14] == 'object network':
# object network name
  onn = line[15:eol]
  ton.append([id,onn])
  if debugmode == "on":
   print line[0:14] + ' -> OBJECT NAME: ' + onn


 if line[1:22] == 'network-object object':
# network object object name
  noon = line[23:eol]
  togn.append([id,noon])
  if debugmode == "on":
   print '|-'+line[1:22] +' -> NETWORK-OBJECT OBJECT NAME: '+ noon

if debugmode == "on":
 print '\n\nNetwork-object table:'
 for i in togn:
  print i

print("\n\n")

if debugmode == "on":
 print '\n\nObject network table:'
 for i in ton:
  print i


for i in togn:
 if debugmode == "on":
  print ("togn i")
  print i[1]
 for j in ton:
  if debugmode == "on":
   print ("ton j")
   print j[1]
  if i[1] == j[1]:
   ton.remove(j)
   if debugmode == "on":
    print('removed\n')

print("Orphan objects:")

for i in ton:
 print i
