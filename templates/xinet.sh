#setup xinetd server
PORT=REPLACE
cp /vagrant/problems/$PROBLEM/$PROBLEM.xinetd /etc/xinetd.d/$PROBLEM
echo -e "\n$PROBLEM $PORT/tcp\n" >> /etc/services

#***** Fill in any of the service (server.py etc) files you need to run here *****
files=()
#Copy service files over
for fname in "${files[@]}"
do
	mkdir -p /home/vagrant/problems/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /home/vagrant/problems/$PROBLEM/$fname
done

service xinetd restart
