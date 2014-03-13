

from nose import with_setup
import sys
import vagrant
import subprocess
import shlex
import os



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

    assert vm.status()['default'] == 'running' 
    open('sshConfig','w').write(vm.ssh_config())
    out, err = RunCommand('ssh -F sshConfig default -C '+sshCommand)

    return (out, err)





def TestSSH():
    """
    """
    print('ssh tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 

    out,err = RunVagrantSSHCommand('uname -a')
    print(out,err)

    assert err == '', 'stderr was not blank.'
    assert out == 'Linux raring32-vanilla 3.8.0-19-generic #30-Ubuntu SMP Wed May 1 16:36:13 UTC 2013 i686 i686 i686 GNU/Linux\n', 'uname was not correct: %s'%(err)





def BuildForPlatform(platformName, binaryName='../Examples/DemoOne/Output/Main'):
    """
    """
    #
    # Remove the binary.
    #
    try:
        os.remove(binaryName)
    except OSError:
        pass

    #
    # Build the binary.
    #
    out,err = RunCommand('bash -c "cd ../Examples/DemoOne && Build PLATFORM=%s clean all"'%(platformName))
    print(out,err)

    #
    # Test the binary exists.
    #
    assert os.path.exists(binaryName), 'Binary not produced (%s)'%(binaryName)
    assert out != '', 'no text from build process %s'%(err)



def TestMSP430Build():
    """
    """
    print('MSP430 tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 

    BuildForPlatform('MSP430')



def TestSTM32Build():
    """
    """
    print('STM32 tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 

    BuildForPlatform('STM32')


def TestLinuxBuild():
    """
    """
    print('Linux tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 

    BuildForPlatform('Linux')


def TestWin32Build():
    """
    """
    print('Window tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 

    BuildForPlatform('Win32', binaryName='../Examples/DemoOne/Output/Main.exe')


def TestRaspberryPiBuild():
    """
    """
    print('RaspberryPi tests')
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 

    BuildForPlatform('RPI')







