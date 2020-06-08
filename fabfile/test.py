# -*- coding: utf-8 -*-
import sys, os
from fabric import *
from invoke import task
from datetime import datetime

FABDIR=os.getcwd()

#------------------------------------------------------------------
# fab -H x.x.x.x test
#------------------------------------------------------------------
@task
def test(c):
    '''fab -H x.x.x.x test'''
    print("host", c.host) 

    c.local("whoami", echo=True)
    c.local("pwd", echo=True)
    c.run("hostname", echo=True)
    c.sudo("whoami", echo=True, pty=True)
    c.sudo("cat /etc/sudoers |tail", warn=True, pty=True, echo=True)
    c.run('ls -l /tmp2', echo=True, warn=True)


#------------------------------------------------------------------
# fab -H x.x.x.x test2
#------------------------------------------------------------------
@task
def test2(c):
    '''fab -H x.x.x.x test2'''
    print("host", c.host) 

    result = c.local("whoami", echo=True)
    result = c.local("pwd", echo=True)
    result = c.run("hostname", echo=True)
    result = c.sudo("whoami", echo=True, pty=True)
    result = c.sudo("cat /etc/sudoers |tail", warn=True, pty=True, echo=True)
    result = c.run('ls -l /tmp2', echo=True, warn=True)
    print("c.host", "result")

