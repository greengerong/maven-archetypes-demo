import sys
import subprocess

assert sys.argv.__len__() >= 2, "should given project name."

project = sys.argv[1].lower()

words = "".join(list(word.strip().capitalize() for word in project.split("-")) )
directiveName = words[0:1].lower() + words[1:]

cmd = "mvn archetype:generate -DinteractiveMode=false -DarchetypeGroupId=<archetype-groupId>  -DarchetypeArtifactId={}  -DarchetypeVersion=<archetype-version> -DgroupId=<my.groupid>  -DartifactId=<my-artifactId> -Dversion=<version>  -DdirectiveName={}".format(project, directiveName)

print "execute command : " + cmd  + "\r\n"
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
p.wait()
