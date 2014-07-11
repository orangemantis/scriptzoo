#Paul Bunyan gets logs, get it?
import ftplib
import csv

class PaulBunyan:
    #extend by adding a file format checker method
    def __init__(self, user = '', pw = '', hfn = ''):
        self.user = user
        self.pw = pw
        self.hfn = hfn #host file name
        self.hostNames = []
        self.failedHost = []
        
    def getHostNames(self, hfn = ''):
        response = False
        self.hfn = hfn if (hfn != '') else self.hfn
        
        if (self.hfn != ''):
            with open(self.hfn, newline = '') as hfcsv:
                hfReader = csv.reader(hfcsv, delimiter = ',', quotechar = '"')
                for row in hfReader:
                    self.hostNames.append(row[0])
                    if (len(self.hostNames) > 0):
                        response = True
        #returns true if host names added         
        return response
    
    def fetch(self, user = '', pw = '', fdir = '', fn = ''):
        filesFound = 0
        
        self.user = user if (user != '') else self.user
        self.pw = pw if (pw != '') else self.pw
        
        
        if (self.user != '' 
            and self.pw != ''  
            and self.hfn != '' 
            and fn != ''):

            response = self.getHostNames(self.hfn)

            if (response):
                for h in self.hostNames:
                    ftp = ftplib.FTP(h)
                    ftp.login(self.user, self.pw)
                    
                    if (fdir != ''):
                        ftp.cwd(fdir)
                        
                    status = ftp.retrbinary(('RETR ' + fn), open((h + '_' + fn), 'wb').write)
                    print(status)
                    if (status != '226 Transfer complete'):
                        self.failedHost.append(h)
                    else:
                        filesFound += 1
                        
                    ftp.quit()
                
        return filesFound

logs = PaulBunyan('user', 'password', 'hostlist.txt')
status = logs.fetch(fdir = 'testlogs', fn = 'test.txt')
print(status)
