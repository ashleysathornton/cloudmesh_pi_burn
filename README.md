
!!! This is not yet working

cm-burn —name  red[5,7] -key ~/.ssh/id_rsa.pub —ip 192.168.1.[5,7] —image ~/Downloads/rasbian…..

# Install

git clone ...
cd cm-burn
pip install .

or


# mount idea

do the following so we can modify

mkdir linux
mkdir boot
cp  ../*.img 00.img
brew cask install osxfuse
brew install ext4fuse
hdiutil mount 00.img 
ext4fuse /dev/disk2s2 linux
less linux/etc/hosts

# Links

* https://github.com/cloudmesh/cloudmesh.pi/blob/dev/bin/cm-burn
* http://www.microhowto.info/howto/mount_a_partition_located_inside_a_file_or_logical_volume.html
* http://www.janosgyerik.com/mounting-a-raspberry-pi-image-on-osx/
* https://github.com/Hitabis/pibakery
* http://osxdaily.com/2014/03/20/mount-ext-linux-file-system-mac/
* https://linuxconfig.org/how-to-mount-rasberry-pi-filesystem-image
* https://www.jeffgeerling.com/blogs/jeff-geerling/mounting-raspberry-pis-ext4-sd
* https://blog.hypriot.com/post/cloud-init-cloud-on-hypriot-x64/