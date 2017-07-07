#!/bin/bash
cd /opt/ss/develenv/platform/selenium/node/
/usr/bin/java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -Dwebdriver.gecko.driver=/usr/bin/geckodriver -cp ../SeleniumGridExtras.jar:../selenium-server-standalone.jar  org.openqa.grid.selenium.GridLauncherV3 -role node -nodeConfig node_5566.json -log log/node_5566.log 
