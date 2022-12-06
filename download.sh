while read url; do
	curl $url -o ./UTC.dat
done < url_dutc.txt

while read url; do
	curl $url -o ./TAI.dat
done < url_tai.txt
