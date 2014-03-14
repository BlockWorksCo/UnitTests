

from nose import with_setup
import sys
import vagrant
import subprocess
import shlex
import os
from Utilities import *



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







