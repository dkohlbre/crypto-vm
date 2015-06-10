# Make sure your init script is named correctly
# setup the init script
cp /vagrant/problems/$PROBLEM/$PROBLEM.init /etc/init.d/$PROBLEM


#***** Fill in any of the service (server.py etc) files you need to run here *****
files=()
#Copy service files over
for fname in "${files[@]}"
do
	mkdir -p /home/vagrant/problems/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /home/vagrant/problems/$PROBLEM/$fname
done

# Start the service
update-rc.d $PROBLEM defaults
service $PROBLEM start &
