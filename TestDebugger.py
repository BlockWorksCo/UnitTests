

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






def RunCommand(command):
    """
    """
    commandList = shlex.split(command)
    print('Executing '+str(commandList))
    p   = subprocess.Popen(commandList, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = p.communicate()

    return (out, err)





def TestLinuxDebugger():
    """
    """
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 

    #
    #
    #
    BuildForPlatform('Linux')

    #
    # Build the binary.
    #
    out,err = RunCommand('bash -c "cd ../Examples/DemoOne && Debug Main -ex quit"')
    print(out,err)







