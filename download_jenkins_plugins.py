#!/usr/bin/python
import sys
import zipfile
import urllib
plugins_list=['cloudbees-folder 6.12', 
'junit 1.28', 
'ant 1.11', 
'git 4.2.2', 
'github 1.29.5', 
'mailer 1.32', 
'kubernetes 1.25.2', 
'ssh-slaves 1.31.2', 
'matrix-auth 2.5', 
'ldap 1.22', 
'performance 3.17', 
'email-ext 2.69', 
'copyartifact 1.43.1', 
'greenballs 1.15', 
'dashboard-view 2.12', 
'htmlpublisher 1.22', 
'golang 1.2', 
'ansible 1.0', 
'favorite 2.3.2', 
'openshift-client 1.0.32', 
'jira 3.0.15', 
'python 1.3', 
'blueocean 1.22.0', 
'openshift-pipeline 1.0.57', 
'ruby-runtime 0.12', 
'slack 2.39', 
'thinBackup 1.9', 
'ssh-agent 1.19', 
'view-job-filters 2.2', 
'global-build-stats 1.5', 
'build-metrics 1.3', 
'BlazeMeterJenkinsPlugin 4.7', 
'kubernetes-cli 1.8.2', 
'ssh 2.6.1', 
'metrics 4.0.2.6', 
'prometheus 2.0.6', 
'ansicolor 0.6.3', 
'influxdb 2.2', 
'gitbucket 0.8', 
'publish-over 0.22', 
'publish-over-ssh 1.20.1', 
'timestamper 1.11.2',
'embeddable-build-status 2.0.3']



def download_plugin(name,version):
    if version == "latest":
      pluginUrl = "http://updates.jenkins-ci.org/latest/%s.hpi" % name
    else:
      pluginUrl = "http://updates.jenkins-ci.org/download/plugins/%s/%s/%s.hpi" % (name,version,name)
    print "downloading: %s" % pluginUrl
    file = "%s.hpi" % name
    try:
    	urllib.urlretrieve (pluginUrl, file)
    except Exception,e:
       print e
       download_plugin (name, "latest")
    download_dependencies(file)

def download_dependencies(file):
    z = zipfile.ZipFile(file, "r")        
    manifestPath = "META-INF/MANIFEST.MF"        
    bytes = z.read(manifestPath)
    dependencies = [x for x in bytes.decode("utf-8").split("\n") if "Dependencies" in x]
    for dep in dependencies:
        _deps = dep.split(";")
        tlist = _deps[0]
        tlist.strip()
        dummy,_useful = tlist.split(' ')
        _list = _useful.split(",")
        for plugin in _list:
          plugin.strip()
          name,version = plugin.split(":")
          name.strip()
          version.strip()
          print "plugin name = %s" %name
          print "plugin version = %s " %version
          download_plugin(name,version)

#download_plugin("junit","1.19")
if __name__ == "__main__":
    for item in plugins_list:
      _item = item.strip()
      _items = _item.split(" ")
      _name = _items[0].strip()
      _version = _items[1].strip()
      print "download %s %s " % (_name, _version)
      download_plugin(_name,_version)
