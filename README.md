## Ansible-Play

A simple project created to be able to run a hello-world sample to check syntax quickly (and locally)

#### MVP Playbook

Useful for checking single line syntax

```
jmaki@jmaki-pro /build/playground/ansible-play
$ ./mvp.sh 
 [WARNING]: provided hosts list is empty, only localhost is available


PLAY ***************************************************************************

TASK [debug] *******************************************************************
ok: [localhost] => {
    "msg": "bob says hi there"
}

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0   
```

#### Hello-World Playbook

Useful for checking role based syntax (including template generation)

```
jmaki@jmaki-pro /build/playground/ansible-play
$ ./hello-world.sh 
 [WARNING]: provided hosts list is empty, only localhost is available


PLAY ***************************************************************************

TASK [hello-world : Test jinja2template] ***************************************
changed: [localhost]
--- before
+++ after: dynamically generated
@@ -0,0 +1,10 @@
+
+ExecStart=/usr/bin/docker run -u root --net host --name zavikon \
+  -v "/srv/zavikon:/srv/zavikon:z" \
+  -v "/srv/zavikon/gc_logs:/tmp/gc:z" \
+  quay.io/ntoggle/zavikon:VERSION \
+    java -jar /app/zavikon.jar \
+    -server -Xmx8G -Xms8G -XX:NewSize=6G -XX:+PerfDisableSharedMem -XX:+HeapDumpOnOutOfMemoryError -XX:+DisableExplicitGC -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+CMSScavengeBeforeRemark -XX:+ScavengeBeforeFullGC -XX:CMSInitiatingOccupancyFraction=70 -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=2222 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.rmi.port=2222 -Dcom.sun.management.jmxremote.local.only=false -Djava.rmi.server.hostname=127.0.0.1 -Dlogback.configurationFile=/srv/zavikon/logback.xml \
+    -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintGCDateStamps -XX:+PrintTenuringDistribution -Xloggc:/srv/zavikon/zavikon%i-gc.log -verbose:gc \
+    --name zavikon --port 8080 
+


PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=1    unreachable=0    failed=0   
```