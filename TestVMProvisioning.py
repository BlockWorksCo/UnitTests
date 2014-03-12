

from nose import with_setup
import sys
import vagrant
import subprocess
import shlex



def setup_module():
    """
    """
    vm  = vagrant.Vagrant()
    print('Vagrant down.')
    vm.halt()
    print('Vagrant up.')
    vm.up()
    print('vagrant status')



def teardown_module():
    """
    """
    vm  = vagrant.Vagrant()
    vm.halt()






def RunCommand(command):
    """
    """
    commandList = shlex.split(command)
    print('Executing '+str(commandList))
    p   = subprocess.Popen(commandList, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = p.communicate()

    return (out, err)


def RunVagrantSSHCommand(sshCommand):
    """
    """
    vm  = vagrant.Vagrant()
    open('sshConfig','w').write(vm.ssh_config())
    out, err = RunCommand('ssh -F sshConfig default -C '+sshCommand)

    return (out, err)





def TestSSH():
    """
    """
    print('ssh tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 

    out,err = RunVagrantSSHCommand('ls -la')
    print(out,err)


def TestMSP430Build():
    """
    """
    print('MSP430 tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 


def TestSTM32Build():
    """
    """
    print('STM32 tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 


def TestLinuxBuild():
    """
    """
    print('Linux tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 


def TestRaspberryPiBuild():
    """
    """
    print('RaspberryPi tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 







