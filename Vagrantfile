# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "centos/8"
  config.ssh.insert_key = false

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  #config.vm.box_url = "-"
  


  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb, override|
  
  # #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  #   override.vm.box_url = "https://cloud.centos.org/centos/7/vagrant/x86_64/images/CentOS-7.box"
  # end
  # config.vm.provider "libvirt" do |lv, override|
  #    # Customize the amount of memory on the VM:
  #    lv.memory = "1024"
  #    override.vm.box_url = "https://cloud.centos.org/centos/7/vagrant/x86_64/images/CentOS-7.Libvirt.box"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.


  config.vm.define 'workbook' do |workbook|
    workbook.vm.hostname = "workbook"
    workbook.vm.synced_folder './', '/vagrant'
    workbook.vm.provider "virtualbox" do |v, override|
      v.memory = 512
      override.vm.box_url = "https://cloud.centos.org/centos/8/vagrant/x86_64/images/CentOS-8-Vagrant-8.1.1911-20200113.3.x86_64.vagrant-virtualbox.box"
    end
    workbook.vm.provider "libvirt" do |lv, override|
      # Customize the amount of memory on the VM:
      lv.memory = "512"
      override.vm.box_url = "https://cloud.centos.org/centos/8/vagrant/x86_64/images/CentOS-8-Vagrant-8.1.1911-20200113.3.x86_64.vagrant-libvirt.box"
   end
   workbook.vm.provision "shell", inline: <<-SHELL
   dnf install git epel-release python2-setuptools python2 -y
   pip2 install paramiko
   rm -rf lymworkbook
   git clone https://github.com/kushaldas/lymworkbook.git
   cd lymworkbook; sudo python2 setup.py install

   git clone https://github.com/magicmonty/bash-git-prompt.git /home/vagrant/.bash-git-prompt --depth=1
   echo "if [ -f "/home/vagrant/.bash-git-prompt/gitprompt.sh" ]; then
   GIT_PROMPT_ONLY_IN_REPO=1
   source /home/vagrant/.bash-git-prompt/gitprompt.sh
fi" | tee -a /home/vagrant/.bashrc

 SHELL
  end


  config.vm.define 'webserver', autostart: false  do |webserver|
    webserver.vm.hostname = "app-webserver"
    webserver.vm.provider "virtualbox" do |v, override|
      v.memory = 512
      override.vm.box_url = "https://cloud.centos.org/centos/8/vagrant/x86_64/images/CentOS-8-Vagrant-8.1.1911-20200113.3.x86_64.vagrant-virtualbox.box"
    end
    webserver.vm.provider "libvirt" do |lv, override|
      # Customize the amount of memory on the VM:
      lv.memory = "512"
      override.vm.box_url = "https://cloud.centos.org/centos/8/vagrant/x86_64/images/CentOS-8-Vagrant-8.1.1911-20200113.3.x86_64.vagrant-libvirt.box"
   end
  end

  config.vm.define 'spybox', autostart: false do |spybox|
    spybox.vm.hostname = "spybox"
    spybox.vm.box = "debian/buster64"
    spybox.vm.box_version = "10.0.0"
    spybox.vm.synced_folder './', '/vagrant', disabled: true
    spybox.vm.provider "virtualbox" do |v, override|
      v.memory = 512
    end
    spybox.vm.provider "libvirt" do |lv, override|
      # Customize the amount of memory on the VM:
      lv.memory = "512"
   end

  end
end
