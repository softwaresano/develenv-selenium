#!/bin/bash
minor_version=$(grep "%define selenium_version" src/rpm/SPECS/selenium.spec |awk '{print $3}')
chromedriver_version=$(grep "%define chromedriver_version" src/rpm/SPECS/selenium.spec |awk '{print $3}')
geckodriver_version=$(grep "%define geckodriver_version" src/rpm/SPECS/selenium.spec |awk '{print $3}')
major_version=$(echo $minor_version|sed s:"\.[0-9]*$":"":g)
selenium_url=https://selenium-release.storage.googleapis.com/$major_version/selenium-server-standalone-${minor_version}.jar
chrome_driver_url=https://chromedriver.storage.googleapis.com/${chromedriver_version}/chromedriver_linux64.zip
gecko_driver_url=https://github.com/mozilla/geckodriver/releases/download/v${geckodriver_version}/geckodriver-v${geckodriver_version}-linux64.tar.gz
rm -Rf target/artifacts
mkdir -p target/artifacts/drivers
cd target/artifacts
curl -k $selenium_url > selenium-server-standalone.jar
cd drivers
curl -k -O $chrome_driver_url
zip_file=$(basename $chrome_driver_url)
unzip $zip_file
rm -Rf $zip_file
curl -k -L $gecko_driver_url|tar xfz -
