import subprocess
import string

def  stripNewline(s) :
    return string.replace(s, "\n", "")

def removeCommas(s) :
    return string.replace(s, ",", ".")

def buildCSV(l) :
    return ",".join(l)

if __name__ == "__main__":

    print "hash, author, authdate, committer, commitdate, subject, added, deleted, file"
    command = ['git', 'log', '--numstat', '--pretty=format:||%H||%an||%aI||%cn||%cI||%s']
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)

    for line in proc.stdout:
        if line.startswith("||"):
            cols = buildCSV(removeCommas(line).split("||"))
            cols = stripNewline(cols)
        if line[0].isdigit():
            filecol = buildCSV(line.split("\t"))
            filecol = stripNewline(filecol)
            print "{0},{1}".format(cols[1:], filecol)


