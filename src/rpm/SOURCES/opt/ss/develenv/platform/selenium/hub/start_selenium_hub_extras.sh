#!/bin/bash
cd /opt/ss/develenv/platform/selenium/hub/
/usr/bin/java -cp ../SeleniumGridExtras.jar:../selenium-server-standalone.jar org.openqa.grid.selenium.GridLauncherV3 -role hub -log log/hub_4444.log -hubConfig hub_4444.json
