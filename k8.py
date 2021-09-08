#!/usr/bin/python3

import subprocess
import cgi
print('Access-Control-Allow-Origin: *')
print("content-type: text/html")
print()

f =cgi.FieldStorage()
cmd=f.getvalue("x")

if ("show" in cmd or "get" in cmd) and ("pod" in cmd or "pods" in cmd):
   output =subprocess.getoutput("sudo kubectl get pods --kubeconfig admin.conf")
   print("<pre>{}</pre>".format(output))
   
elif (("show" in cmd or "get" in cmd) and ("svc" in cmd or "Svc" in cmd)):
   output=subprocess.getoutput("sudo kubectl get svc --kubeconfig admin.conf")
   print("<pre>{}</pre>".format(output))
elif (("show" in cmd or "get" in cmd) and ("deployments" in cmd or "deployment" in cmd)):
   output=subprocess.getoutput("sudo kubectl get deployments --kubeconfig admin.conf")
   print("<pre>{}</pre>".format(output))
elif (("describe" in cmd or "Describe" in cmd) and ("pod" in cmd or "pods" in cmd)):
   output=subprocess.getoutput("sudo kubectl describe pods --kubeconfig admin.conf")
   print("<pre>{}</pre>".format(output)) 
else:
   print("Invalid Requirments !!")
