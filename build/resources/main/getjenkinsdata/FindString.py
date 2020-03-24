#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

if leftSearch == '' and rightSearch == '':
    print "At least one search parameter (left or right) must be specified."
    sys.exit(1);

# Output variable should be recognized as global, add this if there's a scoping issue
# build_id = 0;

request = HttpRequest(server)   # server is from our input parameter, a jenkins.server derived from httpserver
path = '/' + jobPath.strip('/') + '/' + buildNumber + '/consoleText'
# response = request.doRequest(method = 'GET')
response = request.get(path)

if not response.isSuccessful():
    print "Failed to retrieve the provided URL."
    print "Http Status: %s" % response.status
    response.errorDump()
    sys.exit(1)
    
print "Retrieved: " + path
print "Http Status: %s" % response.status 

r_lines = str.splitlines(str(response.response))  # response.response returns unicode

foundResults = False;

if leftSearch = '' : 
    for l in r_lines : 
        if l.find(leftSearch) > -1: 
            result = str(l[ l.find(leftSearch) + len(leftSearch) : ])
            print "Found: ''" + str(result) + "'\r\n";
            foundResults = True;
elif rightSearch = '' : 
    for l in r_lines : 
        if l.rfind(rightSearch) > -1: 
            result = str(l[ : l.rfind(rightSearch) ])
            print "Found: '" + str(result) + "'\r\n";
            foundResults = True;
else : 
    for l in r_lines : 
       if l.find(leftSearch) > -1 and l.rfind(rightSearch) > -1 : 
           result = int(l[l[ l.find(leftSearch) + len(leftSearch) : l.rfind(rightSearch)])
           print "Found: '" + str(result) + "'\r\n";
           foundResults = True;

# We use a boolean flag instead of checking if result = '' to be precise 
# because it's possible that the search will successfully find an empty result, e.g. IPADDRESS=''

if foundResults = False : 
    print 'No results were found.';
    


