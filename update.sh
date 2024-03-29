#!/bin/bash -ex
minor_version=$(grep --color=no -Po '(?<=      <version>).*(?=<)' pom.xml)
chromedriver_version=$(grep --color=no -Po '(?<=chromedriver-py="=).*(?=\")' Pipfile)
geckodriver_version=$(curl -I -f -s https://github.com/mozilla/geckodriver/releases/latest | grep --color=no -Po '(?<=releases/tag/).*(?=\r)')
[[ ${geckodriver_version} == '' ]] && exit 1
major_version=$(echo $minor_version | sed s:"\.[0-9]*$":"":g)
selenium_grid_extras_version=2.0.4
selenium_url="https://github.com/SeleniumHQ/selenium/releases/download/selenium-${minor_version}/selenium-server-${minor_version}.jar"
selenium_grid_extras_url=https://github.com/groupon/Selenium-Grid-Extras/releases/download/v${selenium_grid_extras_version}/SeleniumGridExtras-${selenium_grid_extras_version}-SNAPSHOT-jar-with-dependencies.jar
chrome_driver_url="https://storage.googleapis.com/chrome-for-testing-public/${chromedriver_version:?}/linux64/chromedriver-linux64.zip"
gecko_driver_url=https://github.com/mozilla/geckodriver/releases/download/${geckodriver_version}/geckodriver-${geckodriver_version}-linux64.tar.gz
rm -Rf target/artifacts
mkdir -p target/artifacts/drivers
cd target/artifacts
curl -f -k -L "${selenium_url:?}" >selenium-server-standalone.jar || exit 1
curl -f -k -L "${selenium_grid_extras_url:?}" >SeleniumGridExtras.jar || exit 1
curl -f -k -L $gecko_driver_url | tar xfz -

cd drivers || exit 1
curl -f -k -O $chrome_driver_url
zip_file=$(basename $chrome_driver_url)
unzip -j "${zip_file:?}" chromedriver-linux64/chromedriver
rm -Rf $zip_file
curl -k -L $gecko_driver_url | tar xfz -
