

import sys
import vagrant
import subprocess
import shlex
import os



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


