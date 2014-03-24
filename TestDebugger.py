

from nose import with_setup
import sys
import vagrant
import subprocess
import shlex
import os
from Utilities import *
import pexpect



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
    Blaa
    """
    vm  = vagrant.Vagrant()
    assert vm.status()['default'] == 'running' 

    #
    # Build the binary.
    #
    BuildForPlatform('Linux')

    #
    # Debug the binary.
    #
    child   = pexpect.spawn('bash -c "cd ../Examples/DemoOne && Debug -i mi"')
    child.expect('\(gdb\) ')

    child.sendline('-file-exec-and-symbols Output/Main')
    child.expect('\(gdb\) ')
    print('\n** %s **\n'%child.before)

    child.sendline('-break-insert main')
    child.expect('\(gdb\) ')
    print('\n** %s **\n'%child.before)

    child.sendline('-exec-run')
    child.expect('\(gdb\) ')
    print('\n** %s **\n'%child.before)

    child.expect('\(gdb\) ')
    print('\n** %s **\n'%child.before)
    assert child.before.find('stopped,reason="breakpoint-hit"') != -1

    child.sendline('-gdb-exit')







