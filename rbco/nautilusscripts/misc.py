import os
import sys
import nautilus
import util
from . import PyZenity
import commands
from .wrapper import nautilus_script
from clom import clom, AND

@nautilus_script
def backup():
    """
    Copies FILE to FILE.bak . If FILE.bak exists then first moves FILE.bak to FILE.bak.1 .
    """
    f = nautilus.files[0]

    # Removes trailing /
    if f[-1] == "/":
        f = f[:-1]

    bak = f + ".bak"
    bak1 = f + ".bak.1"

    # Checks FILE existence
    if not os.access(f, os.R_OK):
        print "ERROR: " + f + " not readable."
        sys.exit(1)

    # Removes FILE.bak.1
    if os.access(bak1, os.F_OK):
        os.system("rm -rf \"%s\"" % bak1)

    # Moves FILE.bak to FILE.bak.1
    if os.access(bak, os.F_OK):
        os.system("mv \"%s\" \"%s\"" % (bak, bak1))

    # Copies FILE to FILE.bak
    if os.access(f, os.F_OK):
        os.system("cp -R \"%s\" \"%s\"" % (f, bak))

@nautilus_script
def change_owner_to_me():
    user = os.getenv('USER')
    group = util.user_main_group(user)
    files = ' '.join([util.escape_space(path) for path in nautilus.paths])

    cmd = 'chown -R %s:%s %s' % (user, group, files)
    util.gksu(cmd)

@nautilus_script
def open_in_terminal():
    dirs_to_open = [p for p in nautilus.paths if os.path.isdir(p)]

    if (not dirs_to_open) or (len(dirs_to_open) != len(nautilus.files)):
        dirs_to_open.append(nautilus.current_path)

    xterm = getattr(clom, 'x-terminal-emulator')
    for p in dirs_to_open:
        AND(clom.cd(p), xterm).shell()

@nautilus_script
def open_real_path():
    def format_path(p):
        return escape_space(os.path.realpath(p))

    if nautilus.paths:
        paths_str = ' '.join([format_path(p) for p in nautilus.paths])
    else:
        paths_str = format_path(nautilus.current_path)

    os.system('nautilus %s' % paths_str)

@nautilus_script
def execute_custom_command():
    cmd_template = '\n'.join([
        'source /etc/bash.bashrc',
        '(%s) > %s'
    ])

    cmd_to_exec = PyZenity.GetText('Command to execute on the selected items:')

    if cmd_to_exec:
        paths_str = ' '.join([util.escape_space(p) for p in nautilus.paths])

        if cmd_to_exec.find('$FILES') >= 0:
            cmd_to_exec = cmd_to_exec.replace('$FILES', paths_str)
        else:
            cmd_to_exec += ' ' + paths_str

        if PyZenity.Question('Execute the following command ?\n\n%s' % cmd_to_exec):
            temp_filename = commands.getoutput('mktemp')
            cmd = cmd_template % (cmd_to_exec, temp_filename)
            os.system(cmd)
            PyZenity.TextInfo(temp_filename)
