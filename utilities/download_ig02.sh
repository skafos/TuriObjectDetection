mkdir -p ~/Downloads/ig02
cd ~/Downloads/ig02

printf "%s\n Downloading bikes %s\n"
curl https://lear.inrialpes.fr/people/marszalek/data/ig02/ig02-v1.0-bikes.zip > bikes.zip
printf "%s\n Downloading cars %s\n"
curl https://lear.inrialpes.fr/people/marszalek/data/ig02/ig02-v1.0-cars.zip > cars.zip
printf "%s\n Downloading people %s\n"
curl https://lear.inrialpes.fr/people/marszalek/data/ig02/ig02-v1.0-people.zip > people.zip

unzip bikes.zip
mv readme.txt readme-bikes.txt

unzip cars.zip
mv readme.txt readme-cars.txt

unzip people.zip
mv readme.txt readme-cars.txt

rm bikes.zip cars.zip people.zip 