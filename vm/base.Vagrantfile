Vagrant.configure("2") do |config|
  config.vm.define 'cryptovm', primary: true do |cryptovm|
    cryptovm.vm.box = "ubuntu/trusty64"
    cryptovm.vm.synced_folder "../", "/vagrant", disabled: false
    cryptovm.vm.provision :shell, path: "setup.sh"
    cryptovm.vm.network :forwarded_port, guest: 80, host: 8082
    #PORTS
  end
end