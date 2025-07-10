How to mount a disk in linux and make it persistent across reboots.

1. Check for available disks:
   ```bash
   lsblk
   ```
2. Identify the disk you want to mount (e.g., `/dev/sdb1`).

in my case 
sda      8:0    0 931.5G  0 disk 
├─sda1   8:1    0   128M  0 part 
└─sda2   8:2    0 931.4G  0 part

3. Create a directory to mount the disk:
   ```bash
   sudo mkdir /mnt/data
    ```

4. Get the UUID of the disk:
   ```bash
   sudo blkid /dev/sda2
   ```
   This will output something like:
   ```
   /dev/sda2: LABEL="DATA" BLOCK_SIZE="512" UUID="some uuid" TYPE="ntfs" PARTLABEL="Basic data partition" PARTUUID="<part uuid>"
   ```

5. Take a copy of fstab:
   ```bash
   sudo cp /etc/fstab /etc/fstab.bak
   ```

6. Edit the fstab file to add the new disk:
   ```bash
   sudo vim /etc/fstab
    ```

7. Add the following line to the end of the file:
   ```
   UUID=FC4C9C474C9BFA9A /mnt/data ntfs defaults,nofail,uid=1000,gid=1000,umask=0022 0 0
   ```
   Replace `some uuid` with the actual UUID you got from the `blkid` command.

8. Save and exit the editor.

9. Test the fstab entry by mounting all filesystems:
   ```bash
   sudo mount -a
   ```

10. Verify that the disk is mounted:
    ```bash
    df -h /mnt/data
    ```

11. List the contents of the mounted directory to ensure it is accessible:
    ```bash
    ls /mnt/data
    ```
If everything is set up correctly, you should see the contents of the disk in the `/mnt/data` directory.



